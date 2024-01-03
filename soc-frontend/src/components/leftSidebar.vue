

<template>
<nav class="Navbar fixed top-0 z-50 w-full 
bg-gradient-to-r from-green-500 via-purple-500 to-pink-500 border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
  <div class="px-3 py-3 lg:px-5 lg:pl-3">
    <div style="max-height: 33px;" class="flex items-center justify-between">
        <button @click="toggleSidebar">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            style="fill: white; transform: ; msfilter: "
          >
            <path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h16v2H4z"></path>
            LOGO
          </svg>
        </button>
      <div class="flex items-center justify-start">        
        <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar" type="button" class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
            <span class="sr-only">Open sidebar</span>
            <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
               <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
            </svg>
         </button>
          <p class="flex  md:mr-24 ml-20 no-underline ">
            <img src="@/assets/static/DURGA.png" 
            class="mr-1 w-6 h-8 rounded-full" alt="DURGA Logo" />
            <span class="title-name self-center text-black font-bold  text-3xl name">
            DURGA         
            <span class=" text-black text-base font-bold name "> Defense Utility for Risk Governance and Awareness </span>
            </span>           
          </p>       
      </div>
      <div class="flex items-center">
          <div class=" flex items-center ml-3" >
            <div class="flex">
               <!-- <button v-if="isDark ===false" @click="toggleDarkMode" id="theme-toggle" type="button" class=" mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
                  <svg id="theme-toggle-dark-icon" class=" w-8 h-8" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path></svg>
              </button> 
              <button v-else @click="toggleDarkMode" id="theme-toggle" type="button" class="mr-5 flex text-gray-500  hover:bg-gray-300 dark:hover:bg-gray-700 rounded-lg text-sm p-2.5">
                  <svg id="theme-toggle-light-icon" class="w-8 h-8" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" fill-rule="evenodd" clip-rule="evenodd"></path></svg>      
              </button>  -->
             
              
              <button @click="userToggle" type="button" class="flex text-sm mt-3 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" aria-expanded="false" data-dropdown-toggle="dropdown-user">
                <span class="sr-only">Open user menu</span>
                <img class="w-8 h-8 rounded-full" src="@/assets/static/admin.jpeg" alt="user photo">
              </button>
            </div>

            <div :class="{ 'hidden' : !UserToggle }" class="fixed top-8 right-[0.5px]
            z-50  my-4 text-base list-none bg-white divide-y divide-gray-100 
            rounded shadow dark:bg-gray-700 dark:divide-gray-600" >
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
                  <a @click.prevent="logout" href="#" class="no-underline  block px-4 py-2 text-sm text-gray-700 hover:bg-gray-300 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Sign out</a>
                </li>
              </ul>
            </div>

          </div>
        </div>
    </div>
  </div>
</nav>

