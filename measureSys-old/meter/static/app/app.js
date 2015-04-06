/**
 * 
 */

Ext.application({
    name: "ExtMVCOne",
    appFolder: '/static/app',
    controllers: ["MainPanel"],
    autoCreateViewport: true,
    launch: function () {
        // 页面加载完成之后执行
      console.log(this.controllers);
    }
});