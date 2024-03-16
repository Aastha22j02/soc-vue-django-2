<template>
  <div>
    <!-- leftsider bar -->
    <div :class="['h-screen p-5 pt-8 relative    bg-blue-800 ', store.open ? 'w-72' : 'w-20']">
      <img src="../assets/control.png"
        class="absolute cursor-pointer -right-3 top-9 w-7 h-7 border-dark-purple border-2 rounded-full"
        :class="{ 'rotate-180': !store.open }" @click="toggleSidebar" />

      <router-link to="/home">
        <div class="flex gap-x-4 items-center  ">
          <img src="../assets/logo.png " class="cursor-pointer duration-500 w-7 h-7"
            :class="{ 'rotate-[360deg]': store.open }" />
          <h1 class="text-white origin-left font-bold text-xl duration-200" :class="{ 'scale-0': !store.open }">
            HOME 
          </h1>
        </div>
      </router-link>


      <ul class="pt-6">
        <router-link v-for="(menu, index) in menus" :key="index" :to="`/${menu.routeName}`"
          class="flex rounded-md p-2 cursor-pointer hover:bg-light-white text-gray-300 text-sm items-center gap-x-4"
          :class="{ 'mt-9': menu.gap, 'mt-2': !menu.gap, 'bg-light-white': index === 0 }">
          <img class="w-8 h-8" :src="`./src/assets/${menu.src}.png`" />
          <span class="text-lg font-medium " :class="{ hidden: !store.open, 'origin-left duration-200': store.open }">
            {{ menu.title }} </span>
        </router-link>
  
      </ul>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue';
import { useSidebarStore } from '@/stores/sidebar';


export default defineComponent({
  name: 'App',

  setup() {

    const store = useSidebarStore()

    const open = ref(true);

    const menus = [

      { title: 'SOC Dashboard', src: 'socdashboard', routeName: 'socdashboard' },

      { title: 'Server Onboard', src: 'serverOnboard', routeName: 'onBoard' },

      { title: 'Rules', src: 'rules', routeName: 'rules' },

      { title: 'Documentation', src: 'document', gap: true },

      { title: 'Help', src: 'help', },

    ];

    const isOpen = computed(() => store.open);

    function toggleSidebar() {
      store.toggleSidebar();
    }
    const setOpen = (value) => {
      open.value = value;
    };

    return {
      open,
      menus,store,
      setOpen, toggleSidebar,

    };

  },

});

</script>

<style lang="scss" scoped></style>