<template>
    <el-main>
        <el-col :span="18">
            <div class="block">
                <p class="norecord-text" v-if="noRecords">您还没有评分记录。</p>
                <el-timeline :reverse="reverse">
                    <el-timeline-item
                        v-for="(record, index) in records"
                        :key="index"
                        :timestamp="record.commitTime"
                        placement="top">
                        <el-card class="card-box">
                            <span class="article-title">题目：{{ record.articleTitle }}</span>
                            <span class="total-score">得分：{{ record.totalScore }}</span>
                            <p class="article-content">{{ record.articleContent }}</p>
                            <el-link type="primary" @click="toRecord(record.recordId)" class="more-button">更多</el-link>
                        </el-card>
                    </el-timeline-item>
                </el-timeline>
            </div>
        </el-col>
        <el-col :span="6">
            <div class="calculate-box">
                <div class="calculate-item">
                    <div class="words" style="font-family: 'Adobe 楷体 Std R';color:#337afb">当前使用</div>
                    <div class="circle">{{ count }}</div>
                    <div style="margin-top:45px;font-family: 'Adobe 楷体 Std R';color:#337afb">次</div>
                </div>
                <div class="calculate-item">
                    <div class="words" style="font-family: 'Adobe 楷体 Std R';color:#337afb">当前最高</div>
                    <div class="circle">{{ maxScore }}</div>
                    <div style="margin-top:45px;font-family: 'Adobe 楷体 Std R';color:#337afb">分</div>
                </div>
            </div>
        </el-col>
    </el-main>
</template>

<script>
    import https from '../api/https.js'

    export default {
        data () {
            return {
                records: [],
                noRecords: false,
                // 时间线倒序显示
                reverse: true,
                count: 0,
                maxScore: 0
            }
        },
        mounted () {
            https.fetchGet('records').then((res) => {
                if (res.data['code'] === 200) {
                    if (res.data['records'].length !== 0) {
                        this.records = res.data['records'];
                        // 统计数目
                        this.count = this.records.length;
                        // 计算最高分
                        this.maxScore = this.getMaxScore();
                        // 格式化日期
                        this.dateToString();
                    } else {
                        this.noRecords = true;
                    }
                    return true;
                } else {
                    return false;
                }
            })
        },
        methods: {
            toRecord (recordId) {
                // 跳转到结果界面，并传递记录id
                this.$router.push({path: '/result', query: {recordId: recordId}});
            },
            // 获取最高分
            getMaxScore () {
                var maxScore = 0;
                for (let index in this.records) {
                    if (this.records[index].totalScore > maxScore) {
                        maxScore = this.records[index].totalScore;
                    }
                }
                return maxScore;
            },
            // 格式化日期
            dateToString () {
                for (let index in this.records) {
                    var da = new Date(this.records[index].commitTime);
                    this.records[index].commitTime = da.getFullYear() + '-' + (da.getMonth() + 1) + '-' + da.getDate() + ' ' + da.getHours() + ':' + da.getMinutes() + ':' + da.getSeconds();
                }
            }
        }
    }
</script>

<style lang="scss" scoped>
    .article-title{
        font-size: 21px;
        color: #475164;
        background-color: rgba(182, 208, 251, 0.98);
        // 边框
        // border: solid 1px rgba(102, 146, 191, 0.68);
        // 边角弧度
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 1px 1px 1px #59bbbb;
        -webkit-box-shadow: 1px 1px 1px #bcfcff;
        box-shadow: 5px -3px 10px #b6d0fb;
    }
    .block {
        text-align: left;
    }
    .card-box {
        // 边角弧度*/
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 2px 2px 5px #333333;
        -webkit-box-shadow: 2px 2px 5px #333333;
        box-shadow: 7px 15px 30px #285a63;
        background: ghostwhite;
        height: 200px;
    }
    .article-content {
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
    }
    .more-button {
        position: absolute;
        bottom: 20px;
        left: 50px;
    }
    .article-title {
        font-size: 21px;
        font-weight: bold;
        margin-top: 30px;
    }
    .total-score {
        font-size: 21px;
        font-weight: bold;
        color: #ff724c;
        position: absolute;
        right: 50px;
        background-color: rgba(253, 232, 213, 0.98);
          // 边框
        // border: solid 1px rgba(102, 146, 191, 0.68);
        // 边角弧度
        border-radius: 10px;
        // 阴影
        -moz-box-shadow: 1px 1px 1px #59bbbb;
        -webkit-box-shadow: 1px 1px 1px #bcfcff;
        box-shadow: 5px 10px 10px #fde8d5;
    }
    .calculate-box {
        text-align: center;
        margin-top: 10px;
    }
    .calculate-item {
        margin-bottom: 120px;
        font-size: 20px;
        font-weight: bold;
    }
    .circle {
        width: 80px;
        height: 80px;
        border: 8px solid rgb(255, 255, 255);
        text-align: center;
        line-height: 80px;
        font-size: 40px;
        font-weight: bold;
        border-radius: 50%;  // 圆角百分比
        float: left;
        margin-left: 90px;
        margin-top: 20px;
        margin-right: -10px;
        color: #ff9900;
    }
    .norecord-text {
        font-size: 25px;
        font-weight: bold;
    }
</style>
