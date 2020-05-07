<template>
<div id="main">
    <el-container class="div-container">
        <el-header>
            <el-menu
            :default-active="defaultActive"
            background-color="#c2e9fb"
            mode="horizontal"
            router
            class="el-menu-demo"
            @select="handleselect"
            >
                <el-menu-item v-for="(item, i) in navList" :key="i" :index="item.name">
                    <span class="every-item">{{ item.navItem }}</span>
                </el-menu-item>
            </el-menu>

            <div class="login-logout">
                <span class="login">欢迎您，{{ name }}</span>
                <el-link type="danger" class="logout" @click="dologout">注销</el-link>
            </div>
        </el-header>

        <!-- 导航下方主页面-->
        <router-view class="menu-bottom"></router-view>
    </el-container>
</div>
</template>

<script>
    import store from '../store';
    import https from '../api/https.js';

    export default {
        name: 'Main',
        data () {
            return {
                navList: [
                    {name: '/main/usermain', navItem: '用户主页'},
                    {name: '/main/history', navItem: '历史记录'},
                    {name: '/main/new', navItem: '新建评分'}
                ],
                // TODO： 添加昵称申请
                name: '',
                defaultActive: '/main/usermain'
            }
        },
        methods: {
            dologout () {
                store.commit('del_token');
                sessionStorage.removeItem('token');
                this.$router.push('/login');
            },
            // 无论在哪个页面，后退都返回登录页面
            handleselect () {
                this.$router.push('/login')
            }
        },
        created () {
            https.fetchGet('users', {}).then((res) => {
                if (res.data['code'] === 200) {
                    this.name = res.data['name'];
                    return true;
                } else {
                    return false;
                }
            });
            // 如果不是主页根路径，则导航菜单选中当前页（防止刷新导航active丢失）
            if (this.$route.path !== '/main') {
                this.defaultActive = this.$route.path;
            }
        }
    }
</script>

<style lang="scss" scoped>
    #main {
        position:absolute;
        width:1360px;
        height:457px;
        MARGIN-RIGHT:auto;
        MARGIN-LEFT:auto;
    }
    el-menu-item {
        color:#285A63;
    }
    .div-container {
        margin:0px 180px;
    }
    .menu-bottom {
        margin: 35px -5px;
        background-color: rgba(180, 222, 241, 0.44);
        background-image: linear-gradient(120deg, #c2e9fb 0%, #a1c4fd 100%);
        // 边框
        border: solid 1px rgba(250, 255, 254, 0);
        // 边角弧度
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 2px 2px 5px #333333;
        -webkit-box-shadow:2px 2px 5px #333333;
        box-shadow: 7px 15px 30px #285a63;
        // 延迟过度
        -moz-box-sizing: border-box;  // Firefox
        -webkit-box-sizing: border-box;
        -o-box-sizing:border-box;  // Opera
        transition: all 0.3s linear;  // 0.3s过渡时间
        -moz-transition: all 0.3s linear;  // Firefox 4
        -webkit-transition: all 0.3s linear;  // Safari 和 Chrome
    }
    .el-menu-demo {
        height: 60px;
        width: 100%;
        background-color: rgb(180, 222, 241);
    }
    .el-header {
        background-color: rgb(180, 222, 241);
        margin: 0px -20px;
        border-radius: 10px;
    }
    .login-logout {
        position: absolute;
        top: 20px;
        right: 240px;
        font-size: 15px;
    }
    .logout {
        margin-left: 10px;
        margin-top:-5px;
    }
</style>
