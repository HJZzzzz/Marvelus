<template>
  <div>
    <div class="login-wrap">
      <h3>Luminus Login</h3>
      <p v-show="showHelp">{{ help }}</p>
      <input type="text" placeholder="Please enter username" v-model="username">
      <input type="password" placeholder="Please enter password" v-model="password" @keyup.enter="login">
      <button v-on:click="login">Login</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      showHelp: false,
      help: '',
      username: '',
      password: ''
    }
  },
  mounted () {
    if (this.$store.state.username) {
      this.$router.push({name: 'home'})
    }
  },
  methods: {
    login () {
      this.$axios({
        method: 'post',
        url: this.$url + 'login/',
        data: {
          'username': this.username,
          'password': this.$util.encrypt(this.password)
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        transformRequest: [
          function (data) {
            let ret = ''
            for (let it in data) {
              ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
            }
            return ret
          }
        ]
      }).then(response => {
        if (response.data.state) {
          if (this.$store.state.isProf){
            this.$router.push({name: 'TeachList'})
          } else {
            this.$router.push({name: 'Index'})
          }
        } else {
          this.help = response.data.error
          this.showHelp = true
        }
      })
    }
  }
}
</script>

<style scoped>
h3 {
  margin-top: 200px;
}
.login-wrap {
  text-align:center;
}
input {
  display:block;
  width:250px;
  height:40px;
  line-height:40px;
  margin:0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
  outline:none;
  border:1px solid #888;
  padding:10px;
  box-sizing:border-box;
}
p {
  color:red;
}
button {
  display:block;
  width:250px;
  height:40px;
  line-height: 40px;
  margin:0 auto;
  border:none;
  background-color:#1565c0;
  color:#fff;
  font-size:16px;
  margin-bottom:5px;
}
</style>
