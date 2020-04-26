<template>
    <el-main v-loading="loading" element-loading-text="正在计算得分" element-loading-background="rgba(255, 255, 255, 0.7)">
        <el-form
        ref="newForm"
        :model="form"
        label-width="80px"
        :rules="rules"
        label-position="top"
        class="new-box">
            <el-form-item prop="title" label="题目：">
                <el-input type="text" v-model="form.title" class="title-input"></el-input>
            </el-form-item>
            <el-form-item prop="article" label="请输入正文：">
                <el-input type="textarea" v-model="form.article" :rows="18" class="article-input" @input="countChar"></el-input>
            </el-form-item>
            <el-form-item>
                <span class="count-corner">字数：{{ count }}</span>
                <el-button type="primary" size="medium" class="new-button" @click="onSubmit('newForm')">提交</el-button>
            </el-form-item>
        </el-form>

        <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width=30%>
            <span>题目或文章格式不正确</span>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" @click="dialogVisible = false">确定</el-button>
            </span>
        </el-dialog>
    </el-main>
</template>

<script>
    import https from '../api/https.js';

    export default {
        name: 'New',
        data () {
            return {
                form: {
                    title: '',
                    article: ''
                },
                // 控制加载图形的显示
                loading: false,
                count: 0,
                dialogVisible: false,
                rules: {
                    title: [
                        {required: true, message: '题目不能为空', trigger: 'blur'},
                        {min: 0, max: 30, message: '题目长度过长', trigger: ['blur', 'change']}
                    ],
                    article: [
                        {required: true, message: '文章不能为空', trigger: 'blur'},
                        {min: 0, max: 1500, message: '文章长度过长', trigger: ['blur', 'change']}
                    ]
                }
            }
        },
        methods: {
            onSubmit (formName) {
                var title = this.form.title;
                var article = this.form.article;
                var newInfo = {'title': title, 'article': article};

                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.loading = true;
                        https.fetchPost('records', newInfo).then((res) => {
                            if (res.data['code'] === 200) {
                                this.loading = false;
                                // 跳转到结果界面，并传递记录id
                                this.$router.push({path: '/result', query: {recordId: res.data['recordId']}});
                                return true;
                            } else {
                                return false;
                            }
                        })
                    } else {
                        this.dialogVisible = true;
                        return false;
                    }
                });
            },
            // 统计文章中汉字字数
            countChar () {
                // 检测中文字符正则
                var re = /[\u4E00-\u9FA5]/g;
                if (this.form.article.match(re)) {
                    this.count = this.form.article.match(re).length;
                } else {
                    this.count = 0;
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    .new-box {
        text-align: left;
    }
    .count-corner {
        margin-left: 30px;
    }
    .new-button {
        position: absolute;
        right: 40px;
    }
    .title-input {
        width: 500px;
        margin-left: 25px;
    }
    .article-input {
        width: 900px;
        margin-left: 25px;
    }
</style>
