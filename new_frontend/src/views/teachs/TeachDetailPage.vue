<template>
  <div>
    <TeachSidebarMenu/>
    <div class="placeholder">
      <router-view/>
    </div>
  </div>
</template>

<script>
import TeachSidebarMenu from '../../components/TeachSidebarMenu'
export default {
  name: "TeachDetailPage",
  components:{
    TeachSidebarMenu
  }
}
</script>

<style scoped>
.placeholder {
  width: calc(100% - 175px);
  float:right;
}
</style>