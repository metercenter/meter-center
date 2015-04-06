Ext.define('ExtMVCOne.view.Users.View', {
    extend: 'Ext.grid.Panel',
    alias: 'widget.usersview',
    requires: ["Ext.ux.CheckColumn"],
    title: "用户管理",
    id: "usersView",
    store: "Users",
    initComponent: function () {
        var me = this;
        me.columns = [
        { text: '客户名称', dataIndex: 'user_company', flex: 1 },
        { text: '客户电话', dataIndex: 'user_phone', flex: 1 },
        { text: '用户名', dataIndex: 'user_name', flex: 1 },
        { text: '密码', dataIndex: 'user_password', flex: 1 },
//        { xtype: "datecolumn", text: '创建时间', dataIndex: 'Created', format: "Y-m-d H:i:s", width: 150 },
//        { xtype: "datecolumn", text: '最后登录时间', dataIndex: 'Created', format: "Y-m-d H:i:s", width: 150 },
        { xtype: 'checkcolumn', dataIndex: "IsApproved", text: "允许登录", winth: 150 }
    ]

    me.tbar = {
        xtype: "pagingtoolbar",
        pageSize: 50, displayInfo: true, store: me.store
    }

//    me.bbar = ["双击用户可进入编辑状态，用户密码默认为“123456”。重置密码可将用户密码重置为“123456”。"]

        me.callParent(arguments);
    }
});
