(window.webpackJsonp=window.webpackJsonp||[]).push([[51],{DHhl:function(t,e,n){"use strict";n.d(e,"a",(function(){return i})),n.d(e,"b",(function(){return o}));var i=function(){var t=this,e=t._self._c;return e("div",[e("Card",{attrs:{header:"内容导入"}}),t._v(" "),e("Card",[e("div",{staticClass:"content-import-source"},[e("span",{staticClass:"content-import-source__title"},[t._v("来源")]),t._v(" "),e("el-select",{staticClass:"content-import-source__option",attrs:{placeholder:"选择内容来源",clearable:""},model:{value:t.contentSourceId,callback:function(e){t.contentSourceId=e},expression:"contentSourceId"}},t._l(t.contentSource,(function(t){return e("el-option",{key:t.id,staticClass:"content-import-source__option-selected",attrs:{label:t.name,value:t.id}})})),1)],1)]),t._v(" "),4!==t.contentSourceId&&5!==t.contentSourceId?e("div",{staticClass:"content-import"},[t._v("多次导入同一话题会导致数据重复，需要站长手动清理")]):t._e(),t._v(" "),5===t.contentSourceId?e("div",{staticClass:"content-import"},[t._v("仅支持导入已加入的星球内容，多次导入同一话题会导致数据重复，需要站长手动清理")]):t._e(),t._v(" "),5===t.contentSourceId?e("Card",[e("div",{staticClass:"content-import-planet"},[e("p",{staticClass:"content-import-planet__left"},[t._v("Cookie")]),t._v(" "),e("el-input",{model:{value:t.planetCookie,callback:function(e){t.planetCookie=e},expression:"planetCookie"}}),t._v(" "),e("a",{staticClass:"content-import-planet__right",attrs:{href:"https://discuz.com/manual-admin/2.html#_2-10-2-知识星球cookie和user-agent",target:"_blank"}},[e("i",{staticClass:"el-icon-question"})])],1)]):t._e(),t._v(" "),5===t.contentSourceId?e("Card",[e("div",{staticClass:"content-import-planet"},[e("p",{staticClass:"content-import-planet__left"},[t._v("User-Agent")]),t._v(" "),e("el-input",{model:{value:t.planetUserAgent,callback:function(e){t.planetUserAgent=e},expression:"planetUserAgent"}}),t._v(" "),e("a",{staticClass:"content-import-planet__right",attrs:{href:"https://discuz.com/manual-admin/2.html#_2-10-2-知识星球cookie和user-agent",target:"_blank"}},[e("i",{staticClass:"el-icon-question"})])],1)]):t._e(),t._v(" "),4!==t.contentSourceId?e("Card",[e("div",{staticClass:"content-import-search"},[e("el-input",{attrs:{placeholder:"搜索想要导入站点的话题"},model:{value:t.topicContent,callback:function(e){t.topicContent=e},expression:"topicContent"}})],1)]):t._e(),t._v(" "),4===t.contentSourceId?e("Card",t._l(t.officialAccountLink,(function(n,i){return e("div",{key:i,staticClass:"content-import-official"},[e("el-input",{attrs:{placeholder:"输入想要导入公众号文章链接"},model:{value:n.linkData,callback:function(e){t.$set(n,"linkData",e)},expression:"item.linkData"}}),t._v(" "),e("div",{staticClass:"content-import-official__btn"},[i===t.officialAccountLink.length-1?e("span",{staticClass:"content-import-official__btn-iconleft",on:{click:t.increaseLink}},[e("i",{staticClass:"el-icon-circle-plus-outline"})]):t._e(),t._v(" "),1!==t.officialAccountLink.length?e("span",{staticClass:"content-import-official__btn-iconright",on:{click:function(e){return t.deleteLink(i)}}},[e("i",{staticClass:"el-icon-remove-outline"})]):t._e()])],1)})),0):t._e(),t._v(" "),4!==t.contentSourceId?e("Card",{staticClass:"content-import-layer"},[e("CardRow",{attrs:{description:"一次最多导入1000条"}},[e("div",{staticClass:"content-import-num"},[e("p",{staticClass:"content-import-num__topic"},[t._v("导入条数")]),t._v(" "),e("el-input",{attrs:{type:"number"},on:{input:t.topicNumInput},model:{value:t.topicNum,callback:function(e){t.topicNum=e},expression:"topicNum"}})],1)])],1):t._e(),t._v(" "),e("Card",{staticClass:"footer-btn"},[e("el-button",{attrs:{type:"primary",size:"medium"},on:{click:t.importDataBtn}},[t._v("提交")])],1),t._v(" "),t.speed?e("Card",[e("el-progress",{staticClass:"progress-box",attrs:{percentage:t.progress}}),t._v(" "),1===t.importing?e("p",{staticClass:"progress-box__importing"},[t._v("正在导入中")]):t._e(),t._v(" "),2===t.importing?e("div",{staticClass:"progress-box__success"},[e("p",{staticClass:"progress-box__success-confirm"},[t._v("成功导入"+t._s(t.totalDataNumber)+"条数据，稍后可在前台查看")]),t._v(" "),e("el-button",{attrs:{type:"primary",size:"medium"},on:{click:t.determineBtn}},[t._v("确认")])],1):t._e(),t._v(" "),0!==t.importing&&1!==t.importing&&2!==t.importing?e("div",{staticClass:"progress-box__fail"},[e("p",{staticClass:"progress-box__fail-fotter"},[t._v("导入失败")]),t._v(" "),e("el-button",{attrs:{type:"primary",size:"medium"},on:{click:t.retryBtn}},[t._v("重试")]),t._v(" "),e("el-button",{attrs:{size:"medium"},on:{click:t.cancelBtn}},[t._v("取消")])],1):t._e()],1):t._e()],1)},o=[]},QiPt:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=r(n("4gYi")),o=r(n("pNQN"));function r(t){return t&&t.__esModule?t:{default:t}}e.default={data:function(){return{topicContent:"",topicNum:"",speed:!1,importing:"",progress:0,startTiming:!1,contentSourceId:1,accuntlnroCookie:"",accuntlnroToken:"",planetCookie:"",planetUserAgent:"",totalNumber:0,contentSource:[{name:"微博",id:1},{name:"贴吧",id:2},{name:"豆瓣",id:3},{name:"微信公众号",id:4},{name:"知识星球",id:5}],officialAccountLink:[{linkData:""}]}},methods:{increaseLink:function(){this.officialAccountLink.length<20&&this.officialAccountLink.push({linkData:""})},deleteLink:function(t){this.officialAccountLink.length>1&&this.officialAccountLink.splice(t,1)},topicNumInput:function(t){Number(t)>1e3&&(this.$message.error("一次最多导入1000条"),this.topicNum="")},importDataBtn:function(){var t=this,e={};if(4===this.contentSourceId){var n=[];this.officialAccountLink.map((function(t){n.push(t.linkData)})),e={officialAccountUrl:n,platform:this.contentSourceId}}else e=5===this.contentSourceId?{topic:this.topicContent,cookie:this.planetCookie,userAgent:this.planetUserAgent,number:this.topicNum,platform:this.contentSourceId}:{topic:this.topicContent,number:this.topicNum,platform:this.contentSourceId};this.appFetch({url:"create_crawler_get",method:"get",data:e}).then((function(e){if(e.errors)t.$message.error(e.errors[0].code);else{if(0!==e.Code)return void t.$message.error(e.Message);t.speed=!0,clearInterval(t.timer),t.startTiming=!1,t.progress=0,t.importing=1,t.timer=setInterval(t.crawlerQuery,2e3),t.$message({message:e.Message,type:"success"})}}))},crawlerQuery:function(){var t=this;this.appFetch({url:"check_crawler_get",method:"get"}).then((function(e){if(e.errors)clearInterval(t.timer),t.$message.error(e.errors[0].code);else{if(0!==e.Code)return clearInterval(t.timer),void t.$message.error(e.Message);var n=e.Data;0!==n.startCrawlerTime&&(t.startTiming=!0,t.importing=n.status,t.progress=n.progress,0!==n.status&&1!==n.status&&2!==n.status&&clearInterval(t.timer)),t.startTiming&&(t.importing=n.status,t.progress=n.progress,2===n.status&&100===n.progress&&(t.progress=100,t.totalDataNumber=n.totalDataNumber,clearInterval(t.timer)),0!==n.status&&1!==n.status&&2!==n.status&&clearInterval(t.timer))}}))},determineBtn:function(){this.speed=!1,clearInterval(this.timer)},cancelBtn:function(){history.go(0)},retryBtn:function(){this.importDataBtn()}},components:{Card:i.default,CardRow:o.default}}},VPrg:function(t,e,n){"use strict";n.r(e);var i=n("DHhl"),o=n("gzmO");for(var r in o)["default"].indexOf(r)<0&&function(t){n.d(e,t,(function(){return o[t]}))}(r);var a=n("KHd+"),s=Object(a.a)(o.default,i.a,i.b,!1,null,null,null);e.default=s.exports},gzmO:function(t,e,n){"use strict";n.r(e);var i=n("pl4M"),o=n.n(i);for(var r in i)["default"].indexOf(r)<0&&function(t){n.d(e,t,(function(){return i[t]}))}(r);e.default=o.a},pl4M:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=r(n("QbLZ"));n("lpfh");var o=r(n("QiPt"));function r(t){return t&&t.__esModule?t:{default:t}}e.default=(0,i.default)({name:"other-service-content"},o.default)}}]);