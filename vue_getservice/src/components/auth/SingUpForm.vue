<template>
<!--  @submit.prevent="register"-->
  <el-form class="singup-form" ref="form" :model="form" label-width="120px">
    <p v-if="err">{{ err }}</p>

    <el-form-item required label="Название:">
      <el-input placeholder="Название..." v-model="form.first_name"></el-input>
    </el-form-item>

    <el-form-item label="E-mail:">
      <el-input
          placeholder="E-mail..."
          v-model="form.email"
          v-imask="emailMask"
          @input="isEmail">
      </el-input>
    </el-form-item>

    <el-form-item label="Логотип:">
      <el-upload
        class="avatar-uploader"
        action="https://jsonplaceholder.typicode.com/posts/"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
        <img v-if="imageUrl" :src="imageUrl" class="avatar" alt="">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
    </el-form-item>

    <el-form-item required label="Тип фирмы:">
      <el-select style="width: 100%" v-model="form.type" placeholder="Тип фирмы...">
        <el-option
          v-for="item in types"
          :key="item.value"
          :label="item.text"
          :value="item.value">
        </el-option>
      </el-select>
    </el-form-item>

    <el-form-item required label="Логин:">
      <el-input placeholder="Логин..." v-model="form.username"></el-input>
      <p><small class="text-muted">Минимальная длина логина 5 символов</small></p>
    </el-form-item>

    <el-form-item required label="Пароль:">
      <el-input placeholder="Пароль..." v-model="form.password" show-password></el-input>
      <p><small class="text-muted">Минимальная длина пароля 6 символов</small></p>
    </el-form-item>

    <el-form-item required label="Повторите пароль:">
      <el-input placeholder="Пароль..." v-model="form.repeatPassword" show-password></el-input>
    </el-form-item>

    <p class="text-danger" v-if="!$v.form.password.minLength">Длина пароля меньше 6 символов</p>

    <p class="text-danger" v-if="isPasswordTheSame">Введённые пароли не совпадают</p>

    <el-button type="primary" native-type="submit" :disabled="formValid">Регистрация</el-button>

    <p>
      <small class="text-muted">
        Все поля отмеченные <span class="text-danger">*</span> обязательны для заполнения.
      </small>
    </p>

    <p>Уже есть аккаунт? <router-link to="/auth/signin">Вход</router-link></p>

  </el-form>
</template>

<script>
import { required, minLength, sameAs } from 'vuelidate/lib/validators'
import { IMaskDirective } from 'vue-imask'
import authRequest from '@/mixins/authRequest'
export default {
  name: "SignUpForm",
  data () {
    return {
      form: {
        username: "",
        first_name: "",
        email: "",
        password: "",
        repeatPassword: "",
      },
      emailMask: {
        mask: 'company@domain.ru',
        lazy: true
      },
      types: [
        { text: 'Салон красоты', value: '1' },
        { text: 'Автосервис', value: '2' },
        { text: 'Маникюрный салон', value: '3' },
        { text: 'Медицинский центр', value: '4' },
        { text: 'Сервисный центр', value: '5' }
      ],
      err: '',
      imageUrl: ''
    }
  },
  validations: {
    form: {
      username: {
        required,
        minLength: minLength(5)
      },
      first_name: {
        required
      },
      password: {
        required,
        minLength: minLength(6)
      },
      repeatPassword: {
        required,
        sameAs: sameAs('password')
      },
      type: {
        required
      }
    }
  },
  computed: {
    formValid () {
      return this.$v.$invalid
    },
    isPasswordTheSame () {
      const form = this.$v.form
      return form.password.required
        && form.repeatPassword.required
        && !form.repeatPassword.sameAs
    }
  },
  mixins: [ authRequest ],
  methods: {
    async register () {
      // логика регистрации
      try {
        await this.authRequest('auth/users', this.form)
        // редиректим, если нет ошибки
        this.$router.push('/auth/signin')
      } catch (e) {
        console.error('AN API ERROR', e)
        this.err = e
      }
    },
    // onAccept (e) {
    //   const maskRef = e.detail
    //   this.form.phone = maskRef.value
    // },
    // onComplete (e) {
    //   const maskRef = e.detail
    //   this.userPhone = maskRef.unmaskedValue
    // },
    // isNumber (e) {
    //   const regex = /[0-9]/
    //   if (!regex.test(e.key)) {
    //     e.returnValue = false;
    //     if (e.preventDefault) e.preventDefault();
    //   }
    // },
    isEmail (e) {
      const regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      if (!regex.test(e.key)) {
        e.returnValue = false;
        if (e.preventDefault) e.preventDefault();
      }
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('Логотип должен быть в формате JPEG!');
      }
      if (!isLt2M) {
        this.$message.error('Логотип должен весить не более 2Мб!');
      }
      return isJPG && isLt2M;
    }
  },
  directives: {
    imask: IMaskDirective
  }
};
</script>

<style scoped>
.singup-form >>> .form-group.required .control-label:after {
  content:" *";
  color:red;
}
.singup-form >>> .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}
.singup-form >>> .avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}
.singup-form >>> .avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.singup-form >>> .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>