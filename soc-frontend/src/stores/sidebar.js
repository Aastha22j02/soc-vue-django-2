// src/store/sidebar.js
import { defineStore } from 'pinia';

export const useSidebarStore = defineStore('sidebar', {
  state: () => ({
    open: false,
  }),

  actions: {
    toggleSidebar() {
      this.open = !this.open;
    },
  },
});
