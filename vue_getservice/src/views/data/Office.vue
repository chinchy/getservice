<template>
  <el-table :data="tableData">
      <el-table-column prop="address" label="Адрес">
      </el-table-column>
      <el-table-column prop="phone" label="Телефон">
      </el-table-column>
      <el-table-column prop="schedule" label="Режим работы">
      </el-table-column>
    </el-table>
</template>

<script>
import axios from "axios";

export default {
  async created() {
    await axios.get('http://127.0.0.1:7000/api/v1/offices/all?company=2').then(resp => {
      this.tableData = []
      resp.data.forEach(element => this.tableData.push(
          {
            address: element.address,
            phone: element.phone,
            schedule: element.schedule
          }
      ))
    });
  },
  data() {
    return {
      tableData: []
    }
  }
};
</script>

<style scoped>

</style>