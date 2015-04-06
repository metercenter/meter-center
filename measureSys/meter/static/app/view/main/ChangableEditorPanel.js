Ext.define('app.view.main.ChangableEditorPanel', {
	extend: 'Ext.panel.Panel',
    alias: 'widget.changableEditorPanel',

    requires: [
                 'app.view.introduction.Introduction',
                 'app.view.editorPanelContent.AddUser',
                 'app.view.editorPanelContent.AddMeter'
              ],

	layout: 'fit',
	collapsible: true,

	items: [{
			xtype: 'addUser'
		},{
			xtype: 'addMeter',
			hidden: true
		}],

	initComponent: function() {
		var me = this;
		// var userPanel = Ext.create('app.view.editorPanelContent.AddUser');
		this.callParent();
	}

});