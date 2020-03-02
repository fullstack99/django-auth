<template>
  <div class="login-form">
    <v-card class="login-card">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>
        <v-text-field
          v-model="password"
          :rules="passwordRules"
          name="input-10-2"
          label="Password"
          hint="At least 8 characters"
          required
        ></v-text-field>
        <v-btn
          :disabled="!valid"
          color="success"
          @click="login"
        >
          Login
        </v-btn>
      </v-form>
    </v-card>
  </div>
</template>
<script>
  export default {
    data: () => ({
      valid: true,
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      password: '',
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 8) || 'Password must be more than 8 characters',
      ],
    }),

    methods: {
      login () {
        if (this.$refs.form.validate()) {
          this.snackbar = true
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
</style>