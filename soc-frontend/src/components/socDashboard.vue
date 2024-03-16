[10:01 AM] Ashish Sahu
<template>
  <navBar />
  <div class="flex fixed mt-16 ">
    <leftSidebar />
 
    <div :class="['h-screen pb-5 flex-1 flex flex-col overflow-hidden', store.open ? 'w-[1625px]' : 'w-[1830px]']">           
      <button @click="toggleDashboard" class="p-2 m-2 bg-blue-500 text-white rounded">Switch Dashboard</button>
 
      <div class="flex-1 overflow-x-hidden overflow-y-auto p-7" style="margin-bottom: 20px;">
        <iframe v-if="currentDashboard === 1" width="100%" height="100%" :src="embedUrl" frameborder="0" allowfullscreen class="m-5"></iframe>
        <iframe v-else-if="currentDashboard === 2" width="100%" height="100%" :src="embedUrl2" frameborder="0" allowfullscreen class="m-5"></iframe>
        <!-- Add more else-if conditions for additional dashboards if needed -->
      </div>    
    </div>
  </div>
</template>
 
<script>
import { ref, computed } from 'vue';
import leftSidebar from '@/components/leftSidebar.vue';
import navBar from '@/components/navBar.vue';
import { useSidebarStore } from '@/stores/sidebar';
 
export default {
  components: {
    leftSidebar,
    navBar,
  },
  setup() {
    const store = useSidebarStore();
    const currentDashboard = ref(1);
 
    const toggleDashboard = () => {
      currentDashboard.value = (currentDashboard.value === 1) ? 2 : 1;
    };
 
    const embedUrl = computed(() => {
      return `http://172.16.1.55:5601/app/dashboards?auth_provider_hint=anonymous1#/view/1002c610-a23f-11ed-9c45-1d7f2cbf4bd8?embed=true&_g=(refreshInterval%3A(pause%3A!t%2Cvalue%3A60000)%2Ctime%3A(from%3Anow-10m%2Cto%3Anow))&show-top-menu=true&show-query-input=true&show-time-filter=true`
  
 
    });
 
    const embedUrl2 = computed(() => {
      return `http://172.16.1.55:5601/app/discover#/?_g=(refreshInterval:(pause:!t,value:60000),time:(from:now-16m,to:now))&_a=(columns:!(),filters:!(),index:'12b7b007-b388-4778-9e1f-20d5dc187d3e',interval:auto,query:(language:kuery,query:''),sort:!(!('@timestamp',desc)))`
    });
 
    return {
      store,
      toggleDashboard,
      currentDashboard,
      embedUrl,
      embedUrl2,
    };
  },
};
</script>
 