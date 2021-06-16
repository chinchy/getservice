<template>
  <el-table
      :data="tableData"
      stripe
      style="width: 100%">
        <el-table-column
          prop="name"
          label="Категория">
        </el-table-column>
        <el-table-column
          prop="count"
          label="Количество">
        </el-table-column>
      </el-table>
</template>

<script>
export default {
  data() {
    return {
      tableData: [{
        name: 'Записи клиентов',
        count: 2
      }, {
        name: 'Филиалы',
        count: 1
      }, {
        name: 'Сотрудники',
        count: 5
      }, {
        name: 'Услуги',
        count: 15
      }, {
        name: 'Должности',
        count: 5
      }, {
        name: 'Позиций в прайс листе',
        count: 15
      }, {
        name: 'Клиентов',
        count: 1
      }]
    }
  }
}
</script>

<style scoped>

</style>