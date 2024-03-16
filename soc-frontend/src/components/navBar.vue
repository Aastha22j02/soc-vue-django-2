<template>
  
  <nav class="Navbar fixed top-0 z-50 w-full bg-gradient-to-r from-blue-800  to-blue-300 border-b border-gray-200
   dark:bg-gray-800 dark:border-gray-700">
    <div class="px-3 py-3 lg:px-5 lg:pl-3">
      <div class="flex items-center justify-between">

        <div class="flex items-center justify-start">

          <!-- Hamburger sign commented -->
          <!-- <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar"
            type="button"
            class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
            <span class="sr-only">Open sidebar</span>
            <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg">
              <path clip-rule="evenodd" fill-rule="evenodd"
                d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z">
              </path>
            </svg>
          </button> -->

          <p class="flex  md:mr-24  no-underline ">
            <img src="@/assets/static/DURGA.png" class="mr-1 w-6 h-8 rounded-full" alt="DURGA Logo" />
            <span class="title-name self-center text-white font-bold  text-3xl name">
              DURGA
              <span class=" text-white text-base font-bold name "> (Defense Utility for Risk Governance and Awareness)
              </span>
            </span>
          </p>
        </div>
        <div class="flex items-center">
          <div class=" flex items-center ml-3">
            <div class="flex">
              <!-- <button v-if="isDark ===false" @click="toggleDarkMode" id="theme-toggle" type="button" class=" mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
                    <svg id="theme-toggle-dark-icon" class=" w-8 h-8" 
                    ="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
                </button> 
                <button v-else @click="toggleDarkMode" id="theme-toggle" type="button" class="mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
                    <svg id="theme-toggle-light-icon" class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>      
                </button>  -->


                <button @click="toggleUser"
                class="flex  items-center justify-center text-purple-600 h-8 w-8 text-lg bg-white rounded-full">
                {{ getFirstLetter(Username) }}
              </button>

            </div>

            <div :class="{ 'hidden': !UserToggle }" class="fixed top-8 right-[0.5px]
              z-50  my-4 text-base list-none bg-white divide-y divide-gray-100 
              rounded shadow dark:bg-gray-700 dark:divide-gray-600">
              <div class="px-4 py-3" role="none">
                <p class="text-sm text-gray-900 dark:text-white" role="none">
                  {{ Username }}
                </p>
                <p class="text-sm font-medium text-gray-900 truncate dark:text-gray-300" role="none">
                  {{ Username }}.soc@os3.com
                </p>
              </div>
              <ul class="py-1" role="none">
                <!-- <li>
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Dashboard</a>
                  </li>
                  <li>
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Settings</a>
                  </li>
                  <li>
                    <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Billing</a>
                  </li> -->
                <li>
                  <a @click.prevent="logout" href="#"
                    class="no-underline  block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white"
                    role="menuitem">Sign out</a>
                </li>
              </ul>
            </div>

          </div>
        </div>
      </div>
    </div>
  </nav>


</template>

<script >
export default {
  data() {
    

    return {
      

       UserToggle: false,
       Username: '',

    };
  },
  created() {
    this.Username = sessionStorage.getItem('username');
  },




  methods: {
    
    toggleUser(){
   
      this.UserToggle = !this.UserToggle;
    },
    

    logout(){
     
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      window.location.reload()
    },

    getFirstLetter(username) {
      return username.charAt(0, 1).toUpperCase();
    },

  },

};




</script>

<style lang="scss" scoped>

</style>