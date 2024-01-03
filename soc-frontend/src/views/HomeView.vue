<template>

   <div class="pt-24  main_content w-full h-[100vh]">
      <div class="container px-3 mx-auto flex flex-wrap flex-col md:flex-row items-center">
         <!--Left Col-->
         <div :class="{ 'zoom-in': zoomIn }"
            class="flex flex-col w-full md:w-2/5 justify-center items-start text-center
             md:text-left">
            <!-- <p class="uppercase tracking-loose w-full text-white">What business we are?</p> -->
            <h1 class="my-4 text-4xl font-bold leading-tight text-black">
               Welcome to the DURGA Operations Dashboard !!

            </h1>
            <p class="leading-normal text-2xl mb-8 text-black">
               Experience unparalleled protection and resilience with Durga, your ultimate security companion.            </p>


         </div>
         <!--Right Col-->
         <div class="w-full md:w-3/5 py-6 text-center">
            <img class="w-full md:w-4/5 z-50"
             src="@/assets/static/security3.png " />
         </div>
      </div>
   </div>
</template>
 
<script>
import leftSidebar from '@/components/leftSidebar.vue';

export default {
   components: {
      leftSidebar,

   },
   data() {
      return {
         Username: '',
         zoomIn: false,
         zoomOut: false,
      };
   },
   created() {
      this.Username = sessionStorage.getItem("username");
   },
   mounted() {
      // Add the zoom-in class after a delay
      setTimeout(() => {
         this.zoomIn = true;
      }, 500);

      // Add the zoom-out class after a longer delay
      setTimeout(() => {
         this.zoomOut = true;
      }, 800);
   },
}

</script>
<style scoped>
.zoom-in {
   animation: zoomIn 1s;
}

.zoom-out {
   animation: zoomOut 1s;
}

@keyframes zoomIn {
   from {
      transform: scale(0.8);
      opacity: 0;
   }

   to {
      transform: scale(1);
      opacity: 1;
   }
}

@keyframes zoomOut {
   from {
      transform: scale(1);
      opacity: 1;
   }

   to {
      transform: scale(0.8);
      opacity: 0;
   }
}
.main_content {
   background: linear-gradient(90deg, #eeecee 0%, #8167c9 100%);

}

</style>
 
 