webpackJsonp([1],{"+tar":function(t,e){},"0/3c":function(t,e){},"9GaO":function(t,e){},"9uqx":function(t,e){},CUmV:function(t,e){},FJ7n:function(t,e){},GD3o:function(t,e){},NHnr:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=a("7+uW"),s={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"app"}},[e("router-view")],1)},staticRenderFns:[]};var o=a("VU/8")({name:"App"},s,!1,function(t){a("0/3c")},null,null).exports,r=a("/ocq"),n=a("NYxO");i.default.use(n.a);var l=new n.a.Store({state:{token:""},mutations:{set_token:function(t,e){t.token=e,localStorage.token=e},del_token:function(t){t.token="",localStorage.removeItem("token")}}}),c=a("//Fk"),u=a.n(c),d=a("mtWM"),m=a.n(d),v={apiUrl:"http://127.0.0.1:5000",apiPrefix:"api"};function f(t){return v.apiUrl+"/"+v.apiPrefix+"/"+t}m.a.defaults.timeout=18e5,m.a.defaults.headers.post["Content-Type"]="application/x-www-form-urlencoded;charset=UTF-8",m.a.defaults.withCredentials=!0,m.a.interceptors.request.use(function(t){return l.state.token&&(t.headers.common.Authorization="JWT "+l.state.token),t},function(t){return u.a.reject(t)}),m.a.interceptors.response.use(function(t){return t},function(t){if(t.response)switch(t.response.status){case 401:l.commit("del_token"),sessionStorage.removeItem("token"),st.replace({path:"/login",query:{redirect:st.currentRoute.fullPath}})}return u.a.reject(t)});var p={fetchGet:function(t,e){var a=f(t);return new u.a(function(t,i){m.a.get(a,e).then(function(e){t(e)},function(t){i(t)}).catch(function(t){i(t)})})},fetchPost:function(t,e){var a=f(t);return new u.a(function(t,i){m.a.post(a,e).then(function(e){t(e)},function(t){i(t)}).catch(function(t){i(t)})})}},h={name:"Main",data:function(){return{navList:[{name:"/main/usermain",navItem:"用户主页"},{name:"/main/history",navItem:"历史记录"},{name:"/main/new",navItem:"新建评分"}],name:"",defaultActive:"/main/usermain"}},methods:{dologout:function(){l.commit("del_token"),sessionStorage.removeItem("token"),this.$router.push("/login")},handleselect:function(){this.$router.push("/login")}},created:function(){var t=this;p.fetchGet("users",{}).then(function(e){return 200===e.data.code&&(t.name=e.data.name,!0)}),"/main"!==this.$route.path&&(this.defaultActive=this.$route.path)}},g={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"main"}},[a("el-container",{staticClass:"div-container"},[a("el-header",[a("el-menu",{staticClass:"el-menu-demo",attrs:{"default-active":t.defaultActive,"background-color":"#c2e9fb",mode:"horizontal",router:""},on:{select:t.handleselect}},t._l(t.navList,function(e,i){return a("el-menu-item",{key:i,attrs:{index:e.name}},[a("span",{staticClass:"every-item"},[t._v(t._s(e.navItem))])])}),1),t._v(" "),a("div",{staticClass:"login-logout"},[a("span",{staticClass:"login"},[t._v("欢迎您，"+t._s(t.name))]),t._v(" "),a("el-link",{staticClass:"logout",attrs:{type:"danger"},on:{click:t.dologout}},[t._v("注销")])],1)],1),t._v(" "),a("router-view",{staticClass:"menu-bottom"})],1)],1)},staticRenderFns:[]};var b=a("VU/8")(h,g,!1,function(t){a("dc9F")},"data-v-9fea5940",null).exports,_=a("cf+J"),y=a.n(_),w={name:"Begin",data:function(){return{img:y.a}},methods:{gotolink:function(){this.$router.push("/login")}}},C={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"img",style:{backgroundImage:"url("+this.img+")"}},[e("el-button",{staticClass:"new-button",attrs:{type:"primary",size:"large"},on:{click:this.gotolink}},[this._v("从这里开始")])],1)},staticRenderFns:[]};var x=a("VU/8")(w,C,!1,function(t){a("VnEc")},"data-v-df995830",null).exports,k=a("Av7u"),S=a.n(k),V=S.a.enc.Utf8.parse("13579BDFFDB97531"),T=S.a.enc.Utf8.parse("02468ACEECA86420"),$={name:"Login",data:function(){return{form:{userid:"",password:"",remember:!1},rules:{userid:[{required:!0,message:"用户名/邮箱不能为空",trigger:"blur"}],password:[{required:!0,message:"密码不能为空",trigger:"blur"}]},dialogVisible:!1,dialogVisible1:!1}},created:function(){var t=this.getCookie("userid"),e=this.decrypt(this.getCookie("password"));t&&(this.form.userid=t,this.form.password=e,this.form.remember=!0);var a=this;document.onkeydown=function(t){t=window.event||t,"/login"!==a.$route.path||"Enter"!==t.code&&"Num Enter"!==t.code||a.onSubmit("loginForm")}},methods:{onSubmit:function(t){var e=this;this.$refs[t].validate(function(t){var a={userid:e.form.userid,password:e.form.password};if(!t)return e.dialogVisible=!0,!1;p.fetchPost("login",a).then(function(t){return 200===t.data.code?(e.$store.commit("set_token",t.data.token),sessionStorage.setItem("token",t.data.token),e.setUserInfo(),e.$router.push("/main"),!0):(e.dialogVisible1=!0,!1)})})},setCookie:function(t,e,a){var i=new Date;i.setDate(i.getTime()+a),document.cookie=t+"="+e+(null==a?"":";expires="+i.toGMTString())},getCookie:function(t){if(document.cookie.length>0){var e=document.cookie.indexOf(t+"=");if(-1!==e){e=e+t.length+1;var a=document.cookie.indexOf(";",e);return-1===a&&(a=document.cookie.length),unescape(document.cookie.substring(e,a))}}return""},setUserInfo:function(){if(this.form.remember){this.setCookie("userid",this.form.userid,7);var t=this.encrypt(this.form.password);this.setCookie("password",t,7)}else this.setCookie("userid","",null),this.setCookie("password","",null)},decrypt:function(t){var e=S.a.enc.Hex.parse(t),a=S.a.enc.Base64.stringify(e),i=S.a.AES.decrypt(a,V,{iv:T,mode:S.a.mode.CBC,padding:S.a.pad.Pkcs7});return i.toString(S.a.enc.Utf8).toString()},encrypt:function(t){var e=S.a.enc.Utf8.parse(t);return S.a.AES.encrypt(e,V,{iv:T,mode:S.a.mode.CBC,padding:S.a.pad.Pkcs7}).ciphertext.toString().toUpperCase()}}},q={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"login-container"},[a("el-form",{ref:"loginForm",staticClass:"login-box",attrs:{model:t.form,rules:t.rules,"label-width":"0"}},[a("h3",{staticClass:"login-title"},[t._v("登录")]),t._v(" "),a("el-form-item",{attrs:{prop:"userid"}},[a("el-input",{attrs:{type:"text",placeholder:"用户名/邮箱"},model:{value:t.form.userid,callback:function(e){t.$set(t.form,"userid",e)},expression:"form.userid"}})],1),t._v(" "),a("el-form-item",{attrs:{prop:"password"}},[a("el-input",{attrs:{type:"password",placeholder:"密码"},model:{value:t.form.password,callback:function(e){t.$set(t.form,"password",e)},expression:"form.password"}})],1),t._v(" "),a("div",{staticClass:"under-input"},[a("el-checkbox",{staticClass:"remember-checkbox",model:{value:t.form.remember,callback:function(e){t.$set(t.form,"remember",e)},expression:"form.remember"}},[t._v("记住我")]),t._v(" "),a("el-link",{staticClass:"register-button",attrs:{type:"primary",href:"/#/register"}},[t._v("注册")])],1),t._v(" "),a("el-form-item",{staticClass:"login-button"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){return t.onSubmit("loginForm")}}},[t._v("登录")])],1)],1),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible,width:"30%"},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("span",[t._v("请输入帐号和密码")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogVisible=!1}}},[t._v("确定")])],1)]),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible1,width:"30%"},on:{"update:visible":function(e){t.dialogVisible1=e}}},[a("span",[t._v("帐号或密码错误")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogVisible1=!1}}},[t._v("确定")])],1)])],1)},staticRenderFns:[]};var L=a("VU/8")($,q,!1,function(t){a("WcYl")},"data-v-1abf2434",null).exports,R={name:"Register",data:function(){var t=this;return{show:!0,count:"",timer:null,form:{email:"",username:"",password:"",confirmPassword:"",name:"",verificationCode:""},dialogVisible:!1,dialogVisible1:!1,dialogVisible2:!1,dialogVisible3:!1,dialogVisible4:!1,countMessage:"",interval:null,rules:{email:[{required:!0,message:"请输入邮箱地址",trigger:"blur"},{type:"email",message:"请输入正确的邮箱地址",trigger:"blur"}],username:[{required:!0,message:"请输入用户名",trigger:"blur"},{min:0,max:20,message:"用户名的长度不得超过20个字符",trigger:["blur","change"]}],password:[{required:!0,message:"请输入密码",trigger:"blur"},{min:8,max:15,message:"密码长度为8～15位",trigger:"blur"},{validator:function(e,a,i){""!==t.form.confirmPassword&&t.$refs.registerForm.validateField("confirmPassword"),i()},trigger:"blur"}],confirmPassword:[{required:!0,message:"请输入确认密码",trigger:"blur"},{validator:function(e,a,i){a!==t.form.password?i(new Error("两次输入的密码不一致")):i()},trigger:"blur"}],name:[{min:0,max:20,message:"昵称长度过长",trigger:["blur","change"]}],verificationCode:[{required:!0,message:"请输入验证码",trigger:"blur"}]}}},methods:{onSubmit:function(t){var e=this,a={email:this.form.email,username:this.form.username,password:this.form.password,name:this.form.name,verificationCode:this.form.verificationCode};this.$refs[t].validate(function(t){if(!t)return e.dialogVisible=!0,!1;p.fetchPost("register",a).then(function(t){if(200===t.data.code){var a=e,i=5;return e.interval=window.setInterval(function(){a.countMessage="注册成功！"+i+"秒后返回登录",!1===a.dialogVisible3&&(e.dialogVisible3=!0),--i<0&&(window.clearInterval(a.interval),e.$router.push("/login"))},1e3),!0}return"email"===t.data.wrongType?(e.dialogVisible2=!0,!1):"username"===t.data.wrongType?(e.dialogVisible1=!0,!1):"verificationCode"===t.data.wrongType?(e.dialogVisible4=!0,!1):void 0})})},backToLogin:function(){this.interval&&window.clearInterval(this.interval),this.$router.push("/login")},send:function(){var t=this;this.timer||(this.count=60,this.show=!1,this.timer=setInterval(function(){t.count>0&&t.count<=60?t.count--:(t.show=!0,clearInterval(t.timer),t.timer=null)},1e3)),p.fetchPost("confirm",{email:this.form.email}).then(function(e){return 200===e.data.code||("email"===e.data.wrongType&&(t.dialogVisible2=!0),!1)})}}},E={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"register-container"},[a("el-form",{ref:"registerForm",staticClass:"register-box",attrs:{model:t.form,"status-icon":"",rules:t.rules,"label-width":"0"}},[a("h3",{staticClass:"register-title"},[t._v("注册")]),t._v(" "),a("el-form-item",{attrs:{prop:"email"}},[a("el-input",{attrs:{type:"text",placeholder:"请填写邮箱地址"},model:{value:t.form.email,callback:function(e){t.$set(t.form,"email",e)},expression:"form.email"}})],1),t._v(" "),a("el-form-item",{attrs:{prop:"verificationCode"}},[a("el-input",{staticStyle:{width:"60%",float:"left"},attrs:{type:"text",placeholder:"请输入验证码"},model:{value:t.form.verificationCode,callback:function(e){t.$set(t.form,"verificationCode",e)},expression:"form.verificationCode"}}),t._v(" "),a("el-button",{staticStyle:{width:"35%"},attrs:{icon:"el-icon-mobile-phone",type:"success",disabled:t.disabled=!t.show},on:{click:t.send}},[a("span",{directives:[{name:"show",rawName:"v-show",value:t.show,expression:"show"}]},[t._v("获取验证码")]),t._v(" "),a("span",{directives:[{name:"show",rawName:"v-show",value:!t.show,expression:"!show"}],staticClass:"count"},[t._v(t._s(t.count)+" s")])])],1),t._v(" "),a("el-form-item",{attrs:{prop:"username"}},[a("el-input",{attrs:{type:"text",placeholder:"请设置用户名"},model:{value:t.form.username,callback:function(e){t.$set(t.form,"username",e)},expression:"form.username"}})],1),t._v(" "),a("el-form-item",{attrs:{prop:"password"}},[a("el-input",{attrs:{type:"password",placeholder:"密码"},model:{value:t.form.password,callback:function(e){t.$set(t.form,"password",e)},expression:"form.password"}})],1),t._v(" "),a("el-form-item",{attrs:{prop:"confirmPassword"}},[a("el-input",{attrs:{type:"password",placeholder:"确认密码"},model:{value:t.form.confirmPassword,callback:function(e){t.$set(t.form,"confirmPassword",e)},expression:"form.confirmPassword"}})],1),t._v(" "),a("el-form-item",{attrs:{prop:"name"}},[a("el-input",{attrs:{type:"text",placeholder:"昵称"},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),t._v(" "),a("el-form-item",[a("el-button",{staticClass:"return-button",on:{click:t.backToLogin}},[t._v("返回登录")]),t._v(" "),a("el-button",{staticClass:"register-button",attrs:{type:"primary"},on:{click:function(e){return t.onSubmit("registerForm")}}},[t._v("注册")])],1)],1),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible,width:"30%"},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("span",[t._v("输入信息不正确")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogVisible=!1}}},[t._v("确定")])],1)]),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible1,width:"30%"},on:{"update:visible":function(e){t.dialogVisible1=e}}},[a("span",[t._v("用户名已被注册")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogVisible1=!1}}},[t._v("确定")])],1)]),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible2,width:"30%"},on:{"update:visible":function(e){t.dialogVisible2=e}}},[a("span",[t._v("邮箱已被注册")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(e){t.dialogVisible2=!1}}},[t._v("确定")]),t._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:t.backToLogin}},[t._v("返回登录")])],1)]),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible3,width:"30%"},on:{"update:visible":function(e){t.dialogVisible3=e},close:t.backToLogin}},[a("span",[t._v(t._s(t.countMessage))]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:t.backToLogin}},[t._v("立即返回")])],1)]),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible4,width:"30%"},on:{"update:visible":function(e){t.dialogVisible4=e}}},[a("span",[t._v("验证码不正确")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogVisible4=!1}}},[t._v("确定")])],1)])],1)},staticRenderFns:[]};var I=a("VU/8")(R,E,!1,function(t){a("+tar")},"data-v-f9d6147c",null).exports,F={data:function(){return{records:[],noRecords:!1,reverse:!0,count:0,maxScore:0}},mounted:function(){var t=this;p.fetchGet("records").then(function(e){return 200===e.data.code&&(0!==e.data.records.length?(t.records=e.data.records,t.count=t.records.length,t.maxScore=t.getMaxScore(),t.dateToString()):t.noRecords=!0,!0)})},methods:{toRecord:function(t){this.$router.push({path:"/result",query:{recordId:t}})},getMaxScore:function(){var t=0;for(var e in this.records)this.records[e].totalScore>t&&(t=this.records[e].totalScore);return t},dateToString:function(){for(var t in this.records){var e=new Date(this.records[t].commitTime);this.records[t].commitTime=e.getFullYear()+"-"+(e.getMonth()+1)+"-"+e.getDate()+" "+e.getHours()+":"+e.getMinutes()+":"+e.getSeconds()}}}},D={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-main",[a("el-col",{attrs:{span:18}},[a("div",{staticClass:"block"},[t.noRecords?a("p",{staticClass:"norecord-text"},[t._v("您还没有评分记录。")]):t._e(),t._v(" "),a("el-timeline",{attrs:{reverse:t.reverse}},t._l(t.records,function(e,i){return a("el-timeline-item",{key:i,attrs:{timestamp:e.commitTime,placement:"top"}},[a("el-card",{staticClass:"card-box"},[a("span",{staticClass:"article-title"},[t._v("题目："+t._s(e.articleTitle))]),t._v(" "),a("span",{staticClass:"total-score"},[t._v("得分："+t._s(e.totalScore))]),t._v(" "),a("p",{staticClass:"article-content"},[t._v(t._s(e.articleContent))]),t._v(" "),a("el-link",{staticClass:"more-button",attrs:{type:"primary"},on:{click:function(a){return t.toRecord(e.recordId)}}},[t._v("更多")])],1)],1)}),1)],1)]),t._v(" "),a("el-col",{attrs:{span:6}},[a("div",{staticClass:"calculate-box"},[a("div",{staticClass:"calculate-item"},[a("div",{staticClass:"words",staticStyle:{"font-family":"'Adobe 楷体 Std R'",color:"#337afb"}},[t._v("当前使用")]),t._v(" "),a("div",{staticClass:"circle"},[t._v(t._s(t.count))]),t._v(" "),a("div",{staticStyle:{"margin-top":"45px","font-family":"'Adobe 楷体 Std R'",color:"#337afb"}},[t._v("次")])]),t._v(" "),a("div",{staticClass:"calculate-item"},[a("div",{staticClass:"words",staticStyle:{"font-family":"'Adobe 楷体 Std R'",color:"#337afb"}},[t._v("当前最高")]),t._v(" "),a("div",{staticClass:"circle"},[t._v(t._s(t.maxScore))]),t._v(" "),a("div",{staticStyle:{"margin-top":"45px","font-family":"'Adobe 楷体 Std R'",color:"#337afb"}},[t._v("分")])])])])],1)},staticRenderFns:[]};var A=a("VU/8")(F,D,!1,function(t){a("FJ7n")},"data-v-4ccc4c16",null).exports,P=a("mvHQ"),W=a.n(P),M=a("XLwt"),U=a.n(M),O={data:function(){return{emptyMessage:"",visible1:!1,visible2:!0,visible3:!0,records:[],wrongchars:{},suggestion:"",vocabulary:0,vocabularySuggestion:"",tableData:[],pickerOptions:{shortcuts:[{text:"最近一周",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-6048e5),t.$emit("pick",[a,e])}},{text:"最近一个月",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-2592e6),t.$emit("pick",[a,e])}},{text:"最近三个月",onClick:function(t){var e=new Date,a=new Date;a.setTime(a.getTime()-7776e6),t.$emit("pick",[a,e])}}]},timeValue:""}},mounted:function(){var t=this;p.fetchGet("history").then(function(e){return 200===e.data.code&&(e.data.records?(t.records=e.data.records,t.wrongchars=e.data.wrongchars,t.initDataTable(),t.suggestion=e.data.suggestion,t.vocabulary=e.data.vocabulary,t.vocabularySuggestion=e.data.vocabularySuggestion,"{}"===W()(t.wrongchars)&&(t.visible3=!1),t.drawScoreLine(),t.drawVocabularyLine()):(t.visible1=!0,t.visible2=!1,t.emptyMessage=e.data.message),!0)})},methods:{onSubmit:function(){var t=this,e={startTime:this.timeValue[0],endTime:this.timeValue[1]};this.visible1=!1,this.visible2=!0,p.fetchPost("history",e).then(function(e){return 200===e.data.code&&(e.data.records?(t.records=e.data.records,t.wrongchars=e.data.wrongchars,t.initDataTable(),t.suggestion=e.data.suggestion,t.vocabulary=e.data.vocabulary,t.vocabularySuggestion=e.data.vocabularySuggestion,"{}"===W()(t.wrongchars)&&(t.visible3=!1),t.drawScoreLine(),t.drawVocabularyLine()):(t.visible1=!0,t.visible2=!1,t.emptyMessage=e.data.message),!0)})},initDataTable:function(){for(var t in this.wrongchars)this.tableData.push({wrongchar:t,num:this.wrongchars[t]})},drawScoreLine:function(){var t=U.a.init(document.getElementById("scoreLine")),e={title:{text:"总得分统计图",color:"#337afb"},xAxis:{name:"次数",nameTextStyle:{fontSize:10},type:"category",data:[]},yAxis:{name:"分值",nameTextStyle:{fontSize:10},type:"value",max:100},series:[{data:[],type:"line"}]},a=[],i=[],s=1;for(var o in this.records)a.push(s),s+=1,i.push(this.records[o].totalScore);e.xAxis.data=a,e.series[0].data=i,t.setOption(e)},drawVocabularyLine:function(){var t=U.a.init(document.getElementById("vocabularyLine")),e={title:{text:"词汇水平得分统计图"},xAxis:{name:"次数",nameTextStyle:{fontSize:10},type:"category",data:[]},yAxis:{name:"等级",nameTextStyle:{fontSize:10},type:"value",max:5},series:[{data:[],type:"line"}]},a=[],i=[],s=1;for(var o in this.records)a.push(s),s+=1,i.push(this.records[o].vocabularyLevel);e.xAxis.data=a,e.series[0].data=i,t.setOption(e)},drawWrongcharChart:function(){var t=U.a.init(document.getElementById("wrongcharChart")),e=[],a=[];for(var i in this.wrongchars)e.push(i),a.push(this.wrongchars[i]);for(var s=[],o=0;o<a.length;o++)s.push(20);var r={title:{text:"错别字统计图"},xAxis:{data:e,axisLabel:{inside:!0,textStyle:{color:"#fff"}},axisTick:{show:!1},axisLine:{show:!1},z:10},yAxis:{axisLine:{show:!1},axisTick:{show:!1},axisLabel:{textStyle:{color:"#999"}}},dataZoom:[{type:"inside"}],series:[{type:"bar",itemStyle:{color:"rgba(0,0,0,0.05)"},barGap:"-100%",barCategoryGap:"40%",data:s,animation:!1},{type:"bar",itemStyle:{color:new U.a.graphic.LinearGradient(0,0,0,1,[{offset:0,color:"#83bff6"},{offset:.5,color:"#188df0"},{offset:1,color:"#188df0"}])},emphasis:{itemStyle:{color:new U.a.graphic.LinearGradient(0,0,0,1,[{offset:0,color:"#2378f7"},{offset:.7,color:"#2378f7"},{offset:1,color:"#83bff6"}])}},data:a}]};t.on("click",function(i){console.log(e[Math.max(i.dataIndex-3,0)]),t.dispatchAction({type:"dataZoom",startValue:e[Math.max(i.dataIndex-3,0)],endValue:e[Math.min(i.dataIndex+3,a.length-1)]})}),t.setOption(r)}}},z={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-main",[t.visible1?a("p",{staticClass:"empty-content"},[t._v(t._s(t.emptyMessage))]):t._e(),t._v(" "),a("div",[a("el-row",{staticClass:"el-row1"},[a("el-col",{attrs:{span:24}},[a("span",{staticClass:"demonstration"},[t._v("统计时间范围：")]),t._v(" "),a("el-date-picker",{attrs:{type:"daterange","unlink-panels":"","range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期","picker-options":t.pickerOptions,"value-format":"yyyy-MM-dd"},on:{change:t.onSubmit},model:{value:t.timeValue,callback:function(e){t.timeValue=e},expression:"timeValue"}})],1)],1),t._v(" "),t.visible2?a("el-row",{staticClass:"el-row2"},[a("div",{staticClass:"pic1"},[a("div",{staticStyle:{width:"100%",height:"300px"},attrs:{id:"scoreLine"}})]),t._v(" "),a("div",{staticClass:"suggestion1"},[a("el-col",{attrs:{span:24}},[a("el-card",{staticClass:"suggestion-card"},[a("p",[t._v("建议：")]),t._v(" "),a("p",[t._v(t._s(t.suggestion))])])],1)],1)]):t._e(),t._v(" "),t.visible2?a("el-row",{staticClass:"el-row2"},[a("div",{staticClass:"pic2"},[a("div",{staticStyle:{width:"100%",height:"300px"},attrs:{id:"vocabularyLine"}})]),t._v(" "),a("div",{staticClass:"suggestion2"},[a("el-col",{attrs:{span:24}},[a("el-card",{staticClass:"suggestion-card"},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.tableData,height:"260px","default-sort":{prop:"num",order:"descending"}}},[a("el-table-column",{attrs:{prop:"wrongchar",label:"错别字",width:"180"}}),t._v(" "),a("el-table-column",{attrs:{prop:"num",label:"错误次数",width:"180"}})],1)],1)],1)],1)]):t._e()],1)])},staticRenderFns:[]};var B=a("VU/8")(O,z,!1,function(t){a("k2wP")},"data-v-72b12db0",null).exports,H={name:"New",data:function(){return{form:{title:"",article:""},loading:!1,count:0,dialogVisible:!1,rules:{title:[{required:!0,message:"题目不能为空",trigger:"blur"},{min:0,max:30,message:"题目长度过长",trigger:["blur","change"]}],article:[{required:!0,message:"文章不能为空",trigger:"blur"},{min:0,max:1500,message:"文章长度过长",trigger:["blur","change"]}]}}},methods:{onSubmit:function(t){var e=this,a={title:this.form.title,article:this.form.article};this.$refs[t].validate(function(t){if(!t)return e.dialogVisible=!0,!1;e.loading=!0,p.fetchPost("records",a).then(function(t){return 200===t.data.code&&(e.loading=!1,e.$router.push({path:"/result",query:{recordId:t.data.recordId}}),!0)})})},countChar:function(){var t=/[\u4E00-\u9FA5]/g;this.form.article.match(t)?this.count=this.form.article.match(t).length:this.count=0}}},j={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("el-main",{directives:[{name:"loading",rawName:"v-loading",value:t.loading,expression:"loading"}],attrs:{"element-loading-text":"正在计算得分","element-loading-background":"rgba(255, 255, 255, 0.7)"}},[a("el-form",{ref:"newForm",staticClass:"new-box",attrs:{model:t.form,"label-width":"80px",rules:t.rules,"label-position":"top"}},[a("el-form-item",{attrs:{prop:"title",label:"题目："}},[a("el-input",{staticClass:"title-input",attrs:{type:"text"},model:{value:t.form.title,callback:function(e){t.$set(t.form,"title",e)},expression:"form.title"}})],1),t._v(" "),a("el-form-item",{attrs:{prop:"article",label:"请输入正文："}},[a("el-input",{staticClass:"article-input",attrs:{type:"textarea",rows:18},on:{input:t.countChar},model:{value:t.form.article,callback:function(e){t.$set(t.form,"article",e)},expression:"form.article"}})],1),t._v(" "),a("el-form-item",[a("span",{staticClass:"count-corner"},[t._v("字数："+t._s(t.count))]),t._v(" "),a("el-button",{staticClass:"new-button",attrs:{type:"primary",size:"medium"},on:{click:function(e){return t.onSubmit("newForm")}}},[t._v("提交")])],1)],1),t._v(" "),a("el-dialog",{attrs:{title:"提示",visible:t.dialogVisible,width:"30%"},on:{"update:visible":function(e){t.dialogVisible=e}}},[a("span",[t._v("题目或文章格式不正确")]),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogVisible=!1}}},[t._v("确定")])],1)])],1)},staticRenderFns:[]};var G=a("VU/8")(H,j,!1,function(t){a("iFqB")},"data-v-53529975",null).exports,N={name:"Comment",props:{articleComment:{type:Object}},data:function(){return{contentText:"",editorOption:{theme:"snow",readOnly:!0,placeholder:"",modules:{toolbar:!1}},showProblem:[],myArticleComment:{}}},mounted:function(){this.contentText=this.articleComment.essay.origin_html,this.showProblem=this.articleComment.essay.problem_detail,this.$refs.quillEditorA.$refs.editor.innerHTML=this.contentText},watch:{articleComment:function(t){this.contentText=this.articleComment.essay.origin_html,this.showProblem=this.articleComment.essay.problem_detail,this.$refs.quillEditorA.$refs.editor.innerHTML=this.contentText}}},J={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("div",{staticClass:"origin-div"},[a("quill-editor",{ref:"quillEditorA",staticClass:"quillEditor",attrs:{options:t.editorOption}})],1),t._v(" "),a("div",{staticClass:"result-div"},[a("div",{staticClass:"error-detail-text"},[t._v("错误情况分析")]),t._v(" "),a("div",{staticClass:"right-bottom-div"},t._l(t.showProblem,function(e){return a("div",{key:e.id,staticClass:"each-error-shell-div"},[a("div",{staticClass:"error-content-info"},[a("div",{staticClass:"error-content",domProps:{innerHTML:t._s(e.token_strs)}},[t._v(t._s(e.token_strs))]),t._v(" "),a("div",{staticClass:"word-revise-div"},[a("div",{staticClass:"ErrorWordContent fsReJu"},[a("span",{staticClass:"originWordText ntLBp"},[t._v("你写的")]),t._v(" "),a("span",{staticClass:"unfixed Checkstyle__ErrorWord-an9z37-43 gKCJOw",staticStyle:{"font-size":"30px"}},[t._v(t._s(e.origin_text))])]),t._v(" "),a("i",{staticClass:"el-icon-right right-icon-1"}),t._v(" "),a("div",{staticClass:"Checkstyle__CorrectWordContent-an9z37-40 ehNdGM"},[a("span",{staticClass:"Checkstyle__SmallWordTip-an9z37-41 ntLBp"},[t._v("修改建议")]),t._v(" "),a("span",{staticClass:"unfixed Checkstyle__CorrectWord-an9z37-44 eUmdmJ",staticStyle:{"font-size":"30px"}},[t._v(t._s(e.correct_text))])])])])])}),0)])])},staticRenderFns:[]};var K=a("VU/8")(N,J,!1,function(t){a("GD3o"),a("XBDi")},"data-v-2789e5f9",null).exports,Y={name:"Vocabulary",props:{suggestion:{type:Object}},watch:{suggestion:function(t){}}},X={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},t._l(t.suggestion,function(e,i,s){return a("div",{key:s,staticClass:"each-error-shell-div"},[a("div",{staticClass:"error-content-info"},[a("div",{staticClass:"word-revise-div"},[a("div",{staticClass:"Checkstyle__CorrectWordContent-an9z37-40 ehNdGM"},[a("span",{staticClass:"unfixed Checkstyle__CorrectWord-an9z37-44 eUmdmJ",staticStyle:{"font-size":"30px",width:"100px"}},[t._v(t._s(i))])]),t._v(" "),t._l(e.main,function(e){return a("div",{key:e.sense,staticClass:"explaination"},[a("span",{staticClass:"meaning"},[t._v("意思："),a("span",[t._v(t._s(e.sense))])]),a("br"),t._v(" "),e.examples[0]?a("span",{staticClass:"example"},[t._v("例句："),a("span",[t._v(t._s(e.examples[0][0]))])]):t._e()])})],2)])])}),0)},staticRenderFns:[]};var Z={components:{"component-comment":K,"component-vocabulary":a("VU/8")(Y,X,!1,function(t){a("CUmV"),a("qWO+")},"data-v-196d997a",null).exports},data:function(){return{boxType:"comment",activeIndex:"1",articleTitle:"",articleContent:"",totalScore:0,vocabularyLevel:0,titleRelativity:0,sentenceDifficulty:0,articleComment:{},suggestion:{},hsk1:0,hsk2:0,hsk3:0,hsk4:0,hsk5:0,hsk6:0}},methods:{setArticleComment:function(){this.boxType="comment"},setVocabularyDevelopment:function(){this.boxType="vocabulary"},drawVocabularyPie:function(){var t=U.a.init(document.getElementById("vocabularyPie")),e={title:{},tooltip:{trigger:"item",formatter:"{a} <br/>{b} : {c} ({d}%)"},series:[{name:"词汇类别",type:"pie",radius:"40%",center:["50%","57%"],data:[{value:this.hsk1,name:"HSK一级",label:{fontWeight:"bold"}},{value:this.hsk2,name:"HSK二级",label:{fontWeight:"bold"}},{value:this.hsk3,name:"HSK三级",label:{fontWeight:"bold"}},{value:this.hsk4,name:"HSK四级",label:{fontWeight:"bold"}},{value:this.hsk5,name:"HSK五级",label:{fontWeight:"bold"}},{value:this.hsk6,name:"HSK六级",label:{fontWeight:"bold"}}],emphasis:{itemStyle:{shadowBlur:10,shadowOffsetX:0,shadowColor:"rgba(0, 0, 0, 0.5)"}}}]};t.setOption(e)},formatInt:function(t){return 1===t.toString().split(".").length?t=t.toString()+".0":t}},mounted:function(){var t=this;p.fetchGet("record/"+this.$route.query.recordId).then(function(e){return 200===e.data.code&&(t.articleTitle=e.data.data.articleTitle,t.articleContent=e.data.data.articleContent,t.totalScore=e.data.data.totalScore,t.vocabularyLevel=e.data.data.vocabularyLevel,t.titleRelativity=e.data.data.titleRelativity,t.sentenceDifficulty=e.data.data.sentenceDifficulty,t.articleComment=e.data.data.articleComment,t.suggestion=e.data.data.suggestion,console.log(t.suggestion),t.hsk1=e.data.data.hsk1,t.hsk2=e.data.data.hsk2,t.hsk3=e.data.data.hsk3,t.hsk4=e.data.data.hsk4,t.hsk5=e.data.data.hsk5,t.hsk6=e.data.data.hsk6,t.totalScore=t.formatInt(t.totalScore),t.vocabularyLevel=t.formatInt(t.vocabularyLevel),t.titleRelativity=t.formatInt(t.titleRelativity),t.sentenceDifficulty=t.formatInt(t.sentenceDifficulty),t.drawVocabularyPie(),!0)})}},Q={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"main"}},[a("div",{staticClass:"el-row1"},[a("el-row",{attrs:{gutter:120}},[a("el-col",{attrs:{span:12}},[a("span",{staticClass:"article-title"},[t._v("题目："+t._s(t.articleTitle))])]),t._v(" "),a("el-col",{attrs:{span:6,offset:3}},[a("span",{staticClass:"total-score"},[t._v("总得分："+t._s(t.totalScore)+"/100")])])],1)],1),t._v(" "),a("div",{staticClass:"el-row2"},[a("el-row",{attrs:{gutter:30}},[a("el-col",{attrs:{span:12}},[a("div",{staticClass:"pie-title"},[a("h4",[a("span",{staticClass:"vocabularyWords"},[t._v("词汇分布")])])]),t._v(" "),a("hr",{staticStyle:{margin:"-20px 30px -100px 100px"}}),t._v(" "),a("div",{staticStyle:{width:"100%",height:"400px","padding-left":"40px"},attrs:{id:"vocabularyPie"}})]),t._v(" "),a("el-col",{attrs:{span:12}},[a("div",{staticClass:"score-title"},[a("h4",[t._v("分项得分")])]),t._v(" "),a("hr",{staticStyle:{margin:"-20px 95px 50px 70px"}}),t._v(" "),a("div",{staticClass:"score-content"},[a("div",{staticClass:"each-score-content"},[a("span",{staticClass:"each-score-title"},[t._v("词汇水平")]),t._v(" "),a("el-rate",{attrs:{disabled:"","show-score":"","text-color":"ffba00","score-template":"{value}"},model:{value:t.vocabularyLevel,callback:function(e){t.vocabularyLevel=e},expression:"vocabularyLevel"}})],1),t._v(" "),a("div",{staticClass:"each-score-content"},[a("span",{staticClass:"each-score-title"},[t._v("切题程度")]),t._v(" "),a("el-rate",{attrs:{disabled:"","show-score":"","text-color":"ffba00","score-template":"{value}"},model:{value:t.titleRelativity,callback:function(e){t.titleRelativity=e},expression:"titleRelativity"}})],1),t._v(" "),a("div",{staticClass:"each-score-content"},[a("span",{staticClass:"each-score-title"},[t._v("句型难度")]),t._v(" "),a("el-rate",{attrs:{disabled:"","show-score":"","text-color":"ffba00","score-template":"{value}"},model:{value:t.sentenceDifficulty,callback:function(e){t.sentenceDifficulty=e},expression:"sentenceDifficulty"}})],1)])])],1)],1),t._v(" "),a("el-row",{staticClass:"el-row3"},[a("el-col",{attrs:{span:24}},[a("div",{staticClass:"block-title"},[a("h4",[t._v("全文点评")])]),t._v(" "),a("hr",{staticStyle:{margin:"-25px 100px 15px 100px"}}),t._v(" "),a("div",{staticClass:"comment-block"},[a("el-menu",{staticClass:"el-menu-demo",attrs:{"default-active":t.activeIndex,mode:"horizontal"}},[a("el-menu-item",{attrs:{index:"1"},on:{click:t.setArticleComment}},[t._v("原文点评")]),t._v(" "),a("el-menu-item",{attrs:{index:"2"},on:{click:t.setVocabularyDevelopment}},[t._v("词汇拓展")])],1),t._v(" "),"comment"===t.boxType?a("component-comment",{staticClass:"box-card",attrs:{articleComment:t.articleComment}}):"vocabulary"===t.boxType?a("component-vocabulary",{staticClass:"box-card",attrs:{suggestion:t.suggestion}}):t._e()],1)])],1)],1)},staticRenderFns:[]};var tt=a("VU/8")(Z,Q,!1,function(t){a("9uqx")},"data-v-7727a4bb",null).exports,et={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"hello"},[a("h1",[t._v(t._s(t.msg))]),t._v(" "),a("h2",[t._v("Essential Links")]),t._v(" "),t._m(0),t._v(" "),a("h2",[t._v("Ecosystem")]),t._v(" "),t._m(1)])},staticRenderFns:[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("ul",[a("li",[a("a",{attrs:{href:"https://vuejs.org",target:"_blank"}},[t._v("\n        Core Docs\n      ")])]),t._v(" "),a("li",[a("a",{attrs:{href:"https://forum.vuejs.org",target:"_blank"}},[t._v("\n        Forum\n      ")])]),t._v(" "),a("li",[a("a",{attrs:{href:"https://chat.vuejs.org",target:"_blank"}},[t._v("\n        Community Chat\n      ")])]),t._v(" "),a("li",[a("a",{attrs:{href:"https://twitter.com/vuejs",target:"_blank"}},[t._v("\n        Twitter\n      ")])]),t._v(" "),a("br"),t._v(" "),a("li",[a("a",{attrs:{href:"http://vuejs-templates.github.io/webpack/",target:"_blank"}},[t._v("\n        Docs for This Template\n      ")])])])},function(){var t=this.$createElement,e=this._self._c||t;return e("ul",[e("li",[e("a",{attrs:{href:"http://router.vuejs.org/",target:"_blank"}},[this._v("\n        vue-router\n      ")])]),this._v(" "),e("li",[e("a",{attrs:{href:"http://vuex.vuejs.org/",target:"_blank"}},[this._v("\n        vuex\n      ")])]),this._v(" "),e("li",[e("a",{attrs:{href:"http://vue-loader.vuejs.org/",target:"_blank"}},[this._v("\n        vue-loader\n      ")])]),this._v(" "),e("li",[e("a",{attrs:{href:"https://github.com/vuejs/awesome-vue",target:"_blank"}},[this._v("\n        awesome-vue\n      ")])])])}]};var at=a("VU/8")({name:"HelloWorld",data:function(){return{msg:"Welcome to Your Vue.js App"}}},et,!1,function(t){a("RqNW")},"data-v-3b884edb",null).exports;i.default.use(r.a);var it=new r.a({routes:[{path:"/",name:"HelloWorld",component:at,meta:{required:!0,title:"HelloWorld"}},{path:"/main",name:"Main",component:b,meta:{required:!0,title:"主页面"},children:[{path:"/main/usermain",name:"UserMain",component:A,meta:{required:!0,title:"用户主页"}},{path:"/main/history",name:"History",component:B,meta:{required:!0,title:"历史记录"}},{path:"/main/new",name:"New",component:G,meta:{required:!0,title:"新建评分"}},{path:"",component:A,meta:{required:!0,title:"用户主页"}}]},{path:"/login",name:"Login",component:L,meta:{required:!1,title:"登录"}},{path:"/register",name:"Register",component:I,meta:{required:!1,title:"注册"}},{path:"/result",name:"Result",component:tt,meta:{required:!0,title:"评分结果"}},{path:"/begin",name:"Begin",component:x,meta:{required:!1,title:"首页"}}]});it.beforeEach(function(t,e,a){t.meta.title&&(document.title=t.meta.title),t.meta.required?l.state.token?a():sessionStorage.getItem("token")?(l.state.token=sessionStorage.getItem("token"),a()):a({path:"/begin",query:{redirect:t.fullpath}}):a()});var st=it,ot=a("zL8q"),rt=a.n(ot),nt=(a("tvR6"),a("mw3O")),lt=a.n(nt),ct=a("aiqZ"),ut=a.n(ct);a("oTFt"),a("9GaO"),a("v/ij");i.default.use(ut.a),i.default.prototype.$axios=m.a,i.default.prototype.qs=lt.a,i.default.config.productionTip=!1,i.default.use(r.a),i.default.use(rt.a),new i.default({el:"#app",router:st,store:l,render:function(t){return t(o)}})},RqNW:function(t,e){},VnEc:function(t,e){},WcYl:function(t,e){},XBDi:function(t,e){},"cf+J":function(t,e,a){t.exports=a.p+"static/img/background.555b9ac.png"},dc9F:function(t,e){},iFqB:function(t,e){},k2wP:function(t,e){},oTFt:function(t,e){},"qWO+":function(t,e){},tvR6:function(t,e){},"v/ij":function(t,e){}},["NHnr"]);
//# sourceMappingURL=app.c0aa0ea4b310b6abbec6.js.map