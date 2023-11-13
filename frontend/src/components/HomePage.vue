<!-- src/views/Home.vue -->
<template>
    <div>
      <header>
        <h1>FullContact</h1>
        <nav>
          <router-link to="/jobs">Jobs</router-link>
          <router-link to="/companies">Companies</router-link>
          <router-link to="/contacts">Contacts</router-link>
          <router-link to="/roles">Roles</router-link>
        </nav>
      </header>
  
      <main>
        <section>
          <h2>Data</h2>
          <p>This is the content area in the middle of the page.</p>
        </section>
      </main>
  
      <footer>
        <router-link to="/about">About</router-link>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  header {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
  }
  
  nav {
    display: flex;
    justify-content: space-around;
    margin-top: 1rem;
  }
  
  main {
    padding: 2rem;
  }
  
  footer {
    background-color: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
    position: fixed;
    bottom: 0;
    width: 100%;
  }
  </style>