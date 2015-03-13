Ext.define('ExtMVCOne.view.userLevel.UserLevel', {
  extend : 'Ext.form.ComboBox',
  alias : 'widget.userLevel',
//  requires : [ 'Ext.grid.column.Action' ],
  fieldLabel: 'Choose State',
  store: 'UserLevel',
  queryMode: 'local',
  displayField: 'user_company',
  valueField: 'user_id',

  initComponent : function() {
    var me = this;
    me.callParent();
  }
});