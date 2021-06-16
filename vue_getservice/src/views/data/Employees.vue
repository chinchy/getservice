<template>
  <div>
    <el-button type="primary" icon="el-icon-plus" style="float: right">Добавить</el-button>
    <el-table :data="tableData">
      <el-table-column prop="fio" label="ФИО"></el-table-column>
      <el-table-column prop="position" label="Должность"></el-table-column>
      <el-table-column prop="office" label="Филиал"></el-table-column>
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
    await axios.get('http://127.0.0.1:7000/api/v1/employees/all').then(resp => {
      this.tableData = []
      resp.data.forEach(element => this.tableData.push(
          {
            fio: element.fio,
            position: element.position.map(x => x.name).join(", "),
            office: element.office.address
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