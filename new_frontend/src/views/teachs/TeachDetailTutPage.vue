<template>
  <div>
    <router-view :tutorials = "tutorials" />
  </div>
</template>

<script>
export default {
  name: "TeachDetailTutPage",
  data() {
    return {
      msg: 'Network Error',
      tutorials: null,
      state: false,
    }
  },
  mounted() {
    this.getTuts();
  },
  methods:{
    getTuts: function () {
      this.$axios.request({
        url: this.$url + 'tutorials/code/'+ this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.state = true
          this.tutorials = data.data.tutorials
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    }
  }
}
</script>

<style scoped>

</style>