<template>
  <div v-show="!loading" class="spinner">
    <div class="bg- opacity-60% absolute right-1/2 bottom-1/2 transform translate-x-1/2 translate-y-1/2">
      <div class="p-4 bg-gradient-to-r animate-spin from-green-500 via-purple-500 rounded-full">
        <div class="bg-white rounded-full">
          <div class="w-12 h-12   rounded-full"></div>
        </div>
      </div>
    </div>
  </div>

<div v-show="!loading">
    <div  class="p-4 w-full">
      <div class="flex flex-col mt-8  p-10">
        <div class=" ">
          <div class="flex items-center px-5 py-6 bg-gray-100 rounded-md shadow-sm">
            <div class="p-3 bg-blue-500 bg-opacity-75 rounded-full">
              <svg class="w-8 h-8" fill="#000000" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" width="64px" height="64px" viewBox="-54.76 -54.76 657.16 657.16"
                xml:space="preserve" transform="rotate(0)">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <g>
                    <g>
                      <path
                        d="M181.308,181.412h69.566v343.283c0,12.674,10.275,22.949,22.95,22.949s22.95-10.275,22.95-22.949v-34.199h40.832 c12.675,0,22.95-10.275,22.95-22.949s-10.275-22.949-22.95-22.949h-40.832v-32.686h40.832c12.675,0,22.95-10.275,22.95-22.949 s-10.275-22.949-22.95-22.949h-40.832V181.412h69.562c27.026,0,49.009-21.986,49.009-49.009V49.009 C415.346,21.983,393.36,0,366.337,0H181.308c-27.023,0-49.009,21.986-49.009,49.009v83.394 C132.299,159.429,154.285,181.412,181.308,181.412z M178.199,49.009c0-1.714,1.395-3.109,3.109-3.109h185.029 c1.714,0,3.109,1.396,3.109,3.109v83.394c0,1.713-1.396,3.109-3.109,3.109h-92.513h-92.516c-1.714,0-3.109-1.396-3.109-3.109 V49.009z">
                      </path>
                    </g>
                  </g>
                </g>
              </svg>
            </div>

            <div class="mx-5">
              <h4 class="text-2xl font-semibold text-gray-700"> {{ rules.length }} </h4>
              <div class="text-gray-500">Total Number of Rules</div> 
            </div>

            <button v-if="selectedRules.length > 0" @click.prevent="triggerPipeline"
              class="ml-auto   inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-500 to-pink-500 group-hover:from-purple-500 group-hover:to-pink-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-purple-200 dark:focus:ring-purple-800">
              <span class="w-28  px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
              Apply
              </span>
            </button>

          
          </div>
        </div>
      </div>
    </div>

    <div  class="p-4 w-full ">
      <div class="flex flex-col ">
        <div class="py-2 -my-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 lg:px-8">
          <div class="inline-block min-w-full overflow-hidden align-middle border-b border-gray-200 shadow sm:rounded-lg">
            <table class="min-w-full table" id="datatable">
              <thead>
                <tr>
                  <th scope="col" class="p-4">
                    <div class="flex items-center">
                      <label for="checkbox-all-search" class="sr-only">checkbox</label>
                    </div>
                  </th>

                  <th
                    class="px-6 py-3 text-md font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Rule Name
                  </th>

                  <th
                    class="px-6 py-3 text-md font-medium leading-4 tracking-wider text-left text-gray-500 uppercase border-b border-gray-200 bg-gray-50">
                    Rule Description
                  </th>
                </tr>
              </thead>

              <tbody class="bg-white">
                <tr v-for="rule in rules" :key="rule.name">
                  <td class="w-4 p-4">
                    <div class="flex items-center">
                      <input v-model="selectedRules" :value="rule.rule_number" id="checkbox-table-search-1" type="checkbox"
                        class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                      <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                    </div>
                  </td>
                  <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
                    <span class="inline-flex px-2 text-md font-semibold leading-5 text-green-500  rounded-md">
                      {{ rule.name }} </span>
                  </td>
                  <td class="px-6 py-4 border-b border-gray-200 overflow-hidden whitespace-pre-line max-w-xs">
                    <span class="inline-flex px-2 text-md font-semibold leading-5  rounded-md">
                      {{ rule.description }}
                    </span>
                  </td>
                  <!-- <td class="px-6 py-4  text-sm font-medium leading-5 text-right border-b border-gray-200 whitespace-nowrap">
                                <button class="text-indigo-600 hover:text-indigo-900"> Edit </button>
                        </td> -->
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>


  <!-- Modal -->
  <div id="popup-modal" v-show="isModalVisible" tabindex="-1" class="fixed top-0 left-0 right-0 bottom-0 
    z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
    <div class="relative w-[700px] ">
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">

        <button @click="toggleModel" type="button"
          class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white">
          <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
          </svg>
          <span class="sr-only">Close modal</span>
        </button>

        <div class="p-6 ">
          <h3 class="mb-5 text-lg font-normal text-black dark:text-gray-400">
            You are going to apply these rules </h3>
          <div class=" mb-6" v-for="(selectedRules, index) in selectedRules" :key="index">
            <div class=" shadow-md">
              <div class="text-gray-400 dark:text-white p-3">
                {{ selectedRules.name }}
              </div>

            </div>
          </div>
          <div class="mt-5">
           <button @click.prevent="triggerPipeline" class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
            <span class="w-24 relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
            Proceed 
            </span>
            </button>

            <button @click="toggleModel" class="relative inline-flex items-center justify-center p-0.5 mb-2 me-2 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-teal-300 to-lime-300 group-hover:from-teal-300 group-hover:to-lime-300 dark:text-white dark:hover:text-gray-900 focus:ring-4 focus:outline-none focus:ring-lime-200 dark:focus:ring-lime-800">
            <span class="relative w-24   px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-900 rounded-md group-hover:bg-opacity-0">
            Cancle
            </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import leftSidebar from './leftSidebar.vue';
import axios from "axios";
import "jquery/dist/jquery.min.js";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";

export default {
  components: {
    leftSidebar,
  },
  data(){
    return{
      loading: true
    }
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/api/v3/rules/")
      .then((response) => {
        this.rules = response.data;
        this.loading = false
        this.initializeDataTable();
      });
  },
  data: function () {
    return {
      isModalVisible: false,
      rules: [],
      selectedRules: [],
    };
  },
  methods: {
    toggleModel() {
      this.isModalVisible = !this.isModalVisible
    },

    triggerPipeline() {

      const data = {
        selectedRules: this.selectedRules,
        SelectedServer: this.SelectedServer,
      };
      console.log(data.selectedRules);
      this.$router.push("/result");
      axios
        .post("http://127.0.0.1:8000/api/v2/trigger/", data)
        .then((response) => {
          console.log("API response:", response.data);

        })
        .catch((error) => {
          console.error("API error:", error);

        })
        .finally(() => {
          this.toggleModal();
        });
    },

    initializeDataTable() {
      $(document).ready(function () {
        $("#datatable").DataTable();
      });
    },
  },
};
</script>

  
<style>.dataTables_wrapper .dataTables_length select {
  width: 55px;
}</style>
      
