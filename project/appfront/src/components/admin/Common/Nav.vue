<template>
    <el-col>
    <el-menu
    :default-active=activename
      class="el-menu-vertical-demo nav"
      background-color="#66209A"
      text-color="#eee"
      active-text-color="#d49178" router>
      <el-menu-item index="/home_admin">
        <span slot="title">首页</span>
      </el-menu-item>
      <el-menu-item index="/audit_user">
        <span slot="title">用户审核</span>
      </el-menu-item>
      <el-menu-item index="/view_project">
        <span slot="title">项目查看</span>
      </el-menu-item>
      <el-menu-item index="/view_user">
        <span slot="title">用户查看</span>
      </el-menu-item>
      <el-menu-item index="/feedback_user">
        <span slot="title">查看用户反馈</span>
      </el-menu-item>
      <el-menu-item index="/view_refer">
        <span slot="title">查看易损性数据库</span>
      </el-menu-item>
    </el-menu>
  </el-col>
</template>

<script>
export default {
  beforeMount(){
    this.get_url()
  },
  methods:{
    get_url(){
      let _this = this
      console.log(_this.activename)
      //console.log(this.$route.path)
      var path1 = this.$route.path.split("/")
      console.log('/'+path1[1])
      _this.activename = '/'+path1[1]
    }
  },
  data(){
    return{
      activename:this.$route.path
    }
  },
  watch:{
    "$route": "get_url"
  }
}
</script>

<style scoped>
    .nav{
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.3);
        margin:0 2px 0 5px;
        border-radius: 5px;
        font-weight: 400;
        height: 600px;
    }
    
</style>
