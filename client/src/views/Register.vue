<template>
    <div class="register-container">
        <el-form ref="registerForm" :model="form" status-icon :rules="rules" label-width="0" class="register-box">
            <h3 class="register-title">注册</h3>
            <el-form-item prop="email">
                <el-input type="text" placeholder="请填写邮箱地址" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item prop="verificationCode">
                <el-input type="text" placeholder="请输入验证码" v-model="form.verificationCode" style="width: 60%; float:left"></el-input>
                <el-button icon="el-icon-mobile-phone" @click="send" style="width: 35%" type="success" :disabled="disabled=!show">
                    <span v-show="show">获取验证码</span>
                     <span v-show="!show" class="count">{{count}} s</span>
                </el-button>
            </el-form-item>
            <el-form-item prop="username">
                <el-input type="text" placeholder="请设置用户名" v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input type="password" placeholder="密码" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item prop="confirmPassword">
                <el-input type="password" placeholder="确认密码" v-model="form.confirmPassword"></el-input>
            </el-form-item>
            <el-form-item prop="name">
                <el-input type="text" placeholder="昵称" v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button class="return-button" @click="backToLogin">返回登录</el-button>
                <el-button type="primary" class="register-button" @click="onSubmit('registerForm')">注册</el-button>
            </el-form-item>
        </el-form>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width=30%>
            <span>输入信息不正确</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible = false">确定</el-button>
            </span>
        </el-dialog>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible1"
            width=30%>
            <span>用户名已被注册</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible1 = false">确定</el-button>
            </span>
        </el-dialog>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible2"
            width=30%>
            <span>邮箱已被注册</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible2 = false">确定</el-button>
                <el-button type="primary" @click="backToLogin">返回登录</el-button>
            </span>
        </el-dialog>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible3"
            width=30%
            @close="backToLogin">
            <span>{{ countMessage }}</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="backToLogin">立即返回</el-button>
            </span>
        </el-dialog>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible4"
            width=30%>
            <span>验证码不正确</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible4 = false">确定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import https from '../api/https.js';
    const TIME_COUNT = 60; // 更改倒计时时间

    export default {
        name: 'Register',
        data () {
            // 修改密码后重新调用确认密码验证
            var validatePassword = (rule, value, callback) => {
                if (this.form.confirmPassword !== '') {
                    this.$refs.registerForm.validateField('confirmPassword');
                }
                callback();
            };
            // 判断确认密码与原密码是否一致的方法
            var validateConfirmPassword = (rule, value, callback) => {
                if (value !== this.form.password) {
                    callback(new Error('两次输入的密码不一致'));
                } else {
                    callback();
                }
            };
            return {
                show: true, // 初始启用按钮
                count: '', // 初始化次数
                timer: null,
                form: {
                    email: '',
                    username: '',
                    password: '',
                    confirmPassword: '',
                    name: '',
                    verificationCode: ''
                },
                dialogVisible: false,
                dialogVisible1: false,
                dialogVisible2: false,
                dialogVisible3: false,
                dialogVisible4: false,
                countMessage: '',
                interval: null,
                rules: {
                    email: [
                        {required: true, message: '请输入邮箱地址', trigger: 'blur'},
                        {type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur'}
                    ],
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'},
                        {min: 0, max: 20, message: '用户名的长度不得超过20个字符', trigger: ['blur', 'change']}
                    ],
                    password: [
                        {required: true, message: '请输入密码', trigger: 'blur'},
                        {min: 8, max: 15, message: '密码长度为8～15位', trigger: 'blur'},
                        {validator: validatePassword, trigger: 'blur'}
                    ],
                    confirmPassword: [
                        {required: true, message: '请输入确认密码', trigger: 'blur'},
                        {validator: validateConfirmPassword, trigger: 'blur'}
                    ],
                    name: [
                        {min: 0, max: 20, message: '昵称长度过长', trigger: ['blur', 'change']}
                    ],
                    verificationCode: [
                        {required: true, message: '请输入验证码', trigger: 'blur'}
                    ]
                }
            }
        },
        methods: {
            onSubmit (formName) {
                var email = this.form['email'];
                var username = this.form['username'];
                var password = this.form['password'];
                var name = this.form['name'];
                var verificationCode = this.form['verificationCode'];
                var registerInfo = {
                    'email': email,
                    'username': username,
                    'password': password,
                    'name': name,
                    'verificationCode': verificationCode
                    };

                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        https.fetchPost('register', registerInfo).then((res) => {
                            if (res.data['code'] === 200) {
                                // 倒计时5秒返回登录
                                let that = this;
                                let count = 5;
                                this.interval = window.setInterval(() => {
                                    that.countMessage = '注册成功！' + count + '秒后返回登录';
                                    if (that.dialogVisible3 === false) {
                                        this.dialogVisible3 = true;
                                    }
                                    count--;
                                    if (count < 0) {
                                        window.clearInterval(that.interval);
                                        this.$router.push('/login');
                                    }
                                }, 1000);
                                return true;
                            } else {
                                // 邮箱已被注册显示dialog2
                                if (res.data['wrongType'] === 'email') {
                                    this.dialogVisible2 = true;
                                    return false;
                                // 用户名已被注册显示dialog1
                                } else if (res.data['wrongType'] === 'username') {
                                    this.dialogVisible1 = true;
                                    return false;
                                // 验证码不正确显示dialog4
                                } else if (res.data['wrongType'] === 'verificationCode') {
                                    this.dialogVisible4 = true;
                                    return false;
                                }
                            }
                        });
                    } else {
                        this.dialogVisible = true;
                        return false;
                    }
                });
            },
            backToLogin () {
                // 清空倒计时返回
                if (this.interval) {
                    window.clearInterval(this.interval);
                }
                this.$router.push('/login');
            },
            send () {
                if (!this.timer) {
                    this.count = TIME_COUNT;
                    this.show = false;
                    this.timer = setInterval(() => {
                        if (this.count > 0 && this.count <= TIME_COUNT) {
                            this.count--;
                        } else {
                            this.show = true;
                            clearInterval(this.timer); // 清除定时器
                            this.timer = null;
                        }
                    }, 1000)
                }
                https.fetchPost('confirm', {'email': this.form['email']}).then((res) => {
                    if (res.data['code'] === 200) {
                        return true;
                    } else {
                        if (res.data['wrongType'] === 'email') {
                                this.dialogVisible2 = true;
                        }
                        return false;
                    }
                })
            }
        }
    }
</script>

<style lang="scss" scoped>
    .register-container {
        width: 100%;
        height: 100%;
        background: url(../assets/c.png) center center no-repeat;
        background-size: 100% 100%;
        position: fixed;
        background-attachment: fixed;
        overflow: hidden;
        overflow: auto;
        z-index: -1;
        margin-top: -30px;
    }
    .register-box {
        border: 1px solid #DCDFE6;
        width: 350px;
        margin: 150px auto;
        padding: 30px 35px 40px 35px;
        border-radius: 5px;
        -webkit-border-radius: 5px;
        box-shadow: 0 0 25px #909399;
    }
    .register-title {
        text-align: center;
        margin: 0 auto 20px auto;
        color: #303133;
    }
    .return-button {
        position: absolute;
        left: 10px;
    }
    .register-button {
        position: absolute;
        right: 10px;
    }
</style>
