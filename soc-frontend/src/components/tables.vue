<template>
    <div>
      <h2>Vue Js</h2>
      <table class="table" id="datatable">
        <thead>
          <tr>
            <th>ID</th>
            <th>Rule Name</th>
            <th>Rule Description</th>
            <!-- <th>Created On</th> -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in products" :key="item.id">
            <td>{{ item.id }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.Description }}</td>
            <!-- <td>{{ item.created_at }}</td> -->
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import "jquery/dist/jquery.min.js";
  
  import "datatables.net-dt/js/dataTables.dataTables";
  import "datatables.net-dt/css/jquery.dataTables.min.css";
  
  export default {
    mounted() {
      axios.get("http://127.0.0.1:8000/api/v3/rules/")
      .then((response) => {
        this.products = response.data;
        this.initializeDataTable();
      });
    },
    data: function () {
      return {
        products: [],
      };
    },
    methods: {
      initializeDataTable() {
        $(document).ready(function () {
          $("#datatable").DataTable();
        });
      },
    },
  };
  </script>
  