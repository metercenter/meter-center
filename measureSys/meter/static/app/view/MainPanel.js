/// <reference path="../ext.js" />
Ext.define('ExtMVCOne.view.MainPanel', {
    extend: 'Ext.tab.Panel',
    alias: 'widget.mainpanel',
    flex: 1,
    initComponent: function () {
        var me = this;

        me.items = [
            { title: "数据管理", id: "contentPanel", layout: "fit"},
            { title: "警报数据", id: "picPanel" },
            { title: "日志管理", id: "logPanel" }
        ];

//        var roles = '.' + ExtMVCOne.Userinfo.Roles.join('.') + '.';
        var roles = '.' + '系统管理员' + '.';
        if (roles.indexOf('.系统管理员.') >= 0) {
            me.items.push({ title: "用户管理", id: "userPanel", layout: "fit" });
        }
        me.callParent(arguments);
    }
});