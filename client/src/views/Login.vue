<template>
    <div>
        <el-form ref="loginForm" :model="form" :rules="rules" label-width="0" class="login-box">
            <h3 class="login-title">登录</h3>
            <el-form-item prop="userid">
                <el-input type="text" placeholder="用户名/邮箱" v-model="form.userid"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input type="password" placeholder="密码" v-model="form.password"></el-input>
            </el-form-item>
            <div class="under-input">
                <el-checkbox v-model="form.remember" class="remember-checkbox">记住我</el-checkbox>
                <el-link type="primary" href="/#/register" class="register-button">注册</el-link>
            </div>
            <el-form-item class="login-button">
                <el-button type="primary" @click="onSubmit('loginForm')">登录</el-button>
            </el-form-item>
        </el-form>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width=30%>
            <span>请输入帐号和密码</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible = false">确定</el-button>
            </span>
        </el-dialog>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible1"
            width=30%>
            <span>帐号或密码错误</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible1 = false">确定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import https from '../api/https.js'
    import CryptoJS from 'crypto-js'

    // 十六位十六进制数作为密钥
    const key = CryptoJS.enc.Utf8.parse('13579BDFFDB97531');
    // 十六位十六进制数作为偏移量
    const iv = CryptoJS.enc.Utf8.parse('02468ACEECA86420');

    export default {
        name: 'Login',
        data () {
            return {
                form: {
                    userid: '',
                    password: '',
                    remember: false
                },
                rules: {
                    userid: [
                        {required: true, message: '用户名/邮箱不能为空', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不能为空', trigger: 'blur'}
                    ]
                },
                dialogVisible: false,
                dialogVisible1: false
            }
        },
        created () {
            // 载入cookie
            let userid = this.getCookie('userid');
            let password = this.decrypt(this.getCookie('password'));
            // 如果存在cookie则填入信息并勾选记住我
            if (userid) {
                this.form.userid = userid;
                this.form.password = password;
                this.form.remember = true;
            }

            let that = this;
            // 实现回车键登陆
            document.onkeydown = function (e) {
                e = window.event || e;
                // 确保在登录页面且按下的键是回车
                if (that.$route.path === '/login' && (e.code === 'Enter' || e.code === 'Num Enter')) {
                    that.onSubmit('loginForm');
                }
            }
        },
        methods: {
            onSubmit (formName) {
                this.$refs[formName].validate((valid) => {
                    var userid = this.form['userid'];
                    var pwd = this.form['password'];
                    var loginInfo = {'userid': userid, 'password': pwd};

                    if (valid) {
                        https.fetchPost('login', loginInfo).then((res) => {
                            if (res.data['code'] === 200) {
                                this.$store.commit('set_token', res.data['token']);
                                // sessionStorage中也存取token，解决刷新token丢失问题
                                sessionStorage.setItem('token', res.data['token']);
                                // 存储用户信息
                                this.setUserInfo();
                                this.$router.push('/main');
                                return true;
                            } else {
                                this.dialogVisible1 = true;
                                return false;
                            }
                        });
                    } else {
                        this.dialogVisible = true;
                        return false;
                    }
                });
            },
            // 保存cookie方法
            setCookie (cName, value, expiredays) {
                var exdate = new Date();
                // 有效时间为当前时间加天数
                exdate.setDate(exdate.getTime() + expiredays);
                document.cookie = cName + '=' + value + ((expiredays == null) ? '' : ';expires=' + exdate.toGMTString());
            },
            // 读取cookie方法
            getCookie (key) {
                if (document.cookie.length > 0) {
                    var start = document.cookie.indexOf(key + '=');
                    if (start !== -1) {
                        start = start + key.length + 1;
                        var end = document.cookie.indexOf(';', start);
                        if (end === -1) {
                            end = document.cookie.length;
                        }
                        return unescape(document.cookie.substring(start, end));
                    }
                }
                return '';
            },
            // 存储用户信息到cookie
            setUserInfo () {
                // 通过是否勾选记住我判断存储cookie还是清空cookie
                if (this.form.remember) {
                    this.setCookie('userid', this.form.userid, 7);
                    // 使用Crypto加密密码
                    let pwd = this.encrypt(this.form.password);
                    this.setCookie('password', pwd, 7);
                } else {
                    this.setCookie('userid', '', null);
                    this.setCookie('password', '', null);
                }
            },
            // Crypto解密方法
            decrypt (word) {
                let encryptedHexStr = CryptoJS.enc.Hex.parse(word);
                let srcs = CryptoJS.enc.Base64.stringify(encryptedHexStr);
                let decrypt = CryptoJS.AES.decrypt(srcs, key, { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
                let decryptedStr = decrypt.toString(CryptoJS.enc.Utf8);
                return decryptedStr.toString();
            },
            // Crypto加密方法
            encrypt (word) {
                let srcs = CryptoJS.enc.Utf8.parse(word);
                let encrypted = CryptoJS.AES.encrypt(srcs, key, { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
                return encrypted.ciphertext.toString().toUpperCase();
            }
        }
    }
</script>

<style lang="scss" scoped>
    .login-button {
        text-align: center;
    }
    .login-box {
        border: 1px solid #DCDFE6;
        width: 350px;
        margin: 180px auto;
        padding: 30px 35px 5px 35px;
        border-radius: 5px;
        -webkit-border-radius: 5px;
        box-shadow: 0 0 25px #909399;
    }
    .login-title {
        text-align: center;
        margin: 0 auto 20px auto;
        color: #303133;
    }
    .under-input {
        position: relative;
        margin: 0 0 15px 0;
        height: 15px;
    }
    .remember-checkbox {
        position: absolute;
        left: 0;
    }
    .register-button {
        position: absolute;
        right: 0;
    }
</style>
