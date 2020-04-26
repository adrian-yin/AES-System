<template>
    <div id="main">
        <div class="el-row1">
            <el-row :gutter="120">
                <el-col :span="12">
                    <span class="article-title">题目：{{ articleTitle }}</span>
                </el-col>
                <el-col :span="6" :offset="3">
                    <span class="total-score">总得分：{{ totalScore }}/100</span>
                </el-col>
            </el-row>
        </div>
        <div class="el-row2">
            <el-row :gutter="30">
                <el-col :span="12">
                    <div class="pie-title">
            <h4><span class="vocabularyWords">词汇分布</span></h4>
                    </div>
                    <hr style="margin:-20px 30px -100px 100px" />
                    <div id="vocabularyPie" style="width:100%; height:400px; padding-left:40px">
                        <!-- 此处为词汇分布饼状图 -->
                    </div>
                </el-col>
                <el-col :span="12">
                    <div class="score-title">
                        <h4>分项得分</h4>
                    </div>
                    <hr style="margin:-20px 95px 50px 70px" />
                    <div class="score-content">
                        <div class="each-score-content">
                            <span class="each-score-title">词汇水平</span>
                            <el-rate
                                v-model="vocabularyLevel"
                                disabled
                                show-score
                                text-color="ffba00"
                                score-template="{value}">
                            </el-rate>
                        </div>
                        <div class="each-score-content">
                            <span class="each-score-title">切题程度</span>
                            <el-rate
                                v-model="titleRelativity"
                                disabled
                                show-score
                                text-color="ffba00"
                                score-template="{value}">
                            </el-rate>
                        </div>
                        <div class="each-score-content">
                            <span class="each-score-title">句型难度</span>
                            <el-rate
                                v-model="sentenceDifficulty"
                                disabled
                                show-score
                                text-color="ffba00"
                                score-template="{value}">
                            </el-rate>
                        </div>
                    </div>
                </el-col>
            </el-row>
        </div>
        <el-row class="el-row3">
            <el-col :span="24">
                <div class="block-title">
                    <h4>全文点评</h4>
                </div>
                <hr style="margin:-25px 100px 15px 100px;"/>
                <div class="comment-block">
                    <el-menu
                        :default-active="activeIndex"
                        mode="horizontal"
                        class="el-menu-demo"
                        >
                            <el-menu-item index="1" @click="setArticleComment">原文点评</el-menu-item>
                            <el-menu-item index="2" @click="setSuggestion">提升建议</el-menu-item>
                            <el-menu-item index="3" @click="setVocabularyDevelopment">词汇拓展</el-menu-item>
                    </el-menu>
                    <el-card class="box-card">
                        <div class="text">
                            {{ cardContent }}
                        </div>
                    </el-card>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import https from '../api/https.js'
    import echarts from 'echarts'

    export default {
        data () {
            return {
                cardContent: '',
                activeIndex: '1',
                articleTitle: '',
                articleContent: '',
                totalScore: 0,
                vocabularyLevel: 0,
                titleRelativity: 0,
                sentenceDifficulty: 0,
                articleComment: '',
                suggestion: '',
                vocabularyDevelopment: '',
                hsk1: 0,
                hsk2: 0,
                hsk3: 0,
                hsk4: 0,
                hsk5: 0,
                hsk6: 0
            }
        },
        methods: {
            // 设置卡片内容
            setArticleComment () {
                this.cardContent = this.articleComment;
            },
            setSuggestion () {
                this.cardContent = this.suggestion;
            },
            setVocabularyDevelopment () {
                this.cardContent = this.vocabularyDevelopment;
            },
            // 绘制词汇分布饼状图
            drawVocabularyPie () {
                var myChart = echarts.init(document.getElementById('vocabularyPie'));
                var option = {
                    title: {},
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a} <br/>{b} : {c} ({d}%)'
                    },
                    series: [
                        {
                            name: '词汇类别',
                            type: 'pie',
                            radius: '40%',
                            center: ['50%', '57%'],
                            data: [
                                {value: this.hsk1, name: 'HSK一级', label: {fontWeight: 'bold'}},
                                {value: this.hsk2, name: 'HSK二级', label: {fontWeight: 'bold'}},
                                {value: this.hsk3, name: 'HSK三级', label: {fontWeight: 'bold'}},
                                {value: this.hsk4, name: 'HSK四级', label: {fontWeight: 'bold'}},
                                {value: this.hsk5, name: 'HSK五级', label: {fontWeight: 'bold'}},
                                {value: this.hsk6, name: 'HSK六级', label: {fontWeight: 'bold'}}
                            ],
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                };
                myChart.setOption(option);
            },
            // 在整数后加'.0'
            formatInt (val) {
                var xsd = val.toString().split('.');
                if (xsd.length === 1) {
                    val = val.toString() + '.0';
                    return val;
                }
                return val;
            }
        },
        mounted () {
            https.fetchGet('record/' + this.$route.query.recordId).then((res) => {
                if (res.data['code'] === 200) {
                    this.articleTitle = res.data['articleTitle'];
                    this.articleContent = res.data['articleContent'];
                    this.totalScore = res.data['totalScore'];
                    this.vocabularyLevel = res.data['vocabularyLevel'];
                    this.titleRelativity = res.data['titleRelativity'];
                    this.sentenceDifficulty = res.data['sentenceDifficulty'];
                    this.articleComment = res.data['articleComment'];
                    this.suggestion = res.data['suggestion'];
                    this.vocabularyDevelopment = res.data['vocabularyDevelopment'];
                    this.hsk1 = res.data['hsk1'];
                    this.hsk2 = res.data['hsk2'];
                    this.hsk3 = res.data['hsk3'];
                    this.hsk4 = res.data['hsk4'];
                    this.hsk5 = res.data['hsk5'];
                    this.hsk6 = res.data['hsk6'];
                    // 初始化评价内容
                    this.cardContent = this.articleComment;

                    // 在整数后加'.0'格式化成一位小数
                    this.totalScore = this.formatInt(this.totalScore);
                    this.vocabularyLevel = this.formatInt(this.vocabularyLevel);
                    this.titleRelativity = this.formatInt(this.titleRelativity);
                    this.sentenceDifficulty = this.formatInt(this.sentenceDifficulty);

                    // 绘制图表
                    this.drawVocabularyPie();
                    return true;
                } else {
                    return false;
                }
            });
        }
    }
