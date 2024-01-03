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


class RuleListByCategory(generics.ListAPIView):
    serializer_class = RuleSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Rule.objects.filter(category__name=category_name)

class RuleList(generics.ListAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from paramiko import SSHClient, AutoAddPolicy, SSHException
# from .models import Server
# from .serializers import ServerSerializer


def install_wazuh_agent(server):
    ip_address = server['ip_address']
    ssh_username = server['ssh_username']
    ssh_password = server['ssh_password']
    os_type = server['os_type']
   
    try:  
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())

        print(ip_address)
        # Connect to the remote server
        ssh_client.connect(
            ip_address,
            username=ssh_username,
            password=ssh_password,
        )

        print(os_type)
        # Define the Wazuh agent installation script based on the server's OS type
        if os_type == 'Ubuntu':          
            wazuh_script = (
                "curl -so wazuh-agent.deb https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.5.2-1_amd64.deb && "
                # f"sudo dpkg -i ./wazuh-agent.deb && "
                f"sudo WAZUH_MANAGER='172.16.1.64' WAZUH_AGENT_GROUP='default' dpkg -i ./wazuh-agent.deb &&"
                f"sudo systemctl start wazuh-agent"  )
           
        elif os_type == 'CentOS':
            wazuh_script = (
                "curl -so wazuh-agent.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.2-1.x86_64.rpm && "              
                f"sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' rpm -i ./wazuh-agent.rpm &&"
                f"sudo systemctl start wazuh-agent"    )
                
        elif os_type == 'Redhat':
            wazuh_script = (
                "sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' &&"
                f"yum install -y https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.4-1.x86_64.rpm"              
                f"sudo systemctl start wazuh-agent "
            )
        elif os_type == 'Fedora':
            wazuh_script = (
                "curl -so wazuh-agent.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.5.2-1.x86_64.rpm && "              
                f"sudo WAZUH_MANAGER='172.16.1.61' WAZUH_AGENT_GROUP='default' rpm -i ./wazuh-agent.rpm &&"
                f"sudo systemctl start wazuh-agent "
            )

        elif os_type == 'Windows':
            wazuh_script = (
                f"Invoke-WebRequest -Uri 'https://packages.wazuh.com/4.x/windows/wazuh-agent-4.5.2-1.msi' -OutFile 'wazuh-agent.msi'; "
                f"Start-Process msiexec.exe -ArgumentList '/i', 'wazuh-agent.msi', '/qn', '/quiet', '/norestart', 'WAZUH_MANAGER='172.16.1.61', 'WAZUH_AGENT_GROUP=default' -Wait &&"
                f"NET START Wazuh")
            
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
            server = request.data

            try:
                success, output = install_wazuh_agent(server)
                if success:
                    return Response({'success': success, 'output': output})
                else:
                    return Response({'success': success, 'error': output}, status=400)
            except Exception as e:
                return Response({'success': False, 'error': str(e)}, status=500)    
        return Response({'Methods': Notpost})          