<template>
  <div style="" class="bg-blue-100 overflow-x-hidden lg:overflow-x-auto lg:overflow-hidden flex items-center justify-center lg:h-screen">
    <!-- remove flex classes from body tag to remove the horizontal and vertical position -->
 
    <div class="login-container container w-full lg:w-4/5 lg:bg-white h-screen lg:h-screen-75 lg:border border-gray-300 rounded-lg flex flex-wrap lg:flex-nowrap flex-col lg:flex-row justify-between group">
 
      <!-- product Side -->
      <div class="w-full bg-blue-400  lg:w-1/2 h-28 lg:h-full mt-32 lg:mt-0 lg:bg-theme-yellow-dark flex relative order-2 lg:order-1">
 
        <div class="text-center hidden lg:flex items-center justify-start h-full w-full select-none">
          <!-- <span class="transform block whitespace-nowrap h-full -rotate-90 text-[55px] 2xl:text-[70px] font-black uppercase text-yellow-300 opacity-0 transition-all group-hover:opacity-100 ml-10 2xl:ml-12 group-hover:-ml-20 2xl:group-hover:ml-26 lg:group-hover:ml-20 duration-1000 lg:duration-700 ease-in-out">Defense Utility for Risk Governance and Awareness</span> -->
        </div>
        <!-- product text -->
 
        <!-- <div class="product absolute right-0 bottom-0 flex items-center lg:justify-center w-full opacity-50 lg:opacity-100">
         <img src="../assets/static/u.png" alt="product" class="-mb-5 lg:mb-0 -ml-12 lg:ml-0 product h-[500px] xl:h-[700px] 2xl:h-[900px] w-auto object-cover ">
        
        </div> -->
        <div class="product absolute right-0 flex bottom-[250px]  mr-[95px]  items-center lg:justify-center w-full opacity-50 lg:opacity-100">
  <img src="../assets/static/rl.png" alt="product" class="mx-auto mb-8 lg:mb-0 ml-4 lg:ml-auto mt-8 lg:mt-0 h-[300px] xl:h-[400px] 2xl:h-[500px] w-auto object-cover">
</div>

 
        <div class="hidden lg:block w-1/3 bg-white ml-auto"></div>
      </div>
      <!-- Product Side End-->
 
      <!-- Login Form -->
      <div class="w-full lg:w-1/2 order-1 lg:order-2">
        <div class="form-wrapper flex items-center lg:h-full px-10 relative z-10 pt-16 lg:pt-0">
          <div class="w-full space-y-5">
 
            <div class="form-caption flex items-end justify-center text-center space-x-3 mb-20">
              <img class="w-10 h-10 mr-2" src="../assets/static/DURGA.png" alt="logo">
              <span class="text-3xl font-semibold text-gray-700">DURGA</span>
              
            </div>
            <!-- form caption -->
 
            <div class="form-element">
              <label class="space-y-2 w-full lg:w-4/5 block mx-auto">
                <span class="block text-lg text-gray-800 tracking-wide">Username</span>
                <span class="block">
                  <input v-model="username" type="text" class="bg-yellow-100 lg:bg-white border lg:border-2 border-gray-400 lg:border-gray-200 w-full p-3 focus:outline-none active:outline-none focus:border-gray-400 active:border-gray-400">
                </span>
              </label>
            </div>
            <!-- form element -->
 
            <div class="form-element">
              <label class="space-y-2 w-full lg:w-4/5 block mx-auto">
                <span class="block text-lg text-gray-800 tracking-wide">Password</span>
                <span class="block">
                  <input v-model="password" type="password" @keyup.enter=" login" class="bg-yellow-100 lg:bg-white border lg:border-2 border-gray-400 lg:border-gray-200 w-full p-3 focus:outline-none active:outline-none focus:border-gray-400 active:border-gray-400">
                </span>
              </label>
            </div>
 
            <!-- form element -->
            <div class="form-element">
            <span class="w-full lg:w-4/5 block mx-auto ">
              <button @click="login"  class="cursor-pointer border-2 rounded-md border-blue-200 w-full p-3 bg-blue-500 focus:outline-none active:outline-none focus:bg-theme-yellow active:bg-theme-yellow hover:bg-theme-yellow transition-all">
            Login </button>
            </span>
          </div>
            <!-- form element -->
 
          </div>
        </div>
        <!-- form wrapper -->
      </div>
    </div>
  </div>
</template>
 
<script>
import axios from 'axios';
import { API_ENDPOINT } from '@/../apiconfig.js';

export default {
  data() {
    return {
      username: '',
      password: '',
      rememberMe: false,
      success: null,
      userdata: [],
      apiUrl: API_ENDPOINT,  
      };
  },

 

  methods: {
    login() {
      const formData = {
        username: this.username,
        password: this.password,
      };

      axios
        .post(`${this.apiUrl}/api/v1/login/`, formData) 
        // ${this.apiUrl}/api/v1/login/
        .then((response) => {
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
</style>