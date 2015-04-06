Ext.define('app.view.main.Menu',{
	extend: 'Ext.tab.Panel',
	alias: 'widget.menubar',
    requires: ['app.controller.main.MenuController'],
    // controllers: ['main.MenuController']
    controller: 'menubarController',
	// flex:1,
    initComponent: function(){
    	var me = this;
    	me.items = [
    	  {title: 'Data Management', id: 'dm', layout: 'fit'},
    	  {title: 'Warning Information', id: 'wi'},
    	  {title: 'user Manangement', id: 'um'}
    	];
    	me.callParent(arguments);
    }

});