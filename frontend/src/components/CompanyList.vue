<!-- CompanyList.vue -->
<template>
  <div>
    <h2>Company List</h2>
    <ul>
      <li v-for="company in companies" :key="company.id">
        <a :href="company.url">{{ company.name }}</a>
      </li>
    </ul>
  </div>
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
    // Assuming you make an API call and update the 'companies' data property
    // For example, using axios
    axios.get('http://localhost:8000/api/companies/')
      .then(response => {
        this.companies = response.data.results;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin-bottom: 0.5rem;
  background-color: #f0f0f0;
  padding: 0.5rem;
}
</style>