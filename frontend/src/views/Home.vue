<template>
  <v-container fluid>
    <!-- Header Component -->
    <Header @switch-view="switchView" :currentView="currentView" />

    <v-row>
      <!-- Main Content -->
      <v-col :cols="12">
        <!-- Main content goes here -->
        <v-card>
          <v-card-title>Main Content</v-card-title>
          <v-card-text>

            <!-- Include the JobList component -->
            <job-list v-if="currentView === 'jobs'" />

            <!-- Include the CompanyList component -->
            <company-list v-if="currentView === 'companies'" />

          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Footer Component -->
    <Footer />
  </v-container>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import CompanyList from '@/components/CompanyList.vue';
import JobList from '@/components/JobList.vue';

export default {
  name: 'Home',
  components: {
    Header,
    Footer,
    CompanyList,
    JobList,
  },
  data() {
    return {
      currentView: 'jobs', // Default view
    };
  },
  methods: {
    switchView(view) {
      this.currentView = view;
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
