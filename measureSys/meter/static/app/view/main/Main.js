Ext.define('app.view.main.Main', {
    extend: 'Ext.container.Container',
    layout: 'border',
    requires:['app.view.main.BrowseArea'],
    items: [{
        region: 'north',
        xtype : 'component',
        id : "North",
        cls: 'logo',
        html: '<h1 class="header">金昇计量管理系统</h1><div class="test"><ul><li><a href="javascript:alert(\'请联系宋争，他再找人\')">联系我们</a></li><li><a href="logout">退出</a></li><li><a href="main">刷新</a></li><li><a href="main">首页</a></li></ul></div>',
        border: false,
        height: 50,
        margin: '0 0 5 0'
    }, {
        region: 'center',
        xtype: 'browseArea', // TabPanel itself has no title
    }, {
        region:'south',
        xtype : 'component',
        id: "South",
        height: 8
    }]

});
