<template>
  <div>
    <el-button type="primary" icon="el-icon-plus" style="float: right">Добавить</el-button>
    <el-table :data="tableData">
        <el-table-column prop="name" label="Наименование"></el-table-column>
        <el-table-column prop="duration" label="Длительность, ч." width="200"></el-table-column>
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  async created() {
    await axios.get('http://127.0.0.1:7000/api/v1/services/all').then(resp => {
      this.tableData = []
      resp.data.forEach(element => this.tableData.push(
          {
            name: element.name,
            duration: element.duration
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