Ext.define('ExtMVCOne.view.metertype.MeterType', {
  extend : 'Ext.form.ComboBox',
  alias : 'widget.meterType',
//  requires : [ 'Ext.grid.column.Action' ],
  store: 'UserLevel',
  queryMode: 'local',
  displayField: 'user_company',
  valueField: 'user_id',

  initComponent : function() {
    var me = this;
    me.callParent();
  }
});