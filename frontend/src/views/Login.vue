<template>
  <div class="login-form">
    <v-card class="login-card">
      <v-alert
        v-model="showErrorAlert"
        close-text="Close Alert"
        dark
        dismissible
        type="error"
      >
        {{errorMessage}}
      </v-alert>
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              prepend-inner-icon="mdi-email"
              label="E-mail"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-text-field
              v-model="password"
              :rules="passwordRules"
              prepend-inner-icon="mdi-key"
              label="Password"
              type="password"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-btn
              :disabled="!valid"
              color="success"
              @click="handleLogin"
            >
              Login
            </v-btn>
            <router-link to="/register" class="btn btn-register">Sign Up</router-link>
          </v-col>
        </v-row>
      </v-container>
      </v-form>
    </v-card>
  </div>
</template>
<script>
  import { mapActions, mapGetters } from "vuex";
  export default {
    data: () => ({
      valid: false,
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password: '',
      passwordRules: [
        v => !!v || 'Password is required'
      ],
      showErrorAlert: false
    }),
    computed: {
      ...mapGetters("auth", ["errorMessage"])
    },
    methods: {
      ...mapActions("auth", ["login"]),
      handleLogin () {

        if (this.$refs.form.validate()) {
          this.valid = true;
          this.login({
            email: this.email,
            password: this.password
          }).then((res) => {
            if (res.status == 200) {
              this.$router.push("/")
            } else {
              this.showErrorAlert = true;
            }
          }).catch(err => {
            console.log(err)
          })
        }
      },
    },
  }
</script>
<style scoped>
.login-form {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.login-card {
  width: 400px;
  padding: 10px;
  max-width: 100%;
  text-align: center;
}
.btn-register {
  text-decoration: none;
  margin-left: 15px;
  color: #757575;
}
</style>