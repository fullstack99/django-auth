<template>
  <div class="login-form">
    <v-card class="login-card">
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
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12">
            <v-btn
              :disabled="!valid"
              color="success"
              @click="login"
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
    }),

    methods: {
      login () {
        if (this.$refs.form.validate()) {
          this.valid = true
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