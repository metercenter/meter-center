Ext.define('ExtMVCOne.view.Meters.View', {
    extend: 'Ext.panel.Panel',
    alias : 'widget.metersview',
    requires: [
        'Ext.layout.container.Border',
        'ExtMVCOne.view.user.List',
        'ExtMVCOne.view.user.Tree'
    ],
    layout: 'border',
//    width: 500,
//    height: 400,

    bodyBorder: false,
    
    defaults: {
        collapsible: true,
        split: true,
        bodyPadding: 10
    },

    items: [
        {
            title: '操作台',
            region: 'south',
            height: 100,
            minHeight: 75,
            maxHeight: 150,
            collapsed: true
        },
        {
            title: '用户群',
            region:'west',
            floatable: false,
            margin: '5 0 0 0',
            width: 125,
            minWidth: 200,
            maxWidth: 250,
            xtype:'treeList'
        },
        {
            title: '实时数据显示',
            collapsible: true,
            region: 'center',
            margin: '5 0 0 0',
            xtype: 'userlist',
        }
    ]

});