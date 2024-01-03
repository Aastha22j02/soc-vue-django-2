<template>
  <section class="bg-gradient-to-r from-green-500 via-purple-500 to-pink-500 dark:bg-gray-900">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
            <img class="w-8 h-8 mr-2" src="../assets/static/DURGA.png" alt="logo">
          DURGA    
        </a>
        <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                    Sign in to your account
                </h1>
                <div class="space-y-4 md:space-y-6" action="#">
                    <div>
                        <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
                        <input type="username" v-model="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="username" required="">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                        <input type="password"  v-model="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="">
                    </div>
                    <div class="flex items-center justify-between">                  
                        <a href="#" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">Forgot password?</a>
                    </div>
                    <button type="submit" @click="login" 
                    class="w-full text-white bg-purple-600 hover:bg-purple-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Login</button>                   
                  </div>
            </div>
        </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'


export default {
 
  data() {
    return {
      tab: 'login',
      email: null,
      username: null,
      password: null,
      success: null,
      userdata: [],
     
    }

  },
  // computed:{
  //   ...mapWritableState(userModelstore, ['user_id'])
  // },

  methods: {
    login() {
      const formData = {
        username: this.username,
        password: this.password
      }
      axios
        .post('http://127.0.0.1:8000/api/v1/login/', formData)
        .then((response) => {
          console.log(response.data)

          this.success = 'Successfull LoggedIn!'

          const token = response.data.token
          // console.log(token)

          this.userdata = response.data.user_data
          // console.log(this.userdata)
          const user_id = this.userdata.id
          const username = this.userdata.username

          // localStorage.setItem('token',token );
          sessionStorage.setItem('user_id',user_id );
          sessionStorage.setItem('username',username );

          
          // this.setAuthToken(token);
          this.$router.push('/home')

        })
        .catch((error) => {
          console.error(error.response.data.message)
          // Handle login error
        })
    },
  
  }
}
</script>