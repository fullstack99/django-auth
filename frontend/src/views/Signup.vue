<template>
  <div class="register-form">
    <v-card class="register-card">
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
            <v-col cols="12" md="6">
              <v-text-field
                v-model="firstName"
                :rules="nameRules"
                label="First Name"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="lastName"
                :rules="nameRules"
                label="Last Name"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showPass ? 'text' : 'password'"
                label="Password"
                hint="At least 8 characters"
                counter
                @click:append="showPass = !showPass"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="confirmPassword"
                :rules="passwordRules"
                type="password"
                label="Confirm Password"
                required
                v-on:change="checkPass"
              ></v-text-field>
              <span v-if="showConfirmError" class="show-error-message">Password does not matched</span>
            </v-col>
            <v-col cols="12">
              <v-btn
                :disabled="!valid"
                color="success"
                @click="handleRegister"
              >
                register
              </v-btn>
              <router-link to="/login" class="btn btn-login">Login</router-link>
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
    valid: true,
    firstName: '',
    lastName: '',
    nameRules: [
      v => !!v || 'Password is required',
      v => (v && v.length >= 2) || 'Password must be more than 2 characters',
    ],
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
    confirmPassword: '',
    showPass: false,
    showConfirmError: false,
    showErrorAlert: false
  }),
  computed: {
    ...mapGetters("auth", ["errorMessage"])
  },
  methods: {
    ...mapActions("auth", ["register"]),
    handleRegister() {
      if (this.$refs.form.validate() && !this.showConfirmError) {
        this.snackbar = true
        this.valid = true;

        this.register({
          email: this.email,
          firstName: this.firstName,
          lastName: this.lastName,
          password: this.password,
          confirmPassword: this.confirmPassword
        }).then((res) => {
          if(res.status == 200) {
            this.$router.push("/")
          } else {
            this.showErrorAlert = true;
          }
        }).catch(err => {
          console.log(err)
        })
      }
    },
    checkPass() {
      if(this.password != this.confirmPassword) {
        this.showConfirmError = true
      } else {
        this.showConfirmError = false
      }
    }
  },
}
</script>
<style scoped>
.register-form {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 15px;
}
.register-card {
  width: 100%;
  max-width: 720px;
}
.v-form {
  margin: 0 auto;
  text-align: center;
}
.btn-login {
  text-decoration: none;
  margin-left: 15px;
  color: #757575;
}
.show-error-message {
  position: absolute;
  left: 11px;
  font-size: 12px;
  color: #ff5252;
}
</style>
