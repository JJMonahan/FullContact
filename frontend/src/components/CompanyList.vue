<template>
    <v-container>
      <v-row>
        <v-col v-for="company in companies" :key="company.id" cols="12" md="4">
          <v-card>
            <h2>Company Info</h2>
            <v-card-title>{{ company.name }}</v-card-title>
            <v-card-subtitle>{{ company.address }}</v-card-subtitle>
            <v-card-text>{{ company.description }}</v-card-text>
            <v-card-actions>
              <v-btn text color="primary" @click="openLink(company.url)">
                Visit Website
              </v-btn>
              <v-btn text color="secondary" @click="openLink(company.mapurl)">
                View on Map
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        companies: [],
      };
    },
    mounted() {
      // Assuming you have a method to fetch data from the API using axios
      this.fetchCompaniesData();
    },
    methods: {
      async fetchCompaniesData() {
        
        try {
          const response = await this.$axios.get('http://localhost:8000/api/companies/');
          this.companies = response.data.results;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },

      
      openLink(url) {
        if (url && url !== 'NA' && url !== 'Unknown') {
          // Open the link in a new tab
          window.open(url, '_blank');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  