(window.webpackJsonp=window.webpackJsonp||[]).push([[57],{"0QT+":function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=r(a("QbLZ"));a("lpfh");var s=r(a("GZmH"));function r(e){return e&&e.__esModule?e:{default:e}}t.default=(0,n.default)({name:"other-service-content"},s.default)},"38SU":function(e,t,a){"use strict";a.d(t,"a",(function(){return n})),a.d(t,"b",(function(){return s}));var n=function(){var e=this,t=e._self._c;return t("div",{staticClass:"plugin-unit"},[t("Card",[t("p",{staticClass:"plugin-unit-file"},[t("a",{attrs:{href:"https://developer.discuz.chat/#/plugin/start",target:"_blank"}},[e._v("插件文档")])]),e._v(" "),t("el-upload",{staticClass:"upload-demo",attrs:{action:"","http-request":e.uploaderPlugin,"on-change":e.handleChange,"before-upload":e.beforePluginUpload}},[t("el-button",{attrs:{size:"small",type:"primary"}},[e._v("上传插件")])],1)],1),e._v(" "),t("Card",[t("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData,border:""}},[t("el-table-column",{attrs:{label:"ID"},scopedSlots:e._u([{key:"default",fn:function(a){return[t("span",[e._v(e._s(a.row.app_id))])]}}])}),e._v(" "),t("el-table-column",{attrs:{label:"英文/中文"},scopedSlots:e._u([{key:"default",fn:function(a){return[t("span",[e._v(e._s(a.row.name_en))])]}}])}),e._v(" "),t("el-table-column",{attrs:{label:"状态"},scopedSlots:e._u([{key:"default",fn:function(a){return[t("p",[e._v(e._s(1===a.row.status?"已发布":"未发布"))])]}}])}),e._v(" "),t("el-table-column",{attrs:{label:"类型"},scopedSlots:e._u([{key:"default",fn:function(a){return[t("p",[e._v(e._s(e.typeConversion(a.row.type)))])]}}])}),e._v(" "),t("el-table-column",{staticClass:"plugin-unit-post",attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(a){return[t("div",{staticClass:"plugin-unit-post__box"},[0===a.row.status?t("span",{staticClass:"plugin-unit-post__box-text",on:{click:function(t){return e.plugInRelease(a.row.app_id,1)}}},[e._v("发布")]):e._e(),e._v(" "),1===a.row.status?t("span",{staticClass:"plugin-unit-post__box-text",on:{click:function(t){return e.plugInRelease(a.row.app_id,2)}}},[e._v("下线")]):e._e(),e._v(" "),t("span",{staticClass:"plugin-unit-post__box-detal",on:{click:function(t){return e.plugInRelease(a.row.app_id,3)}}},[e._v("删除")])])]}}])})],1)],1)],1)},s=[]},GPRW:function(e,t,a){"use strict";a.r(t);var n=a("38SU"),s=a("Vqeq");for(var r in s)["default"].indexOf(r)<0&&function(e){a.d(t,e,(function(){return s[e]}))}(r);var o=a("KHd+"),u=Object(o.a)(s.default,n.a,n.b,!1,null,null,null);t.default=u.exports},GZmH:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=r(a("4gYi")),s=r(a("pNQN"));function r(e){return e&&e.__esModule?e:{default:e}}t.default={data:function(){return{tableData:[],dialogVisible:!1,fileList:[],uploadType:"",uploadDetails:""}},created:function(){this.importDataBtn()},methods:{determineBtn:function(e,t){this.uploadType=e,this.uploadDetails=t.row,this.dialogVisible=!0},plugInRelease:function(e,t){var a=this;this.appFetch({url:"panel_operate_post_v3",method:"post",data:{appId:e,operate:t}}).then((function(e){if(e.errors)a.$message.error(e.errors[0].code);else{if(0!==e.Code)return void a.$message.error(e.Message);1===t&&a.$message({message:"插件发布成功",type:"success"}),2===t&&a.$message({message:"插件下线成功",type:"success"}),3===t&&a.$message({message:"插件删除成功",type:"success"}),a.importDataBtn()}}))},handleChange:function(e,t){this.fileList=t.slice(-3)},beforePluginUpload:function(e){var t=e.size/1024/1024<20;return t},uploaderPlugin:function(e){var t=this,a=new FormData;a.append("file",e.file),this.appFetch({url:"panel_upload_post_v3",method:"post",data:a}).then((function(e){if(e.errors)t.$message.error(e.errors[0].code);else{if(0!==e.Code)return void t.$message.error(e.Message);t.$message({message:"插件上传成功",type:"success"}),t.importDataBtn()}}))},importDataBtn:function(){var e=this;this.appFetch({url:"plugin_list_get_v3",method:"get",data:{}}).then((function(t){if(t.errors)e.$message.error(t.errors[0].code);else{if(0!==t.Code)return void e.$message.error(t.Message);e.tableData=t.Data}}))},typeConversion:function(e){switch(e){case 0:return"完全自定义插件";case 1:return"帖子新增类型";case 2:return"外部数据导入";case 3:return"广告插件";case 4:return"首页banner插件";case 5:return"表情插件"}}},components:{Card:n.default,CardRow:s.default}}},Vqeq:function(e,t,a){"use strict";a.r(t);var n=a("0QT+"),s=a.n(n);for(var r in n)["default"].indexOf(r)<0&&function(e){a.d(t,e,(function(){return n[e]}))}(r);t.default=s.a}}]);