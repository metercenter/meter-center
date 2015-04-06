Ext.define('app.controller.main.MenuController', {
	extend: 'Ext.app.ViewController',
	alias: 'controller.menubarController',

	refs: [{
		ref: 'AddUser', selector: 'addUser'
	}, {
		ref: 'AddMeter', selector: 'addMeter'
	}],

	views:  [
				'editorPanelContent.AddMeter',
				'editorPanelContent.AddUser',
				'main.Menu'
			],

	init: function() {
			this.control({
				'addUser panel': {
					setHidden: this.setHidden()
				},
				'#wi': {
					single: true,
					activate: {
						fn: this.doClick()
					}
				}
		})
	},

	setHidden : function(){
	},

	doClick: function(){
		// alert('nihao')
	}

});