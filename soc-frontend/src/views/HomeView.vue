<template>
   <navBar />
   <div class="flex fixed mt-16">
      <!-- leftsider bar -->
      <leftSidebar />

      <!-- center panel -->
      <div :class="['h-screen pb-5 flex-1 flex flex-col overflow-hidden', isOpen ? 'w-[1625px]' : 'w-[1830px]']">           
         <div class="flex-1 overflow-x-hidden overflow-y-auto p-7">
            <div class="bg-gray-100 rounded-md">
               <div class=" main_content p-4 w-full h-[100vh]">
                  <div class="container  flex flex-wrap flex-col md:flex-row items-center">
                     <!--Left Col-->
                     <div class="flex flex-col w-full md:w-2/5 justify-center items-start text-center
             md:text-left">
                        <!-- <p class="uppercase tracking-loose w-full text-white">What business we are?</p> -->
                        <h1 style="font-size: 30px; " class="font-bold  animate__animated animate__bounceInDown"> Welcome
                           to the DURGA Operations Dashboard !!</h1>

                        <p class="leading-normal text-2xl mb-8 mt-2 text-black ">
                           Experience unparalleled protection and resilience with Durga, your ultimate security companion.
                        </p>

                     </div>
                     <!--Right Col-->
                     <div class="w-full md:w-3/5 py-6 text-center ">
                        <img class="w-full md:w-4/5 z-50" src="@/assets/static/security3.png " />
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>
 
<script>
import 'animate.css'
import leftSidebar from '@/components/leftSidebar.vue';
import navBar from '@/components/navBar.vue';

import { useSidebarStore } from '@/stores/sidebar';


export default {
   components: {
      leftSidebar,navBar

   },
   data() {
      return {
         Username: '',
      };
   },
   computed: {
      isOpen() {
            return useSidebarStore().open;
        },
   },
   created() {
      this.Username = sessionStorage.getItem("username");
   },
}

</script>
<style scoped>
.main_content {
   background: linear-gradient(90deg, #eeecee 0%, #8167c9 100%);
   border-radius: 99% 1% 89% 11% / 21% 52% 48% 79% ;

}
</style>
 
 