<template>
  <v-app>
    <v-content>
      <!-- Display view pages here based on route -->
      <Header v-show="isAuthenticated"/>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>
<script>
import { mapGetters } from "vuex";
import Header from "@/components/Header.vue";
export default {
  components: {
    Header
  },
  computed: {
    ...mapGetters("auth", ["isAuthenticated"])
  }
}
</script>