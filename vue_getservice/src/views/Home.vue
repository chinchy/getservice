<template>
  <div>
    <el-row>
      <el-col :span="24">
        <div class="block home" key="contain">
          <el-image
            style="width: 150px; height: 150px"
            src="https://i.ibb.co/872PyZn/121512252-348185422962856-1560874474131106048-n.jpg"
            fit="contain">
          </el-image>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12" :offset="6">
        <h2>Салон красоты "Абрикос"</h2>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
h2 {
  color: rgb(50, 60, 72);
}
.home {
  margin-top: 100px;
}
</style>