</script>

<style lang="scss" scoped>
    #main{
        width: 1300px;
        height: 457px;
        MARGIN-RIGHT: auto;
        MARGIN-LEFT: auto;
    }
    .el-row1{
        margin: 10px 120px;
        padding-top: 20px;
        height: 3em;
        border: 5px solid #91b8ce;
        border-radius: 10px;
    }
    .el-row2 {
        margin: 25px 120px;
        border: 5px solid #91b8ce;
        border-radius: 10px;
    }
    .each-score-title {
        float: left;
        position: relative;
        font-size: 15px;
        // font-weight:bold;
        left: 20%;
        background-color: rgba(255, 208, 99, 0.98);
          // 边框
        // border: solid 1px rgba(102, 146, 191, 0.68);
        // 边角弧度
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 1px 1px 1px #e6c077;
        -webkit-box-shadow: 1px 1px 1px #ffb9a5;
        box-shadow: 5px 10px 10px #ffd063;
    }
    .each-score-content {
        margin-bottom: 50px;
        margin-right: -10px;
    }
    .pie-title{
        text-align: left;
        margin-left: 145px;
    }
    .score-title{
        color: #475164;
        text-align: left;
        margin-left: 120px;
        font-size: 18px;
    }
    .block-title {
        text-align: left;
        margin: 25px 150px;
        color: #475164;
    }
    .el-row3 {
        margin: 30px 120px;
        border: 5px solid #91b8ce;
        border-radius: 10px;
    }
    .el-menu-demo {
        height: 40px;
        width: 100%;
        background-color: rgb(255, 255, 255);
    }
    .comment-block {
        width: 80%;
        margin: 10px auto 10px auto;
    }
    .box-card {
        margin: 50px auto 10px auto;
        height: 300px;
    }
    .block-title{
        font-size: 30px;
        font-weight: bold;
    }
    .article-title{
        font-size: 20px;
        font-weight: bold;
        color: #475164;
        background-color: rgba(134, 226, 251, 0.98);
        // 边框
        // border: solid 1px rgba(102, 146, 191, 0.68);
        // 边角弧度
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 1px 1px 1px #59bbbb;
        -webkit-box-shadow: 1px 1px 1px #bcfcff;
        box-shadow: -10px -5px 10px #86e2fb;
    }
    .total-score{
        font-size: 20px;
        font-weight: bold;
        background-color: rgba(134, 226, 251, 0.98);
          // 边框
        // border: solid 1px rgba(102, 146, 191, 0.68);
        // 边角弧度
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 1px 1px 1px #59bbbb;
        -webkit-box-shadow: 1px 1px 1px #bcfcff;
        box-shadow: -10px -5px 10px #86e2fb;
    }
    // .text {}
</style>
