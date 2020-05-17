<template>
  <div class="container">
    <div class="origin-div">
      <quill-editor :options="editorOption" ref="quillEditorA" class="quillEditor"></quill-editor>
    </div>
    <div class="result-div">
      <div class="error-detail-text">错误情况分析</div>
      <div class="right-bottom-div">
        <div v-for="item in showProblem" :key="item.id" class="each-error-shell-div">
          <div
            class="error-content-info"
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
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Comment',
    props: {
        articleComment: {
            type: Object
        }
    },
    data () {
        return {
            contentText: '',
            editorOption: {
                // quill文本框配置项
                theme: 'snow',
                readOnly: true,
                placeholder: '',
                modules: {
                toolbar: false
                }
            },
            showProblem: [],
            myArticleComment: {}
        }
    },
    mounted () {
        this.contentText = this.articleComment.essay.origin_html;
        this.showProblem = this.articleComment.essay.problem_detail;
        this.$refs.quillEditorA.$refs.editor.innerHTML = this.contentText;
    },
    watch: {
        articleComment (val) {
            this.contentText = this.articleComment.essay.origin_html;
            this.showProblem = this.articleComment.essay.problem_detail;
            this.$refs.quillEditorA.$refs.editor.innerHTML = this.contentText;
        }
    }
}
</script>


<style lang="scss" scoped>
.el-icon-s-home{
  font-size:20px;

}
.top-content-left-1 {
  width: 250px;
  height: 250px;
  opacity: 0.7;
}
.error-content-div {
  display: flex;
}
.icon-div {
  display: flex;
  height: 30px;
  width: 50px;
  color:#606266;
  position: fixed;
  left: 0px;
  top: 0px;
  padding: 10px 10px 15px;
  z-index: 2;
  background-color: transparent;
}
.goback-icon-div {
  font-size: 18px;
  height: 35px;
  width: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  /* box-shadow:  0 5px 5px rgba(0, 0, 0, 0.1), 0 0 1px rgba(82, 168, 236, 0.6); */
  box-shadow: rgba(194, 204, 230, 0.3) 5px 5px 15px 4px;
}
.goback-icon-div:hover {
  /* color: rgb(255, 255, 255); */
  color:#409EFF;
  background-color: #f6f8fc;
  box-shadow: rgba(194, 204, 230, 0.7) 5px 5px 15px 4px;
}
.image-div {
  padding-top: 18px;
}
.little_symbol {
  width: 3px;
  height: 12px;
  /* background-image: linear-gradient(170deg, rgb(89, 159, 254), rgb(108, 188, 230)); */
  background-color: rgb(37, 206, 54);
  border-radius: 5px;
  position: relative;
  left: -8px;
  top: 1px;
}
.container {
  background-color: #f9f9fb;
  overflow-x: hidden;
  width: 100%;
  display: flex;
  /* flex: 1; */
  min-height: 100%;
  /* justify-content: center; */
}
/* 左边编辑框 */
.origin-div {
  flex: 1;
  display: flex;
  /* justify-content: center; */

  flex-direction: column;
  align-items: center;
  padding: 0px 30px;
}

/* 右边结果框 */
.result-div {
  width: 540px;
  background-color: #ffffff;
  margin-right: 0px;
  // overflow: auto;
  box-shadow: 0px 0px 10px 0px rgba(191, 204, 230, 0.3);
}
.quillEditor {
  margin-top: 30px;
  font-size: 17px;
  line-height: 1.88;
  letter-spacing: 0.4px;
  color: rgb(70, 78, 102);
}
.top-content {
  /* margin-right:20px; */
  height: 315px;
  width: 540px;
  /* display: flex; */
  justify-content: space-between;
  /* justify-content: center; */
  box-shadow: 0px 0px 10px 0px rgba(191, 204, 230, 0.3);
  overflow: auto;
}
.top-content-right {
  /* width: 195px; */
  width: 250px;
  padding: 26px 0px 0px 35px;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
}

/* top-right-content */
.error-detail-text {
  display: flex;
  justify-content: center;
  align-items: center;
  line-height: 20px;
  font-size: 18px;
  color: #b2b8c9;
  /* margin:15px 40px 0px 0px; */
  height: 30px;
}
/*
  .top-error-div{
    padding-top: 16px;
  } */
