Ext.define('ExtMVCOne.view.warn.View', {
    extend: 'Ext.grid.Panel',
    alias: 'widget.warnview',
    requires: ["Ext.ux.CheckColumn"],
    title: "警报信息",
    id: "warnView",
    store: "Warn",
    initComponent: function () {
        var me = this;
        me.columns = [
        { text: '接收时间', dataIndex: 'data_date', flex: 1 },
        { text: '标况总累计', dataIndex: 'data_vb', flex: 1 },
        { text: '工况总累计', dataIndex: 'data_vm', flex: 1 },
        { text: '压力', dataIndex: 'data_p', flex: 1 },
//        { xtype: "datecolumn", text: '创建时间', dataIndex: 'Created', format: "Y-m-d H:i:s", width: 150 },
//        { xtype: "datecolumn", text: '最后登录时间', dataIndex: 'Created', format: "Y-m-d H:i:s", width: 150 },
//        { xtype: 'checkcolumn', dataIndex: "IsApproved", text: "允许登录", winth: 150 }
    ]

    me.tbar = {
        xtype: "pagingtoolbar",
        pageSize: 50, displayInfo: true, store: me.store
    }

//    me.bbar = ["双击用户可进入编辑状态，用户密码默认为“123456”。重置密码可将用户密码重置为“123456”。"]

        me.callParent(arguments);
    }
});
