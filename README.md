<template>
  <!-- ... (unchanged code) -->

  <div class="grid gap-6 mb-6 md:grid-cols-2">
    <div>
      <label for="private_key" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
        Private Key       </label>
      <textarea
        id="private_key"
        v-model="private_key"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 h-24 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="-----BEGIN RSA PRIVATE KEY-----
  ...
  -----END RSA PRIVATE KEY-----"
        required
      ></textarea>
      <div v-if="errors.private_key" class="text-red-500 text-sm mt-1">
        {{ errors.private_key }}
      </div>
    </div>
  </div>

  <!-- ... (unchanged code) -->

  <button @click.prevent="onBoard" class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-teal-300 to-lime-300 group-hover:from-teal-300 group-hover:to-lime-300 dark:text-white dark:hover:text-gray-900 focus:ring-4 focus:outline-none focus:ring-lime-200 dark:focus:ring-lime-800">
    <span class="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
      OnBoard Server
    </span>
  </button>

  <!-- ... (unchanged code) -->
</template>

<script>
import axios from 'axios';
import leftSidebar from './leftSidebar.vue';

export default {
  components: {
    leftSidebar,
  },
  data() {
    return {
      errors: {},
      loading: false,
      successMessage: '',
      errorMessage: '',
      server_ip: '',
      server_username: '',
      private_key: '',  // Add private_key to the data
      server_type: '',
    };
  },
  methods: {
    onBoard() {
      // ... (unchanged code)

      const fromData = {
        ip_address: this.server_ip,
        ssh_username: this.server_username,
        private_key: this.private_key,  // Add private_key to the request data
        os_type: this.server_type,
      };

      this.loading = true;

      axios
        .post('http://127.0.0.1:8000/api/v3/onboard/', fromData)
        .then((response) => {
          // ... (unchanged code)
        })
        .catch((error) => {
          // ... (unchanged code)
        });
    },

    // ... (unchanged code)
  },
};
</script>

<style scoped>
/* ... (unchanged code) */
</style>






api


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from paramiko import SSHClient, AutoAddPolicy, SSHException, RSAKey
import io

def install_wazuh_agent(server):
    ip_address = server['ip_address']
    ssh_username = server['ssh_username']
    private_key_str = server['private_key']  # Private key as a string
    os_type = server['os_type']

    try:
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())

        # Load the private key from the string
        private_key = RSAKey(file_obj=io.StringIO(private_key_str))

        ssh_client.connect(
            ip_address,
            username=ssh_username,
            pkey=private_key,  # Use private key for authentication
        )

        # ... (unchanged code for different OS types)

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
    @action(detail=False, methods=['post'])
    def onboard_server(self, request):
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
