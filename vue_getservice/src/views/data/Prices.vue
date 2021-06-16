<template>
  <div>
    <el-button type="primary" icon="el-icon-plus" style="float: right">Добавить</el-button>
    <el-table :data="tableData">
        <el-table-column prop="service" label="Услуга"></el-table-column>
        <el-table-column prop="position" label="Должность"></el-table-column>
        <el-table-column prop="amount" label="Стоимость"></el-table-column>
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
    await axios.get('http://127.0.0.1:7000/api/v1/prices/all').then(resp => {
      this.tableData = []
      resp.data.forEach(element => this.tableData.push(
          {
            service: element.service.name,
            position: element.position.name,
            amount: element.amount + " руб."
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