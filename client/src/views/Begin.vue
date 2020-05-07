<template>
    <div class="img" :style="{backgroundImage: 'url(' + img + ')'}">
        <el-button type="primary" size="large" class="new-button" @click="gotolink">从这里开始</el-button>
    </div>
</template>

<script>
    import Img from '../assets/background.png'
    export default {
        name: 'Begin',
        data () {
            return {
                img: Img
            }
        },
        methods: {
            gotolink () {
                this.$router.push('/login')
            }
        }
    }
</script>

<style lang="scss" scoped>
    .new-button {
        position: absolute;
        right: 950px;
        top: 450px;
        width: 300px;
        height: 100px;
        font-size: 50px;
        // 阴影
        -moz-box-shadow: 2px 2px 5px #99eefb;
        -webkit-box-shadow: 2px 2px 5px #333333;
        box-shadow: 7px 15px 30px #285a63;
        // 延迟过度
        -moz-box-sizing: border-box; // Firefox
        -webkit-box-sizing: border-box;
        -o-box-sizing: border-box; // Opera
        transition: all 0.3s linear; // 0.3s过渡时间
        -moz-transition: all 0.3s linear; // Firefox 4
        -webkit-transition: all 0.3s linear; // Safari 和 Chrome
    }
    .img {
        width: 100%;
        height: 100%;
        background: url('../assets/background.png') center center no-repeat;
        background-size: 100% 100%;
        position: fixed;
        background-attachment: fixed;
        overflow: hidden;
        overflow: auto;
        z-index: -1;
        margin-top: -30px;
    }
</style>
