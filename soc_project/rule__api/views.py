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

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from paramiko import SSHClient, AutoAddPolicy, SSHException, RSAKey
import io

def install_wazuh_agent(server):
    ip_address = server['ip_address']
    ssh_username = server['ssh_username']
    # ssh_password = server['ssh_password']
    # private_key_path = server['/home/ubuntu/.ssh/id_rsa']  # Add this line to get private key path  "/home/ubuntu/.ssh/id_rsa"
    private_key_str = server['private_key']  # Private key as a string

    os_type = server['os_type']

    try:
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())

        # Load the private key
        # private_key = RSAKey(filename=private_key_path)
        private_key = RSAKey(file_obj=io.StringIO(private_key_str))


        ssh_client.connect(
            ip_address,
            username=ssh_username,
            # password=ssh_password,
            pkey=private_key,  # Use private key for authentication
        )

        if os_type == 'Ubuntu':
            # Ubuntu installation script (unchanged)
            wazuh_script = (
                "curl -so wazuh-agent.deb https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.5.2-1_amd64.deb && "
                f"sudo WAZUH_MANAGER='172.16.1.64' WAZUH_AGENT_GROUP='default' dpkg -i ./wazuh-agent.deb &&"
                f"sudo systemctl start wazuh-agent"
            )
        elif os_type == 'CentOS':
            # CentOS installation script (unchanged)
            wazuh_script = (
                "curl -so wazuh-agent.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.2-1.x86_64.rpm && "
                f"sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' rpm -i ./wazuh-agent.rpm &&"
                f"sudo systemctl start wazuh-agent"
            )
        elif os_type == 'Redhat':

            # RHEL installation script
            wazuh_script = (
                "touch demo.txt && "
                "sudo rpm --import https://packages.wazuh.com/key/GPG-KEY-WAZUH && "
                "echo -e '[wazuh]\n"
                "name=Wazuh\n"
                "enabled=1\n"
                f"baseurl=https://packages.wazuh.com/4.x/yum/\n"
                "gpgcheck=1\n"
                "gpgkey=https://packages.wazuh.com/key/GPG-KEY-WAZUH' | sudo tee /etc/yum.repos.d/wazuh.repo && "
                "sudo yum install -y wazuh-agent && "
                f"sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' systemctl enable wazuh-agent && "
                f"sudo systemctl start wazuh-agent"
            )
        elif os_type == 'Fedora':
            # Fedora installation script (unchanged)
            wazuh_script = (
                "curl -so wazuh-agent.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.2-1.x86_64.rpm && "
                f"sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' rpm -i ./wazuh-agent.rpm &&"
                f"sudo systemctl start wazuh-agent"
            )
        else:
            raise ValueError("Unsupported OS type.")

        # Execute the installation script
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
            try:
                # Extract necessary data from the request
                ip_address = request.data.get('ip_address')
                ssh_username = request.data.get('ssh_username')
                private_key = request.data.get('private_key')
                os_type = request.data.get('os_type')

                # Prepare the server dictionary
                server = {
                    'ip_address': ip_address,
                    'ssh_username': ssh_username,
                    'private_key': private_key,
                    'os_type': os_type,
                }

                success, output = install_wazuh_agent(server)

                if success:
                    return Response({'success': success, 'output': output})
                else:
                    return Response({'success': success, 'error': output}, status=400)
            except Exception as e:
                return Response({'success': False, 'error': str(e)}, status=500)
        return Response({'error': 'Invalid request method'}, status=405)       


# class OnboardViewSet(viewsets.ModelViewSet):
#     @action(detail=False, methods=['post'])
#     def onboard_server(self, request):
#         if request.method == 'POST':
#             try:
#                 # Extract necessary data from the request
#                 ip_address = request.data.get('ip_address')
#                 ssh_username = request.data.get('ssh_username')
#                 private_key = request.data.get('private_key')
#                 os_type = request.data.get('os_type')

#                 # Prepare the server dictionary
#                 server = {
#                     'ip_address': ip_address,
#                     'ssh_username': ssh_username,
#                     'private_key': private_key,
#                     'os_type': os_type,
#                 }

#                 success, output = install_wazuh_agent(server)

#                 if success:
#                     return Response({'success': success, 'output': output})
#                 else:
#                     return Response({'success': success, 'error': output}, status=400)
#             except Exception as e:
#                 return Response({'success': False, 'error': str(e)}, status=500)
#         return Response({'error': 'Invalid request method'}, status=405)
 
 
 
############################### Onboarding Windows Machine #############
 
 
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
                'Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.5.4-1.msi -OutFile wazuh-agent.msi; msiexec.exe /i wazuh-agent.msi /q WAZUH_MANAGER=\'172.16.1.61\' WAZUH_REGISTRATION_SERVER=\'172.16.1.61\';  '
            )
            start_service = (
                'NET START Wazuh '
            )
 
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
            print("hiii new window")
 
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
 