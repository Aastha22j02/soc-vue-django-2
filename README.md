<div>
              <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
              <input type="username" v-model="username" @keyup.enter="login" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="username" required="">
            </div>
            <div>
              <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
              <input type="password" v-model="password" @keyup.enter="login" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="">
            </div>
            <div class="flex items-center justify-between">
              <a href="#" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">Forgot password?</a>
            </div>
            <button type="button" @click="login" class="w-full text-white bg-purple-600 hover:bg-purple-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Login</button>
          </div>


##

<template>
  <div class="container">
    <div class="screen">
      <div class="screen__content">
        <form class="login">
          <div class="login__field">
            <i class="login__icon fas fa-user"></i>
            <input v-model="username" type="text" class="login__input" placeholder="User name / Email">
          </div>
          <div class="login__field">
            <i class="login__icon fas fa-lock"></i>
            <input v-model="password" type="password" class="login__input" placeholder="Password">
          </div>
          <button @click="login" class="button login__submit">
            <span class="button__text">Log In Now</span>
            <i class="button__icon fas fa-chevron-right"></i>
          </button>
        </form>
        <div class="social-login">
          <h3>log in via</h3>
          <div class="social-icons">
            <a href="#" class="social-login__icon fab fa-instagram"></a>
            <a href="#" class="social-login__icon fab fa-facebook"></a>
            <a href="#" class="social-login__icon fab fa-twitter"></a>
          </div>
        </div>
      </div>
      <div class="screen__background">
        <span class="screen__background__shape screen__background__shape4"></span>
        <span class="screen__background__shape screen__background__shape3"></span>
        <span class="screen__background__shape screen__background__shape2"></span>
        <span class="screen__background__shape screen__background__shape1"></span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      success: null,
      userdata: [],
    };
  },
  methods: {
    login() {
      const formData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post('http://172.16.1.56:8000/api/v1/login/', formData)
        .then((response) => {
          console.log(response.data);

          this.success = 'Successfully Logged In!';

          const token = response.data.token;
          this.userdata = response.data.user_data;
          const user_id = this.userdata.id;
          const username = this.userdata.username;

          sessionStorage.setItem('user_id', user_id);
          sessionStorage.setItem('username', username);

          this.$router.push('/home');
        })
        .catch((error) => {
          console.error(error.response.data.message);
          // Handle login error
        });
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
/* ... Paste the CSS styles provided in the question ... */
@import url('https://fonts.googleapis.com/css?family=Raleway:400,700');

* {
	box-sizing: border-box;
	margin: 0;
	padding: 0;	
	font-family: Raleway, sans-serif;
}

body {
	background: linear-gradient(90deg, #C7C5F4, #776BCC);		
}

.container {
	display: flex;
	align-items: center;
	justify-content: center;
	min-height: 100vh;
}

.screen {		
	background: linear-gradient(90deg, #5D54A4, #7C78B8);		
	position: relative;	
	height: 600px;
	width: 360px;	
	box-shadow: 0px 0px 24px #5C5696;
}

.screen__content {
	z-index: 1;
	position: relative;	
	height: 100%;
}

.screen__background {		
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	z-index: 0;
	-webkit-clip-path: inset(0 0 0 0);
	clip-path: inset(0 0 0 0);	
}

.screen__background__shape {
	transform: rotate(45deg);
	position: absolute;
}

.screen__background__shape1 {
	height: 520px;
	width: 520px;
	background: #FFF;	
	top: -50px;
	right: 120px;	
	border-radius: 0 72px 0 0;
}

.screen__background__shape2 {
	height: 220px;
	width: 220px;
	background: #6C63AC;	
	top: -172px;
	right: 0;	
	border-radius: 32px;
}

.screen__background__shape3 {
	height: 540px;
	width: 190px;
	background: linear-gradient(270deg, #5D54A4, #6A679E);
	top: -24px;
	right: 0;	
	border-radius: 32px;
}

.screen__background__shape4 {
	height: 400px;
	width: 200px;
	background: #7E7BB9;	
	top: 420px;
	right: 50px;	
	border-radius: 60px;
}

.login {
	width: 320px;
	padding: 30px;
	padding-top: 156px;
}

.login__field {
	padding: 20px 0px;	
	position: relative;	
}

.login__icon {
	position: absolute;
	top: 30px;
	color: #7875B5;
}

.login__input {
	border: none;
	border-bottom: 2px solid #D1D1D4;
	background: none;
	padding: 10px;
	padding-left: 24px;
	font-weight: 700;
	width: 75%;
	transition: .2s;
}

.login__input:active,
.login__input:focus,
.login__input:hover {
	outline: none;
	border-bottom-color: #6A679E;
}

.login__submit {
	background: #6A679E;
	font-size: 14px;
	margin-top: 30px;
	padding: 16px 20px;
	border-radius: 26px;
	border: 1px solid #D4D3E8;
	text-transform: uppercase;
	font-weight: 700;
	display: flex;
	align-items: center;
	width: 100%;
	color: #4C489D;
	box-shadow: 0px 2px 2px #5C5696;
	cursor: pointer;
	transition: .2s;
}

.login__submit:active,
.login__submit:focus,
.login__submit:hover {
	border-color: #6A679E;
	outline: none;
}

.button__icon {
	font-size: 24px;
	margin-left: auto;
	color: #7875B5;
}

.social-login {	
	position: absolute;
	height: 140px;
	width: 160px;
	text-align: center;
	bottom: 0px;
	right: 0px;
	color: #fff;
}

.social-icons {
	display: flex;
	align-items: center;
	justify-content: center;
}

.social-login__icon {
	padding: 20px 10px;
	color: #fff;
	text-decoration: none;	
	text-shadow: 0px 0px 8px #7875B5;
}

.social-login__icon:hover {
	transform: scale(1.5);	
}
</style>

###1

<body class="bg-yellow-100 overflow-x-hidden lg:overflow-x-auto lg:overflow-hidden flex items-center justify-center lg:h-screen">
  <!-- remove flex classes from body tag to remove the horizontal and vertical position -->

  <div class="login-container container w-full lg:w-4/5 lg:bg-white h-screen lg:h-screen-75 lg:border border-gray-300 rounded-lg flex flex-wrap lg:flex-nowrap flex-col lg:flex-row justify-between group">

    <!-- product Side -->
    <div class="w-full lg:w-1/2 h-28 lg:h-full mt-32 lg:mt-0 lg:bg-theme-yellow-dark flex relative order-2 lg:order-1">

      <div class="text-center hidden lg:flex items-center justify-start h-full w-full select-none">

        <span class="transform block whitespace-nowrap h-full -rotate-90 text-[55px] 2xl:text-[70px] font-black uppercase text-yellow-300 opacity-0 transition-all group-hover:opacity-100 ml-10 2xl:ml-12 group-hover:-ml-20 2xl:group-hover:ml-26 lg:group-hover:ml-20 duration-1000 lg:duration-700 ease-in-out">Learn With Aamir</span>

      </div>
      <!-- product text -->

      <div class="product absolute right-0 bottom-0 flex items-center lg:justify-center w-full opacity-50 lg:opacity-100">

        <img src="./images/1.png" alt="product" class="-mb-5 lg:mb-0 -ml-12 lg:ml-0 product h-[500px] xl:h-[700px] 2xl:h-[900px] w-auto object-cover transform group-hover:translate-x-26 2xl:group-hover:translate-x-48 transition-all duration-1000 lg:duration-700 ease-in-out">
        <!-- product image -->

        <div class="shadow w-full h-5 bg-black bg-opacity-25 filter blur absolute bottom-0 lg:bottom-14 left-0 lg:left-24 rounded-full transform skew-x-10"></div>
        <!-- product shadow -->
      </div>

      <div class="hidden lg:block w-1/3 bg-white ml-auto"></div>

    </div>
    <!-- Product Side End-->

    <!-- Login Form -->
    <div class="w-full lg:w-1/2 order-1 lg:order-2">
      <div class="form-wrapper flex items-center lg:h-full px-10 relative z-10 pt-16 lg:pt-0">
        <div class="w-full space-y-5">

          <div class="form-caption flex items-end justify-center text-center space-x-3 mb-20">
            <span class="text-3xl font-semibold text-gray-700">Login</span>
            <span class="text-base text-gray-800">Form</span>
          </div>
          <!-- form caption -->

          <div class="form-element">
            <label class="space-y-2 w-full lg:w-4/5 block mx-auto">
              <span class="block text-lg text-gray-800 tracking-wide">Email</span>
              <span class="block">
                <input type="text" class="bg-yellow-100 lg:bg-white border lg:border-2 border-gray-400 lg:border-gray-200 w-full p-3 focus:outline-none active:outline-none focus:border-gray-400 active:border-gray-400">
              </span>
            </label>
          </div>
          <!-- form element -->


          <div class="form-element">
            <label class="space-y-2 w-full lg:w-4/5 block mx-auto">
              <span class="block text-lg text-gray-800 tracking-wide">Password</span>
              <span class="block">
                <input type="password" class="bg-yellow-100 lg:bg-white border lg:border-2 border-gray-400 lg:border-gray-200 w-full p-3 focus:outline-none active:outline-none focus:border-gray-400 active:border-gray-400">
              </span>
            </label>
          </div>
          <!-- form element -->

          <div class="form-element">
            <div class="w-full lg:w-4/5 block mx-auto flex items-center justify-between">
              <label class="block text-gray-800 tracking-wide flex items-center space-x-2 select-none">
                <input type="checkbox" name="" id="">
                <span class="block text-gray-800 tracking-wide">Remember me</span>
              </label>
              <a href="#" class="block text-gray-800 tracking-wide inline-block border-b border-gray-300">Forgot Password?</a>
            </div>
          </div>
          <!-- form element -->

          <div class="form-element">
            <span class="w-full lg:w-4/5 block mx-auto ">
              <input type="submit" class="cursor-pointer border-2 border-yellow-200 w-full p-3 bg-yellow-200 focus:outline-none active:outline-none focus:bg-theme-yellow active:bg-theme-yellow hover:bg-theme-yellow transition-all">
            </span>
          </div>
          <!-- form element -->

        </div>
      </div>
      <!-- form wrapper -->
    </div>
    <!-- Login Form End-->


  </div>

  <script src="./js/script.js"></script>
</body>


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
        .post('http://172.16.1.56:8000/api/v3/onboard/', fromData)
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