.error-message-text {
  font-size: 14.3px;
  height: 32.5px;
  /* height: 36px; */
  line-height: 32px;
  background-color: rgb(241, 243, 249);
  margin-bottom: 10px;
  color: rgb(84, 89, 101);
  cursor: pointer;
  /* border-radius: 3px; */
  padding: 0px 25px 0px 17px;
  transition: all 0.2s ease 0s;
}
.kbmzcI-currentType {
  box-shadow: rgba(191, 204, 230, 0.75) 0px 0px 10px 0px;
  background: rgb(255, 255, 255);
  /* background-image: linear-gradient(104deg, rgb(89, 159, 254), rgb(108, 188, 230))!important; */
  background-color: rgb(66, 194, 79);
  color: rgb(255, 255, 255);
}
.kbmzcI:active {
  /* background-image: linear-gradient(104deg, rgb(89, 159, 254), rgb(108, 188, 230))!important; */
  background-color: rgb(66, 194, 79);
  color: rgb(255, 255, 255);
}
.kbmzcI:hover {
  box-shadow: rgba(191, 204, 230, 0.7) 0px 0px 10px 0px;
  background: rgb(255, 255, 255);
}
.error-message-count-div {
  float: right;
  display: flex;
  height: 32px;
  /* color: rgb(97, 158, 255); */
  color: rgb(37, 206, 54);
}
.error-message-count-div-currentType {
  float: right;
  display: flex;
  height: 32px;
  color: rgb(241, 243, 249);
}

.line-div {
  width: 443px;
  height: 1px;
  /* background: rgb(215, 224, 239); */
  /* margin-left: 35px; */
}

/* right bottom */
.right-bottom-div {
  padding: 5px 20px;
  overflow: auto;
}
.error-message-type-text {
  height: 16px;
  line-height: 16px;
  font-size: 16px;
  font-weight: 600;
  color: rgb(84, 89, 101);
  margin-bottom: 14px;
  margin-top: 18px;
  display: flex;
}
.error-origin-text {
  height: 45px;
  line-height: 45px;
  display: flex;
  /* padding-right: 8px; */
  box-shadow: transparent 0px 2px 15px 0px;
  border-radius: 3px;
  transition: all 0.2s ease 0s;
}
.left-mouseenter {
  display: flex;
  font-size: 15px;
  color: rgb(178, 184, 201);
  cursor: pointer;
  padding-left: 13px;
  flex: 1 1 0%;
  transition: all 0.2s ease 0s;
  box-shadow: rgba(194, 204, 230, 0.7) 0px 0px 10px 0px;
}
.error-origin-content {
  display: flex;
  font-size: 15px;
  color: rgb(178, 184, 201);
  cursor: pointer;
  padding-left: 13px;
  flex: 1 1 0%;
  transition: all 0.2s ease 0s;
}
.sentence-before-div {
  content: "";
  display: block;
  float: left;
  width: 5px;
  height: 5px;
  background-color: rgb(200, 205, 220);
  margin: 20px 7px 20px 0px;
  border-radius: 50%;
}
.sentence-before-div-0 {
  content: "";
  display: block;
  float: left;
  width: 5px;
  height: 5px;
  background-color: rgb(200, 205, 220);
  margin: 20px 7px 20px 0px;
  border-radius: 50%;
}
.sentence-before-div-0-hover {
  content: "";
  display: block;
  float: left;
  width: 5px;
  height: 5px;
  background-color: rgb(238, 113, 153);
  margin: 20px 7px 20px 0px;
  border-radius: 50%;
}
.sentence-before-div-1 {
  content: "";
  display: block;
  float: left;
  width: 5px;
  height: 5px;
  background-color: rgb(57, 202, 158);
  margin: 20px 7px 20px 0px;
  border-radius: 50%;
}
.the-sentence {
  width: 325px;
}
.the-sentence-1 {
  width: 325px;
  opacity: 0.6;
}
.correct-icon-show-div {
  width: 75px;
  text-align: right;
  font-weight: 600;
  font-size: 14px;
  color: rgb(57, 202, 158);
  margin-right: 0px;
  font-family: -apple-system, BlinkMacSystemFont, PingFang SC, Helvetica Neue,
    Helvetica, Arial, Source Han Sans SC, Microsoft YaHei, sans-serif;
}
.el-icon-check {
  font-size: 19px;
  font-weight: 500;
  position: relative;
  top: 1.45px;
}
.ignore-icon-show-div {
  width: 75px;
  text-align: right;
  font-weight: 600;
  font-size: 14px;
  color: rgb(178, 184, 201);
  margin-right: 0px;
  font-family: -apple-system, BlinkMacSystemFont, PingFang SC, Helvetica Neue,
    Helvetica, Arial, Source Han Sans SC, Microsoft YaHei, sans-serif;
}
.ignore-icon-show-div-1 {
  width: 75px;
  text-align: right;
  font-weight: 600;
  font-size: 14px;
  color: rgb(178, 184, 201);
  margin-right: 0px;
  font-family: -apple-system, BlinkMacSystemFont, PingFang SC, Helvetica Neue,
    Helvetica, Arial, Source Han Sans SC, Microsoft YaHei, sans-serif;
  opacity: 0.6;
}
.error-origin-content:hover {
  box-shadow: rgba(194, 204, 230, 0.7) 0px 0px 10px 0px;
}
.error-word-content {
  color: rgb(84, 89, 101);
}
.error-content-info {
  background-color: rgb(255, 255, 255);
  box-shadow: rgba(191, 204, 230, 0.75) 0px 10px 30px;
  padding: 10px 10px;
  overflow: hidden;
  border-radius: 5px;
  margin: 8px 0px;
  /* width:390px; */
}
.error-content {
  white-space: pre-wrap;
  line-height: 20px;
  font-size: 16px;
  color: rgb(132, 140, 163);
  // cursor: pointer;
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
  justify-content: center;
  margin-top: 15px;
  height: 70px;
}
.right-icon-1 {
  width: 20px;
  height: 59px;
  margin: 0px 20px;
  padding-top: 30px;
  font-size: 24px;
  color: #b2c0d6;
}
.cxbHJz {
  line-height: 26px;
  font-size: 15px;
  font-weight: 600;
  color: rgb(84, 89, 101);
}
.success-button {
  width: 100%;
  height: 44px;
  text-align: center;
  font-size: 16px;
  margin-top: 10px;
  background-color: rgb(66, 194, 79);
  border-color: rgb(66, 194, 79);
  /* background-color:   #419C4F;
    border-color:   #419C4F */
}
.success-button:hover {
  width: 100%;
  height: 44px;
  text-align: center;
  font-size: 16px;
  margin-top: 10px;
  background-color: rgb(107, 214, 118);
  border-color: rgb(107, 214, 118);
}
.hulue-div {
  text-align: center;
  width: 80px;
  font-size: 16px;
  line-height: 22px;
  color: rgb(178, 184, 201);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 15px;
  width: 100%;
  cursor: pointer;
}
</style>