<aside id="logo-sidebar"
:class="{ hidden: !isSidebarOpen }" class="relative top-0 left-0 z-40 w-64 h-screen pt-20
 transition-transform -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0
  dark:bg-gray-800 dark:border-gray-700 bg-gradient-to-b from-green-500 via-purple-500 to-pink-500" aria-label="Sidebar">
   <div class="h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800
    bg-gradient-to-b from-green-500 to-purple-500 ">
      <ul class="space-y-2 font-medium">
        
         <li>
          <router-link to="/home"
           :class="{ 'bg-black ': currentPage === 'home' }" class="flex items-center p-2   text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 
          bg-purple-200  group">
          <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              style="fill: white; transform: ; msfilter: "
            >
              <path
                d="M12.71 2.29a1 1 0 0 0-1.42 0l-9 9a1 1 0 0 0 0 1.42A1 1 0 0 0 3 13h1v7a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-7h1a1 1 0 0 0 1-1 1 1 0 0 0-.29-.71zM6 20v-9.59l6-6 6 6V20z"
              ></path>
            </svg>
             <span class="flex-1 ml-3 whitespace-nowrap white-black">Home  </span>
             <!-- <span class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-300 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
          </router-link>
       </li>
         <hr>
        

       <li>
        <router-link to="/socdashboard"
         :class="{ 'bg-black ': currentPage === 'socdashboard' }" class="flex items-center p-2   text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 
        bg-purple-200  group">
        <svg
              class="w-5 h-5 text-white transition duration-75 dark:text-gray-100 group-hover:text-gray-900 dark:group-hover:text-white"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 21"
            >
              <path
                d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z"
              />
              <path
                d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"
              />
            </svg>
           <span class="flex-1 ml-3 whitespace-nowrap white-black">SOC Dashboard</span>
           <!-- <span class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-300 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
        </router-link>
     </li>

         <li>
            <router-link to="/onBoard"
             :class="{ 'bg-black ': currentPage === 'onBoard' }" class="flex items-center p-2   text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 
            bg-purple-200  group">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              style="fill: white; transform: ; msfilter: "
            >
              <path
                d="M20 4H4c-1.103 0-2 .897-2 2v10c0 1.103.897 2 2 2h4l-1.8 2.4 1.6 1.2 2.7-3.6h3l2.7 3.6 1.6-1.2L16 18h4c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2zM5 13h4v2H5v-2z"
              ></path>
            </svg>
               <span class="flex-1 ml-3 whitespace-nowrap white-black">System Onbording</span>
               <!-- <span class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-300 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
            </router-link>
         </li>
         <li>
          <router-link to="/rules"
           :class="{ 'bg-black ': currentPage === 'rules' }" class="flex items-center p-2   text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 
          bg-purple-200  group">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                style="fill: white; transform: ; msfilter: "
              >
                <path
                  d="m20 8-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM9 19H7v-9h2v9zm4 0h-2v-6h2v6zm4 0h-2v-3h2v3zM14 9h-1V4l5 5h-4z"
                ></path>
              </svg>
             <span class="flex-1 ml-3 whitespace-nowrap white-black">Rules</span>
             <!-- <span class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-300 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
          </router-link>
       </li>
       
         <!-- <li>
          <button @click="toggleDropdown" type="button"  class="flex items-center w-full p-2 text-base  text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-300 dark:text-white dark:hover:bg-gray-700" aria-controls="dropdown-example" data-collapse-toggle="dropdown-example">              
                <span class="flex-1 ml-3 text-left whitespace-nowrap"> Your Account </span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                   <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                </svg>
          </button>
          <ul id="dropdown-example" :class="{'hidden': !isDropdownOpen}"  class=" py-2 space-y-2">
                <li>
                   <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-300 dark:text-white dark:hover:bg-gray-700">Products</a>
                </li>
                <li>
                   <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-300 dark:text-white dark:hover:bg-gray-700">Billing</a>
                </li>
                <li>
                   <a href="#" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-300 dark:text-white dark:hover:bg-gray-700">Invoice</a>
                </li>
          </ul>
       </li> -->
   <hr>
   <li class="absolute bottom-14">
    <a href="#" :class="{ 'bg-slate-900 ': currentPage === 'overview' }" 
    class="flex items-center p-2 bg-purple-200 text-black  transition duration-75 rounded-lg hover:bg-gray-300
   dark:hover:bg-gray-700 dark:text-white dark:bg-gray-800 group w-[195px] ">
      <svg
        class="flex-shrink-0 w-6 h-6 text-white transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
        aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
        <path
          d="M16 14V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 0 0 0-2h-1v-2a2 2 0 0 0 2-2ZM4 2h2v12H4V2Zm8 16H3a1 1 0 0 1 0-2h9v2Z" />
      </svg>
      <span class="ml-3">Documentation</span>
    </a>
  </li>
  <li class="absolute bottom-2">
    <a href="#" class="flex items-center p-2 cursor-not-allowed  bg-purple-200 text-black  transition duration-75 rounded-lg
   hover:bg-gray-300 dark:hover:bg-gray-700 dark:text-white dark:bg-gray-800 group w-[195px] ">
      <svg
        class="flex-shrink-0 w-6 h-6 text-white transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
        aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 21 21">
        <path
          d="m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z" />
      </svg>
      <span class="ml-3">Help</span>
    </a>
  </li>
     </ul>
   </div>
</aside>

