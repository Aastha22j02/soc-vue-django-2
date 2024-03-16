<template> 
  <navBar/>
  <div class="flex fixed mt-16">
      <!-- leftsider bar -->
      <leftSidebar />

      <!-- center panel -->
      <div class="h-screen w-[1665px] pb-5 flex-1 flex flex-col overflow-hidden">
        <div class="flex-1 overflow-x-hidden overflow-y-auto p-7">
          <rulePage/>
        </div>
    </div>
  </div>
</template>
  
  
<script>

import { defineComponent, ref } from 'vue';
import leftSidebar from '@/components/leftSidebar.vue';
import navBar from '@/components/navBar.vue';
import rulePage from '@/components/rulePage.vue';

export default defineComponent({
  name: 'App',
  components: {
    leftSidebar,navBar,rulePage
  },

  setup() {
    const open = ref(true);
    const menus = [

      { title: 'SOC Dashboard', src: 'socdashboard', routeName: 'socdashboard' },

      { title: 'Server Onboard', src: 'serverOnboard', routeName: 'onBoard' },

      { title: 'Rules', src: 'rules', routeName: 'rules' },

      { title: 'Documentation', src: 'document', gap: true , routeName: 'socdashboard'},

      { title: 'Help', src: 'help', routeName: 'socdashboard' },

    ];
    const setOpen = (value) => {
      open.value = value;
    };

    return {
      open,
      menus,
      setOpen,

    };

  },

});

</script>
  
  
<style scoped></style>