<style>
.origin-text-class-hover {
  background-color: rgba(238, 113, 153, 0.3);
  border-bottom: 3px solid rgb(238, 113, 153);
  color: #444;
  cursor: pointer;
}
.origin-text-class {
  color: rgb(132, 140, 163);
  border-bottom: 3px solid rgb(238, 113, 153);
  cursor: pointer;
}
.origin-text-class:hover {
  background-color: rgba(238, 113, 153, 0.3);
  color: #444;
  border-bottom: 3px solid rgb(238, 113, 153);
}
.origin-text-class-re {
  color: rgb(84, 89, 101);
}
.origin-text-class-re-over {
  color: rgb(238, 113, 153);
}
.origin-text-class-sentence-re {
  color: rgb(238, 113, 153);
}
.correct-text-class-sentence-re {
  color: rgb(57, 202, 158);
}
.correct-text-class {
  color: rgb(132, 140, 163);
  border-bottom: 3px solid #6cc7a1;
  cursor: pointer;
}
.correct-text-class:hover {
  background-color: rgb(190, 233, 215);
  border-bottom: 3px solid #6cc7a1;
}
.correct-text-class-hover {
  color: rgb(132, 140, 163);
  background-color: rgb(190, 233, 215);
  border-bottom: 3px solid #6cc7a1;
  cursor: pointer;
}
.correct-text-class-re {
  color: rgb(57, 202, 158);
}
.correct-text-class-re-over {
  color: rgb(57, 202, 158);
}

.ignore-text-class-sentence-re {
  color: rgb(84, 89, 101);
  font-weight: 600;
}
.ignore-text-class {
  color: rgb(132, 140, 163);
  border-bottom: 3px solid rgb(210, 212, 218);
  cursor: pointer;
}
.ignore-text-class:hover {
  background-color: rgb(235, 236, 241);
  border-bottom: 3px solid rgb(210, 212, 218);
}
.ignore-text-class-hover {
  color: rgb(132, 140, 163);
  background-color: rgb(235, 236, 241);
  border-bottom: 3px solid rgb(210, 212, 218);
  cursor: pointer;
}

.ql-toolbar {
  display: none;
}
.ql-editor {
  background-color: #f9f9fb;
  border: 0;
  white-space: normal !important;
  padding: 0px 0px !important;
}
.ql-container {
  text-align: left;
  font-size: 17px !important;
  line-height: 1.88 !important;
  letter-spacing: 0.4px !important;
  color: rgb(70, 78, 102) !important;
  font-family: Akkurat Std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
    Oxygen, Ubuntu, Cantarell, Helvetica Neue, sans-serif !important;
}
.ql-container.ql-snow {
  border: 0px solid #ccc !important;
}
.quillEditor,
.quillEditor p {
  font-weight: 4 00;
  font-family: Akkurat Std, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
    Oxygen, Ubuntu, Cantarell, Helvetica Neue, sans-serif;
  -webkit-font-smoothing: antialiased;
  line-height: 2rem !important;
  font-size: 1.125rem !important;
}
.quillEditor {
  max-width: 620px;
  min-width: 380px;
}
</style>