<aside
    id="logo-sidebar-close"
    :class="{ hidden: isSidebarOpen }"
        class="relative top-0 left-0 z-40 w-16 h-screen pt-20
    transition-transform -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0
      dark:bg-gray-800 dark:border-gray-700 bg-gradient-to-b from-green-500 via-purple-500 to-pink-500"
        aria-label="Sidebar"
  >
    <div class="h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800
    bg-gradient-to-b from-green-500 to-purple-500 ">
      <ul class="space-y-2 font-medium">
        <li>
          <router-link
            to="/home"
            :class="{ 'bg-slate-900 ': currentPage === 'home' }"
            class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              style="fill: white; transform: ; msfilter: "
            >
              <path
                d="M12.71 2.29a1 1 0 0 0-1.42 0l-9 9a1 1 0 0 0 0 1.42A1 1 0 0 0 3 13h1v7a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-7h1a1 1 0 0 0 1-1 1 1 0 0 0-.29-.71zM6 20v-9.59l6-6 6 6V20z"
              ></path>
            </svg>
            
          </router-link>
        </li>
        <hr />
        <li>
          <router-link
            to="socdashboard"
            :class="{ 'bg-slate-900 ': currentPage === 'socdashboard' }"
            class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group"
          >
            <svg
              class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-100 group-hover:text-gray-900 dark:group-hover:text-white"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 22 21"
            >
              <path
                d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z"
              />
              <path
                d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"
              />
            </svg>
          
          </router-link>
        </li>

        <li>
          <router-link
            to="/onBoard"
            :class="{ 'bg-slate-900 ': currentPage === 'onBoard' }"
            class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              style="fill: white; transform: ; msfilter: "
            >
              <path
                d="M20 4H4c-1.103 0-2 .897-2 2v10c0 1.103.897 2 2 2h4l-1.8 2.4 1.6 1.2 2.7-3.6h3l2.7 3.6 1.6-1.2L16 18h4c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2zM5 13h4v2H5v-2z"
              ></path>
            </svg>
            
            <!-- <span class="inline-flex items-center justify-center px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-300 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
          </router-link>
        </li>
        <li>
          <router-link
            to="/rules"
            :class="{ 'bg-slate-900 ': currentPage === 'rules' }"
            class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-300 dark:hover:bg-gray-700 group"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              style="fill: rgb(234, 228, 228); transform: ; msfilter: "
            >
              <path
                d="m20 8-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM9 19H7v-9h2v9zm4 0h-2v-6h2v6zm4 0h-2v-3h2v3zM14 9h-1V4l5 5h-4z"
              ></path>
            </svg>
          
          </router-link>
        </li>

        <hr />
       
   <li class="absolute bottom-14">
    <a href="#" :class="{ 'bg-slate-900 ': currentPage === 'overview' }" 
    class="flex items-center p-2 bg-purple-200 text-black  transition duration-75 rounded-lg hover:bg-gray-300
   dark:hover:bg-gray-700 dark:text-white  group  ">
      <svg
        class="flex-shrink-0 w-6 h-6 text-white transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
        aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
        <path
          d="M16 14V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 0 0 0-2h-1v-2a2 2 0 0 0 2-2ZM4 2h2v12H4V2Zm8 16H3a1 1 0 0 1 0-2h9v2Z" />
      </svg>
      <!-- <span class="ml-3">Documentation</span> -->
    </a>
  </li>
  <li class="absolute bottom-2">
    <a href="#" class="flex items-center p-2 cursor-not-allowed  bg-purple-200 text-black  transition duration-75 rounded-lg
   hover:bg-gray-300 dark:hover:bg-gray-700 dark:text-white  group">
      <svg
        class="flex-shrink-0 w-6 h-6 text-white transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
        aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 21 21">
        <path
          d="m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z" />
      </svg>
      <!-- <span class="ml-3">Help</span> -->
    </a>
  </li>
        
      </ul>
    </div>
  </aside>

</template>


<script>
import { useDark, useToggle } from "@vueuse/core";

export default {
  data() {
    const isDark = useDark();
    const toggleDark = useToggle(isDark);

    return {
      isDark,
      toggleDark,

       isDropdownOpen: false,
       isSidebarOpen: false,
       UserToggle: false,
        Username : ''

    };
  },
  created(){
    this.Username = sessionStorage.getItem('username')
  }
  ,
  computed: {
    currentPage() {
     
      return this.$route.name;
    },
  },
  methods: {
    toggleDarkMode() {
      this.toggleDark();
    },
    socdashboard(){
   
      this.$router.push('/socdashboard');
    },
    toggleDropdown(){
     
      this.isDropdownOpen = !this.isDropdownOpen
    },
    userToggle(){
   
      this.UserToggle = !this.UserToggle;
    },
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },

    logout(){
      console.log("logout");
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      window.location.reload()
    },
  },

};
</script>


<style scoped>

</style>