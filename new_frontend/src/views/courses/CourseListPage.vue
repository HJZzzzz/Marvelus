<template>
  <div class="course-list-page">
    <div class="course-card" v-for="course in courses" @click="goCourse(course.code)" @mousemover.native="hover = true" @mouseleave.native="hover = false" :key="course.code">
      <div class="course-code"> {{course.code}} </div>
      <div class="course-title title-font"> {{course.title}} </div>
      <div class="course-detailed-info"> {{course.title}} </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseListPage",
  props:{
    courses:Array
  },
  methods: {
    goCourse: function (code) {
      this.$router.push({name: 'CourseDetail', params: {code: code}})
    }
  },
  data(){
    return {
      hover:false,
    };
  }
}
</script>

<style scoped>
.course-list-page{
  padding-left: 30px;
  padding-right: 30px;
  width: 100%;
  height: 100%;
  background-color: grey;
}
.title-font{
  font-weight: Bold;
  font-size: 25px;
}
.course-card {
  display: inline-block;
  background-color: #ffffff;
  /*border: #FFFFFF solid 1px;*/
  float: left;
  padding: 20px;
  margin: 10px;
  max-width: 280px;
  max-height: 240px;
  min-width: 210px;
  min-height: 180px;
  width: 28%;
  height: 28%;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}
.course-card:hover{
  background: #ffffff;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  animation-name: example;
  animation-duration: 0.25s;
  border-left: 8px solid #1976d2;
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}
.course-code{
  font-size: 14px;
  color: grey;
  text-align: left;
}
.course-title{
  margin-top: 5px;
  text-align: left;
  height: 100px;
}
.course-detailed-info{
  font-size: 12px;
  color: grey;
  text-align: left;
  height: 50px;
}
</style>