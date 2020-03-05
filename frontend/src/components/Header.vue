<template>
  <nav class="nav-bar">
    <v-navigation-drawer v-model="sidebar" app class="sider-bar">
      <v-list>
        <v-list-group>
          <template v-slot:activator>
            <v-list-item-icon>
              <v-icon>mdi-account-circle</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Users</v-list-item-title>
          </template>

          <v-list-item-group v-model="item" color="primary">
            <v-list-item
              v-for="(item, i) in items"
              :key="i"
              @click="handleAction(item.action)"
            >
              <v-list-item-icon>
                <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app class="header-bar" dark>
      <span class="hidden-sm-and-up">
        <v-app-bar-nav-icon @click="sidebar = !sidebar"></v-app-bar-nav-icon>
      </span>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn icon @click="showList=!showList">
          <v-avatar color="indigo">
            <v-icon dark>mdi-account-circle</v-icon>
          </v-avatar>
        </v-btn>
        <v-card
          class="mx-auto user-action-list-card"
          width="150"
          v-show="showList"
        >
          <v-list flat>
            <v-list-item-group v-model="item" color="primary">
              <v-list-item
                v-for="(item, i) in items"
                :key="i"
                @click="handleAction(item.action)"
              >
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-toolbar-items>
    </v-app-bar>
  </nav>
</template>

<script>
import { mapActions} from "vuex";
export default {
  name: "Header",
  data() {
    return {
      sidebar: false, // Hide mobile side menu by default
      menuItems: [
        { title: "User", path: "/" }
      ],
      item: { text: 'Profile', icon: 'mdi-account', action: 'gotoProfile' },
      items: [
        { text: 'Profile', icon: 'mdi-account', action: 'gotoProfile' },
        { text: 'Logout', icon: 'mdi-logout', action: 'logout' },
      ],
      showList: false
    };
  },
  methods: {
    ...mapActions("auth", ["logout"]),
    handleAction(actionName) {
      this.showList = !this.showList;
      if (actionName == 'logout') {
        this.logout();
        this.$router.push("/login")
      }
    }
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
.user-action-list-card {
  position: absolute !important;
  top: 64px;
  right: 1px;
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