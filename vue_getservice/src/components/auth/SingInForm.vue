<template>
<!--  @submit.prevent="login"-->
  <el-form ref="form" :model="form" label-width="120px">
    <el-form-item label="Логин:">
      <el-input placeholder="Логин..." v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item label="Пароль:">
      <el-input placeholder="Пароль..." v-model="form.password" show-password></el-input>
    </el-form-item>
    <el-button type="primary" native-type="submit">Войти</el-button>
    <p>
      Ещё не зарегистрированы? <router-link to="/auth/signup">Регистрация</router-link>
    </p>
  </el-form>
</template>

<script>
import authRequest from '@/mixins/authRequest'
export default {
  name: "SignInForm",
  data () {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  mixins: [ authRequest ],
  methods: {
    async login () {
      // логика авторизации
      try {
        const response = await this.authRequest('auth/token', this.form)
        // авторизуем юзера
        this.setLogined(response.data.token)

      } catch (error) {
        console.error('AN API ERROR:', error)
      }
    },
    setLogined (token) {
      // сохраняем токен
      console.log(token);
      localStorage.setItem('token', token);
    }
  }
};
</script>