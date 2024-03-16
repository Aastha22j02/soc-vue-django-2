# views.py
from rest_framework import generics
from .models import Rule
from .serializers import RuleSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import requests
from django.http import JsonResponse
from paramiko import SSHClient, AutoAddPolicy, SSHException

class RuleListByCategory(generics.ListAPIView):
    serializer_class = RuleSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Rule.objects.filter(category__name=category_name)

class RuleList(generics.ListAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer


 
import os
from rest_framework import viewsets
from rest_framework.response import Response
from paramiko import SSHClient, AutoAddPolicy, SSHException, RSAKey
import io
 
def save_private_key_to_file(private_key_content):
    project_folder = os.path.dirname(os.path.abspath(__file__)) 
    private_key_file_path = os.path.join(project_folder, 'private_key.pem')
    with open(private_key_file_path, 'w') as key_file:
        key_file.write(private_key_content)

    return private_key_file_path
 
def install_wazuh_agent(server):
    ip_address = server['ip_address']
    ssh_username = server['ssh_username']
    ssh_private_key = server['private_key']
    os_type = server['os_type']
 
    try:
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    
        if os_type == 'Ubuntu':
            ssh_password = server['ssh_password']
            print("connection...")
            ssh_client.connect(
                ip_address,
                username=ssh_username,
                password=ssh_password 
                 )          
        else:
            print("Start connection")
            private_key_str  = server['private_key']
            private_key_file = RSAKey(file_obj = io.StringIO(private_key_str))
            # private_key_file = save_private_key_to_file(ssh_private_key)

       
            ssh_client.connect(
                ip_address,
                username=ssh_username,
                pkey=private_key_file
            )
            print("connection created")

        if os_type == 'Ubuntu':
            print ("script is start")
            wazuh_script = (
                "curl -so wazuh-agent.deb https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.5.2-1_amd64.deb && "
                # f"sudo dpkg -i ./wazuh-agent.deb && "
                f"sudo WAZUH_MANAGER='172.16.1.139' WAZUH_AGENT_GROUP='default' dpkg -i ./wazuh-agent.deb &&"
                f"sudo systemctl start wazuh-agent"              
            )
        elif os_type == 'Redhat':
            print("Rhel")

            # CentOS-specific installation steps
            wazuh_script = (
                "sudo WAZUH_MANAGER='172.16.1.59' WAZUH_AGENT_GROUP='default' yum install -y https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.4-1.x86_64.rpm &&"        
                f"sudo systemctl start wazuh-agent"
            )      
            print("successfull install")
        elif os_type == 'CentOS':
            # CentOS installation script (unchanged)
            print("centos")
            wazuh_script = (
                "sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' yum install -y https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.4-1.x86_64.rpm &&"        
                f"sudo systemctl start wazuh-agent"
            )
       
        else:
            return False, "Unsupported OS type."
 
        stdin, stdout, stderr = ssh_client.exec_command(wazuh_script)

        output = "\n".join(stdout.read().decode('utf-8').splitlines())

        ssh_client.close()

        return True, output

    except SSHException as e:
            return False, f"SSH Error: {str(e)}"

    except Exception as e:
            return False, str(e)

class OnboardViewSet(viewsets.ModelViewSet):

    def create(self, request):

        if request.method == 'POST':
            server = request.data
            try:
                success, output = install_wazuh_agent(server)
                if success:
                    return Response({'success': success, 'output': output})
                else:
                    return Response({'success': success, 'error': output}, status=400)
            except Exception as e:
                return Response({'success': False, 'error': str(e)}, status=500)
        return Response({'Methods': 'Not POST'})


                  
 
## For  Window server ##
 
from winrm.protocol import Protocol
from requests.exceptions import HTTPError, RequestException
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
import time
 
import winrm
 
def install_agent_on_windows(winrm_url, winrm_username, winrm_password):
    try:
        session = winrm.Session(winrm_url, auth=(winrm_username, winrm_password), transport='ntlm')
        print("Session created successfully!")
 
        try:
           
            install_command = (
                
                'Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.5.4-1.msi -OutFile wazuh-agent.msi; msiexec.exe /i wazuh-agent.msi /q WAZUH_MANAGER=\'172.16.1.139\' WAZUH_REGISTRATION_SERVER=\'172.16.1.139\';  '
            )
            print("File Downloaded success")
            start_service = (
                'NET START Wazuh '
            )
            print("Service started successfully")
            result_install = session.run_cmd('powershell', [install_command])
            time.sleep(10)
            result_install = session.run_cmd('powershell', [start_service])
            print(result_install)
 
            if result_install.status_code == 0:
                return True, "Agent installed successfully"
            else:
                return False, f"Failed to install agent. Exit code: {result_install.status_code}, Output: {result_install.std_err}"
 
        except Exception as install_error:
            return False, f"Error installing package: {str(install_error)}"
 
    except Exception as session_error:
        return False, f"Error creating session: {str(session_error)}"
 
class OnboardWindow(viewsets.ModelViewSet):
 
    def create(self, request):
        if request.method == 'POST':
            server = request.data
 
            try:
                success, output = install_agent_on_windows(
                    server['ip_address'],
                    server['ssh_username'],
                    server['ssh_password'],
                )
 
                if success:
                    return Response({'success': True, 'message': output}, status=200)
                else:
                    return Response({'success': False, 'error': output}, status=400)
            except Exception as e:
                return Response({'success': False, 'error': str(e)}, status=500)
 
        return Response({'Methods': 'Not POST'}, status=405)