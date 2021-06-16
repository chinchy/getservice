<template>
  <div id="app">
    <el-container>
      <el-aside>
        <el-menu
          default-active="1"
          class="el-menu-vertical"
          :router="true">
          <img src="./assets/images/full-logo.png" alt="GetService logo" class="aside-logo">
          <el-menu-item index="/">
            <i class="el-icon-s-home"></i>
            <span>Домашняя страница</span>
          </el-menu-item>
          <el-menu-item index="/entries/">
            <i class="el-icon-date"></i>
            <span>Календарь записей</span>
          </el-menu-item>
          <el-menu-item index="/offices/">
            <i class="el-icon-office-building"></i>
            <span>Филиалы</span>
          </el-menu-item>
          <el-menu-item index="/employees/">
            <i class="el-icon-s-custom"></i>
            <span>Сотрудники</span>
          </el-menu-item>
          <el-menu-item index="/services/">
            <i class="el-icon-s-order"></i>
            <span>Услуги</span>
          </el-menu-item>
          <el-menu-item index="/positions/">
            <i class="el-icon-receiving"></i>
            <span>Должности</span>
          </el-menu-item>
          <el-menu-item index="/prices/">
            <i class="el-icon-money"></i>
            <span>Прайс лист</span>
          </el-menu-item>
          <el-menu-item index="/clients/">
            <i class="el-icon-user-solid"></i>
            <span>База клиентов</span>
          </el-menu-item>
          <el-menu-item index="/reports/">
            <i class="el-icon-s-marketing"></i>
            <span>Подготовка отчётности</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header style="text-align: right;">
<!--          <el-dropdown>-->
<!--            <i class="el-icon-setting" style="margin-right: 15px"></i>-->
<!--            <el-dropdown-menu slot="dropdown">-->
<!--              <el-dropdown-item>View</el-dropdown-item>-->
<!--              <el-dropdown-item>Add</el-dropdown-item>-->
<!--              <el-dropdown-item>Delete</el-dropdown-item>-->
<!--            </el-dropdown-menu>-->
<!--          </el-dropdown>-->
          <div id="avatar">
<!--            <el-avatar size="medium" icon="el-icon-user-solid"></el-avatar>-->
<!--            <router-link tag="el-link" style="padding-left: 5px; color: #323c48" to="/auth/signin">-->
<!--              Вход/Регистрация-->
<!--            </router-link>-->
            <el-avatar size="medium"
                       src="https://i.ibb.co/872PyZn/121512252-348185422962856-1560874474131106048-n.jpg">
            </el-avatar>
            <router-link tag="el-link" style="padding-left: 5px; color: #323c48" to="/auth/signin">
              Абрикос
            </router-link>
          </div>
        </el-header>

        <el-main>
          <router-view/>
        </el-main>

        <el-footer>©GetService 2021</el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'app',
  // data() {
  //   return {
  //     activeIndex: '1',
  //   };
  // },
  // methods: {
  //   handleSelect(key, keyPath) {
  //     console.log(key, keyPath);
  //   }
  // }
}
</script>

<style>
html, body {
  height: 100%;
}
body > * {
  position: relative;
  min-height:100%;
}
#app {
  font-family: "Helvetica Neue", sans-serif;
  text-align: center;
  position: relative;
  height:auto !important;
  min-height:100%;
}
.el-menu-vertical{
  max-width: 255px;
  width: 100%;
}
.aside-logo {
  width: 160px;
}
.el-header {
    background-color: #5794ae;
    color: #333;
    line-height: 60px;
}
.el-footer {
    background-color: #5794ae;
    color: #333;
    line-height: 60px;
  }
</style>
<style scoped>
#app >>> #avatar {
  display: flex;
  align-items: center;
  justify-content: end;
}
</style>
