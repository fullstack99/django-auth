<template>
  <nav class="nav-bar">
    <v-navigation-drawer v-model="sidebar" app class="sider-bar">
      <v-list>
        <v-list-item
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          <v-list-item-content v-text="item.title"></v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app class="header-bar" dark>
      <span class="hidden-sm-and-up">
        <v-app-bar-nav-icon @click="sidebar = !sidebar"></v-app-bar-nav-icon>
      </span>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn
          text
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
  </nav>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      sidebar: false, // Hide mobile side menu by default
      menuItems: [
        { title: "User", path: "/" }
      ]
    };
  }
};
</script>
<style>
.nav-bar a {
  font-weight: 600;
}
.theme--dark.v-application {
  background-color: #000000 !important;
}
.header-bar {
  z-index: 9999 !important;
}
.sider-bar {
  z-index: 9999 !important;
  padding-top: 50px;
}
.logo-router {
  height: 100%;
}
.logo-img {
  height: 60px;
  max-height: 100%;
}
@media screen and (min-width: 1000px) {
  .v-navigation-drawer {
    display: none !important;
    width: 0px !important;
  }
  main.v-content {
    padding-left: 0 !important;
  }
  header {
    left: 0 !important;
  }
}

@media only screen and (max-width: 959px) {
  .v-application .hidden-sm-and-up {
    display: block !important;
  }
}
</style>