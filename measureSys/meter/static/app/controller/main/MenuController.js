Ext.define('app.controller.main.MenuController', {
	extend: 'Ext.app.ViewController',
	alias: 'controller.menuController',
    requires:[
              'app.store.tree.UserTreeStore',
              'app.store.tree.SelectPanelStore',
              'app.store.tree.SelectMeterStore',
              'app.store.meterdata.MeterDataStore'
            ],

	init: function() {
			this.control({
				'#datamanage': {
					activate: {
						//single: true,
						fn: function (panel) {
							Ext.ComponentQuery.query('#dataarea')[0].setHidden(false);
							Ext.ComponentQuery.query('#warnarea')[0].setHidden(true);
						}
					}
				},
			
				'#warninfo': {
					activate: {
						//single: true,
						fn: function (panel) {
							Ext.MessageBox.alert('提示', 'test');
							Ext.ComponentQuery.query('#dataarea')[0].setHidden(true);
							Ext.ComponentQuery.query('#warnarea')[0].setHidden(false);
						}
					}
				},
				
				'#usermanage': {
					activate: {
						single: true,
						fn: function (panel) {
						}
					}
				}
		})
	}
});