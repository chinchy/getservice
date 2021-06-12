<template>
  <el-col class="upload-avatar" :span="12" :offset="6">
    <slot></slot>
  </el-col>
</template>
<script>
export default {
  name: 'BaseAuthLayout'
}
</script>