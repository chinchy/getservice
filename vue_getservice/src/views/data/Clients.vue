<template>
  <el-table :data="tableData">
      <el-table-column prop="first_name" label="Имя"></el-table-column>
      <el-table-column prop="last_name" label="Фамилия"></el-table-column>
      <el-table-column prop="phone" label="Телефон"></el-table-column>
      <el-table-column
          label="Действия"
          width="200">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">Изменить</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">Удалить</el-button>
        </template>
      </el-table-column>
    </el-table>
</template>

<script>
import axios from "axios";

export default {
  async created() {
    await axios.get('http://127.0.0.1:7000/api/v1/clients/all').then(resp => {
      this.tableData = []
      resp.data.forEach(element => this.tableData.push(
          {
            first_name: element.user.first_name,
            last_name: element.user.last_name,
            phone: element.phone
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