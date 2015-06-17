Ext.define('app.view.main.Menu',{
	extend: 'Ext.tab.Panel',
	alias: 'widget.menubar',
    requires: ['app.controller.main.MenuController'],
    // controllers: ['main.MenuController']
    controller: 'menuController',
	// flex:1,
    initComponent: function(){
    	var me = this;
    	me.items = [
    	  {title: '数据信息', id: 'datamanage', layout: 'fit'},
    	  {title: '报警信息', id: 'warninfo'},
    	  {title: '用户管理', id: 'usermanage', hidden: true}
    	];
    	me.callParent(arguments);
    }

});