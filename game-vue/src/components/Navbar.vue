<template>
  <div id="navbar">
<b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="#">Game</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Play</b-nav-item>
        <b-nav-item href="#">Missions</b-nav-item>
        <b-nav-item href="#">Shop</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
       

        <b-nav-item-dropdown right no-caret>
          <template #button-content>
            <b-icon icon="person-fill" variant="secondary"></b-icon>
            <em class="ml-2">My account</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  </div>
</template>

<script>
export default {
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    logout() {
      localStorage.clear()
      this.isLoggedIn = false
      this.$router.push('/pitch/login')
    },
  },
  computed: {
    },
};
</script>

<style>
</style>
