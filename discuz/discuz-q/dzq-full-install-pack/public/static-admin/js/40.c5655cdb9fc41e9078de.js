(window.webpackJsonp=window.webpackJsonp||[]).push([[40],{"6a5c":function(e,t,r){"use strict";r.d(t,"a",(function(){return a})),r.d(t,"b",(function(){return n}));var a=function(){var e=this,t=e._self._c;return t("div",{staticClass:"report-manage-box"},[t("div",{staticClass:"report-manage-header"},[t("div",{staticClass:"report-manage-header__section"},[t("span",{staticClass:"report-manage-header__section-title"},[e._v("举报人：")]),e._v(" "),t("el-input",{attrs:{size:"medium",clearable:""},model:{value:e.searchData.userName,callback:function(t){e.$set(e.searchData,"userName",t)},expression:"searchData.userName"}})],1),e._v(" "),t("div",{staticClass:"report-manage-header__section"},[t("span",{staticClass:"report-manage-header__section-title"},[e._v("举报类型：")]),e._v(" "),t("el-select",{attrs:{clearable:"",size:"medium"},model:{value:e.searchData.reportType,callback:function(t){e.$set(e.searchData,"reportType",t)},expression:"searchData.reportType"}},e._l(e.reportTypeData,(function(e){return t("el-option",{key:e.id,attrs:{label:e.name,value:e.id}})})),1)],1),e._v(" "),t("div",{staticClass:"report-manage-header__section"},[t("span",{staticClass:"report-manage-header__section-title time-title"},[e._v("举报时间范围：")]),e._v(" "),t("el-date-picker",{attrs:{"value-format":"yyyy-MM-dd",type:"daterange",align:"right","unlink-panels":"",size:"medium","range-separator":"至","start-placeholder":"开始日期","end-placeholder":"结束日期"},model:{value:e.searchData.reportTime,callback:function(t){e.$set(e.searchData,"reportTime",t)},expression:"searchData.reportTime"}})],1),e._v(" "),t("div",{staticClass:"report-manage-header__section"},[t("el-button",{attrs:{size:"small",type:"primary"},on:{click:e.searchClick}},[e._v("搜索")])],1)]),e._v(" "),t("div",{staticClass:"report-manage-content"},[t("div",{staticClass:"report-manage-content__header"},[t("el-checkbox",{attrs:{indeterminate:e.isIndeterminate},on:{change:e.handleCheckAllChange},model:{value:e.checkAll,callback:function(t){e.checkAll=t},expression:"checkAll"}}),e._v(" "),t("p",{staticClass:"report-manage-content__header-title"},[e._v("举报列表")])],1),e._v(" "),e._l(e.reportList,(function(r){return t("ContArrange",{key:r.report.id,staticClass:"report-manage-content__table",attrs:{establish:r.user.userName?r.user.userName:"该用户被删除",userId:r.user.pid?r.user.pid:"该用户被删除",time:e.formatDate(r.report.createdAt),type:e.getType(r.report.type)}},[t("div",{staticClass:"report-manage-content__table-side",attrs:{slot:"side"},slot:"side"},[t("el-checkbox",{attrs:{label:r.report.id},on:{change:function(t){return e.handleCheckedCitiesChange()}},model:{value:e.checkedReport,callback:function(t){e.checkedReport=t},expression:"checkedReport"}})],1),e._v(" "),t("div",{staticClass:"report-manage-content__table-main",attrs:{slot:"main"},slot:"main"},[t("p",[e._v("\n\t\t\t\t\t\t页面地址：\n\t\t\t\t\t\t"),t("a",{staticStyle:{color:"#3E4043"},attrs:{href:e.getUrl(r.user.pid,r.report.threadId,r.report.postId).href,target:"_blank"}},[e._v("\n\t\t\t\t\t\t\t"+e._s(e.getUrl(r.user.pid,r.report.threadId,r.report.postId).url)+"\n\t\t\t\t\t\t")])]),e._v(" "),t("p",[e._v("举报时间："+e._s(e.formatDate(r.report.updatedAt)))]),e._v(" "),t("p",[e._v("举报理由：")]),e._v(" "),t("p",[e._v(e._s(r.report.reason))])]),e._v(" "),t("div",{staticClass:"report-manage-content__table-footer",attrs:{slot:"footer"},slot:"footer"},[t("el-popover",{ref:"popover-"+e.index,refInFor:!0,attrs:{width:"100",placement:"top"}},[t("p",[e._v("确定删除该项吗？")]),e._v(" "),t("div",{staticStyle:{"text-align":"right",margin:"10PX 0 0 0"}},[t("el-button",{attrs:{type:"danger",size:"mini"},on:{click:function(t){return e.closeDelet("popover-"+e.index)}}},[e._v("\n                  取消\n                ")]),e._v(" "),t("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(t){e.deleteOperation(1,r.report.id),e.closeDelet("popover-"+e.index)}}},[e._v("确定")])],1),e._v(" "),t("el-button",{attrs:{slot:"reference",type:"text"},slot:"reference"},[e._v("删除")])],1)],1)])})),e._v(" "),t("tableNoList",{directives:[{name:"show",rawName:"v-show",value:e.reportList.length<1,expression:"reportList.length < 1"}]}),e._v(" "),e.pageData.pageCount>1?t("Page",{attrs:{"current-page":e.pageData.pageNumber,"page-size":e.pageData.pageSize,total:e.pageData.pageTotal},on:{"current-change":e.handleCurrentChange}}):e._e()],2),e._v(" "),t("div",{staticClass:"report-manage-footer"},[t("el-popover",{attrs:{width:"100",placement:"top"},model:{value:e.visible,callback:function(t){e.visible=t},expression:"visible"}},[t("p",[e._v("确定删除该项吗？")]),e._v(" "),t("div",{staticStyle:{"text-align":"right",margin:"10PX 0 0 0"}},[t("el-button",{attrs:{type:"danger",size:"mini"},on:{click:function(t){e.visible=!1}}},[e._v("\n                  取消\n                ")]),e._v(" "),t("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(t){e.deleteOperation(2),e.visible=!1}}},[e._v("确定")])],1),e._v(" "),t("el-button",{attrs:{slot:"reference",size:"small",type:"primary",loading:e.subLoading},slot:"reference"},[e._v("全部删除")])],1)],1)])},n=[]},EY1w:function(e,t,r){"use strict";r.r(t);var a=r("6a5c"),n=r("tLGw");for(var s in n)["default"].indexOf(s)<0&&function(e){r.d(t,e,(function(){return n[e]}))}(s);var i=r("KHd+"),o=Object(i.a)(n.default,a.a,a.b,!1,null,null,null);t.default=o.exports},"GXs+":function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=s(r("QbLZ"));r("lL+3");var n=s(r("QMoF"));function s(e){return e&&e.__esModule?e:{default:e}}t.default=(0,a.default)({name:"report-processed-view"},n.default)},"KHd+":function(e,t,r){"use strict";function a(e,t,r,a,n,s,i,o){var l,c="function"==typeof e?e.options:e;if(t&&(c.render=t,c.staticRenderFns=r,c._compiled=!0),a&&(c.functional=!0),s&&(c._scopeId="data-v-"+s),i?(l=function(e){(e=e||this.$vnode&&this.$vnode.ssrContext||this.parent&&this.parent.$vnode&&this.parent.$vnode.ssrContext)||"undefined"==typeof __VUE_SSR_CONTEXT__||(e=__VUE_SSR_CONTEXT__),n&&n.call(this,e),e&&e._registeredComponents&&e._registeredComponents.add(i)},c._ssrRegister=l):n&&(l=o?function(){n.call(this,(c.functional?this.parent:this).$root.$options.shadowRoot)}:n),l)if(c.functional){c._injectStyles=l;var p=c.render;c.render=function(e,t){return l.call(t),p(e,t)}}else{var d=c.beforeCreate;c.beforeCreate=d?[].concat(d,l):[l]}return{exports:e,options:c}}r.d(t,"a",(function(){return a}))},QMoF:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=o(r("Dt3C")),n=o(r("rWG0")),s=o(r("7qpD")),i=o(r("VVfg"));function o(e){return e&&e.__esModule?e:{default:e}}t.default={data:function(){return{isIndeterminate:!1,checkAll:!1,reportListAll:[],checkedReport:[],reportList:[],pageData:{pageSize:10,pageCount:1,pageNumber:1,pageTotal:0},searchData:{userName:"",reportType:null,reportTime:["",""],status:0},reportTypeData:[{name:"主题",id:1},{name:"评论/回复",id:2}],subLoading:!1,visible:!1}},methods:{closeDelet:function(e){this.$refs[e][0].doClose()},handleCheckAllChange:function(e){this.checkedReport=e?this.reportListAll:[],this.isIndeterminate=!1},handleCheckedCitiesChange:function(){var e=this.checkedReport.length;this.checkAll=e===this.reportListAll.length,this.isIndeterminate=e>0&&e<this.reportListAll.length},formatDate:function(e){return this.$dayjs(e).format("YYYY-MM-DD HH:mm")},getType:function(e){return 0===e?"个人主页":1===e?"主题":2===e?"评论/回复":void 0},getUrl:function(e,t,r){var a="";return{href:a=0===r?0===t?"/user/"+e:"/thread/"+t:"/thread/comment/"+r+"?threadId="+t,url:window.origin+a}},searchClick:function(){this.searchData.reportTime=null==this.searchData.reportTime?["",""]:this.searchData.reportTime,this.searchData.reportType=""===this.searchData.reportType?null:this.searchData.reportType,this.pageData.pageNumber=1,this.getReportList(1)},getReportList:function(e){var t=this,r=this.searchData;this.appFetch({url:"reports_get_v3",method:"get",data:{"filter[username]":r.userName,"filter[status]":1,"filter[type]":r.reportType,"filter[startTime]":r.reportTime[0],"filter[endTime]":r.reportTime[1],page:e,perPage:this.pageData.pageSize}}).then((function(e){if(e.errors)t.$message.error(e.errors[0].code);else{if(0!==e.Code)return void t.$message.error(e.Message);var r=e.Data;t.reportList=r.pageData||[],t.pageData.pageTotal=r.totalCount,t.pageData.pageCount=r.totalPage,t.reportListAll=[],t.reportList.forEach((function(e){t.reportListAll.push(e.report.id)}))}}))},handleCurrentChange:function(e){this.checkedReport=[],this.pageData.pageNumber=e,this.getReportList(e)},deleteOperation:function(e,t){var r=this,a=this,n="";if(1===e)n=t;else{if(this.checkedReport.length<1)return void this.$message({showClose:!0,message:"操作举报列表为空，请选择举报信息",type:"warning"});this.subLoading=!0,n=this.checkedReport.toString()}this.appFetch({url:"reports_delete_v3",method:"post",data:{ids:n}}).then((function(t){0===t.Code?(a.subLoading=!1,a.$message({message:"删除成功",type:"success"}),1!==e&&(a.checkAll=!1),a.getReportList(Number(i.default.getLItem("pageNumber"))||1)):r.$message.error(t.Message)}))},getCreated:function(e){e?this.getReportList(1):this.getReportList(Number(i.default.getLItem("pageNumber"))||1)}},created:function(){this.getUrl()},beforeDestroy:function(){i.default.setLItem("pageNumber",1)},beforeRouteEnter:function(e,t,r){r((function(r){e.name!==t.name&&null!==t.name?r.getCreated(!0):r.getCreated(!1)}))},components:{ContArrange:a.default,Page:n.default,tableNoList:s.default}}},tLGw:function(e,t,r){"use strict";r.r(t);var a=r("GXs+"),n=r.n(a);for(var s in a)["default"].indexOf(s)<0&&function(e){r.d(t,e,(function(){return a[e]}))}(s);t.default=n.a}}]);