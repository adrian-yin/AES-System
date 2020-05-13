<template>
    <div class="container">
        <div v-for="itemOne in WrongVocabulary" :key="itemOne.id">
		        <div v-for="item in itemOne.problem_list" :key="item.id" class="each-error-shell-div">
                <div
                    class="error-content-info"
                    v-if="show_id==item.id"
                    @click="clickDetailDiv(item.id)"
                >
                    <div class="error-content" v-html="item.token_strs">{{item.token_strs}}</div>
                    <div class="word-revise-div">
                        <div class="ErrorWordContent fsReJu">
                            <span class="originWordText ntLBp">你写的</span>
                            <span
                                class="unfixed Checkstyle__ErrorWord-an9z37-43 gKCJOw"
                                style="font-size: 30px;"
                            >{{item.origin_text}}</span>
                        </div>
                        <i class="el-icon-right right-icon-1"></i>
                        <div class="Checkstyle__CorrectWordContent-an9z37-40 ehNdGM">
                            <span class="Checkstyle__SmallWordTip-an9z37-41 ntLBp">修改建议</span>
                            <span
                                class="unfixed Checkstyle__CorrectWord-an9z37-44 eUmdmJ"
                                style="font-size: 30px;"
                            >{{item.correct_text}}</span>
                        </div>
			                  <div class="explaination">
                            <span class="meaning">意思：<span>{{meanning}}</span></span><br />
                            <span class="example">例句：<span>{{example_sentence}}</span></span>
				                </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    import {stringify} from "querystring";
    import https from '../api/https.js';
    export default {
        name: 'Vocabulary',
        data () {
            return {
                editorOption: {
                    // quill文本框配置项
                    theme: "snow",
                    readOnly: true,
                    placeholder: "",
                    modules: {
                        toolbar: false
                    }
                },
                quillA: null,
                voproblem_detail: [],
                WrongVocabulary: [],
                problem: [],
                show_id: null,
                showOneType: true,
                currentType: null,
                typeData: [],
                meaning,
                example_sentence,
                localStorage_getItem_user_id: false
            };
        },
        // 挂载前
        beforeMount() {
            if (localStorage.getItem("user_id") == null || localStorage.getItem("user_id") == 0) {
                this.localStorage_getItem_user_id = false;
            } else {
                this.localStorage_getItem_user_id = true;
            }
        },
        // 挂载完成
        mounted () {
            document.getElementById("app").style.minHeight = 0;
            document.getElementById("app").style.height = "100%";
            this.quillA = this.$refs.quillEditorA.quill;
        },
        methods: {
            addElementEvent () {
                for (var i = 0; i < this.voproblem_detail.length; i++) {
                    var dom = document.getElementById(this.voproblem_detail[i].id);
                    var _this = this;
                    dom.onmouseenter = function (e) {
                        var name = "c" + e.target.id;
                        if (document.getElementsByName(name)[0] != null) {
                            if (e.target.id != _this.show_id) {
                                document
                                    .getElementsByName(name)[0]
                                    .scrollIntoView({behavior: "smooth", inline: "nearest"});
                                // console.log(document.getElementsByName(name)[0].parentNode.parentNode)
                                document
                                    .getElementsByName(name)[0]
                                    .parentNode.parentNode.setAttribute("class", "left-mouseenter");
                                console.log(e.currentTarget.className);

                                if (e.currentTarget.className == "correct-text-class") {
                                } else if (e.currentTarget.className == "origin-text-class") {
                                    document.getElementsByName(name)[0].style.color = "rgb(238, 113, 153)";
                                    document.getElementsByName(name)[0].parentNode.previousElementSibling.style.backgroundColor = "rgb(238, 113, 153)";
                                } else {
                                }
                            } else {
                            }
                        }
                    };
                    dom.onmouseleave = function (e) {
                        var name = "c" + e.target.id;
                        if (document.getElementsByName(name)[0] != null) {
                            document
                                .getElementsByName(name)[0]
                                .parentNode.parentNode.setAttribute(
                                    "class",
                                    "error-origin-content"
                                );
                            if (e.currentTarget.className == "correct-text-class") {
                            } else if (e.currentTarget.className == "origin-text-class") {
                                document.getElementsByName(name)[0].style.color = "";
                                document.getElementsByName(
                                    name
                                )[0].parentNode.previousElementSibling.style.backgroundColor = "";
                            } else {
                            }
                        }
                    };
                    dom.onclick = function (e) {
                        var id = e.target.id;
                        var click_left = "c" + id;
                        if (id != _this.show_id) {
                            if (_this.show_id != null) {
                                // 将之前修改的类名修复
                                var showIdDom = document.getElementById(_this.show_id);
                                var className = showIdDom.className.replace("-hover", "");
                                showIdDom.setAttribute("class", className);
                                console.log(className);
                            }
                            if (_this.currentType == null) {
                                // _this.show_id=id
                                _this.showCorrectDetail(id);
                            } else {
                                var problemList = _this.showProblem[0].problem_list;
                                var bool = false;
                                for (var i = 0; i < problemList.length; i++) {
                                    if (id == problemList[i].id) {
                                        bool = true;
                                        break;
                                    }
                                }
                                if (bool) {
                                    //  _this.show_id=id
                                    _this.showCorrectDetail(id);
                                } else {
                                    _this.showProblem = _this.problem;
                                    _this.currentType = null;
                                    name = "c" + id;
                                    // console.log(document.getElementsByName(name))
                                    _this.$nextTick(function() {
                                        // dom已更新
                                        // console.log(document.getElementsByName(click_left)[0])
                                        document
                                            .getElementsByName(name)[0]
                                            .scrollIntoView({ behavior: "smooth", inline: "nearest" });
                                        // _this.show_id=id
                                        _this.showCorrectDetail(id);
                                    });
                                }
                            }
                        }
                    };
                }
            },
            testAmend () {
                this.quillA.updateContents(this.data, "api");
            },
            clickDetailDiv (id) {
                this.show_id = null;
            },
            getShowProblem () {
                if (this.currentType == null) {
                    this.showProblem = this.problem;
                } else {
                    for (var i = 0; i < this.problem.length; i++) {
                        if (this.problem[i].problem_type == this.currentType) {
                            var problemList = [];
                            problemList.push(this.problem[i]);
                            this.showProblem = problemList;
                            break;
                        }
                    }
                }
            }
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .container {
        background-color: #f9f9fb;
        min-width: 600px;
        overflow-x: hidden;
        text-align: center;
        margin: 0 auto;
        width: 70%;
        display: flex;
        // flex: 1;
        min-height: 100%;
        // justify-content: center;
}
.error-content-info {
    background-color: rgb(255, 255, 255);
    box-shadow: rgba(191, 204, 230, 0.75) 0px 10px 30px;
    padding: 30px 30px 15px;
    text-align: center;
    margin: 0 auto;
    overflow: hidden;
    border-radius: 5px;
    margin: 10px 50px;
    width: 700px;
    }
.error-content {
    white-space: pre-wrap;
    line-height: 20px;
    font-size: 16px;
    color: rgb(132, 140, 163);
    cursor: pointer;
    text-align: left;
}
.fsReJu {
    min-width: 40px;
}
.ntLBp {
    display: block;
    height: 18px;
    font-size: 13px;
    line-height: 18px;
    color: rgb(178, 184, 201);
    margin-bottom: 8px;
}
.gKCJOw {
    white-space: pre-wrap;
    font-size: 30px;
    line-height: 33px;
    color: rgb(84, 89, 101);
    position: relative;
    display: inline-block;
}
.gKCJOw::after {
    content: "";
    top: 14.4px;
    display: block;
    height: 3px;
    position: absolute;
    width: 100%;
    background: rgb(238, 113, 153);
}
.eUmdmJ {
    display: inline-block;
    font-size: 24px;
    line-height: 33px;
    color: rgb(84, 89, 101);
    white-space: pre-wrap;
}
.word-revise-div {
    display: flex;
    margin-top: 20px;
}
.right-icon-1 {
    width: 20px;
    height: 59px;
    margin: 0px 20px;
    padding-top: 30px;
    font-size: 24px;
    color: #b2c0d6;
}
</style>

<style>
.quillEditor p {
    font-weight: 4 00;
    font-family: Akkurat Std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Helvetica Neue, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 2rem !important;
    font-size: 1.125rem !important;
}
.explaination{
    color: #0F78FB;
    font-size: 16px;
    padding: 15px 30px;
    text-align: left;
}
</style>
