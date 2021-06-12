<template>
  <base-auth-layout>
    <sign-in-form />
  </base-auth-layout>
</template>
<script>
import SignInForm from '@/components/auth/SingInForm.vue'
import BaseAuthLayout from '@/layouts/BaseAuthLayout.vue'
export default {
  name: "SignIn",
  components: { SignInForm, BaseAuthLayout }
}
</script>