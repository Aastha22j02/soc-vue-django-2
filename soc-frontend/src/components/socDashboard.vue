<template>
    <div class="p-4 w-full">
        <div class="   rounded-lg dark:border-gray-700 mt-20" >   
           <div class="flex items-center justify-center h-auto  rounded bg-gray-50 dark:bg-gray-800">
                  
 <iframe sandbox="allow-same-origin allow-scripts allow-popups
  allow-forms"
                    width="1000"
                    height="1000"
                    :src="embedUrl"
                    frameborder="0"
                    allowfullscreen class="m-5"
                ></iframe>
           </div>
        
        </div>
     </div>
    <div>
   
    </div>
    </template>
    

     
    
    <script>
    import leftSidebar from '@/components/leftSidebar.vue'


    export default {
    components:{
      leftSidebar,
    },
      computed: {
        embedUrl() {
          return `https://172.16.1.67/app/wazuh#/overview/`;
        },
      },
    };
    </script>
    
     
    
  