<template>
    <v-container>
      <v-data-table
        :headers="headers"
        :items="jobs"
        :search="search"
      >
        <template v-slot:items="props">
          <td>{{ props.item.title }}</td>
          <td>{{ props.item.description }}</td>
          <td>
            <v-chip v-for="contact in props.item.contacts" :key="contact.id" label>
              {{ contact.fname }} {{ contact.lname }}
            </v-chip>
          </td>
          <td>{{ props.item.company.name }}</td>
          <td>
            <v-btn :href="props.item.url" target="_blank" icon>
              <v-icon>mdi-open-in-new</v-icon>
            </v-btn>
          </td>
        </template>
      </v-data-table>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        jobs: [],
        headers: [
          { text: 'Title', value: 'title' },
          { text: 'Description', value: 'description' },
          { text: 'Contacts', value: 'contacts' },
          { text: 'Company', value: 'company.name' },
          { text: 'URL', value: 'url' },
        ],
        search: '',
      };
    },
    mounted() {
      this.fetchJobs();
    },
    methods: {
      async fetchJobs() {
        try {
          const response = await fetch('http://localhost:8000/api/jobs');
          const data = await response.json();
          this.jobs = data.results;
        } catch (error) {
          console.error('Error fetching jobs:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  </style>
  