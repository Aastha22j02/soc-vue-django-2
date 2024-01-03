<template>
  <div class="app-container flex">
    <LeftSidebar></LeftSidebar>
    <router-view></router-view>
  </div>
</template>

<script>
import LeftSidebar from './components/leftSidebar.vue';

export default {
  components: {
    LeftSidebar
  }
}
</script>

<style>
.app-container {
  grid-row: 2;
}

/* Adjust the width and other styles based on your layout */
LeftSidebar {
  float: left;
  position: relative;
  top: 0;
  left: 0;
  bottom: 0;
  width: 250px; /* Set your desired width */
  background-color: #f1f1f1; /* Set your desired background color */
  z-index: 100; /* Set a higher z-index to ensure it appears above other elements */
}

router-view {
  margin-left: 250px; /* Adjust the margin to match the width of LeftSidebar */
}
</style>
