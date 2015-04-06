Ext.define('ExtMVCOne.view.meter.Grid', {
  extend : 'Ext.grid.Panel',
  alias : 'widget.metergrid',
  requires : [ 'Ext.grid.column.Action' ],
  xtype : 'array-grid',
  store : 'Meter',
  stateful : true,
  scroll : 'vertical',
  collapsible : true,
  multiSelect : true,
  stateId : 'stateGrid',
  height : 350,
  title : 'Array Grid',
  viewConfig : {
    enableTextSelection : true
  },
  listeners: {
    itemdblclick: function(view, record, item, index, e, eOpts) {
      console.log(record.data.meter_eui);
//      alert(record;
//      console.log(Ext.ComponentQuery.query('#datagrid'));
      Ext.ComponentQuery.query('#datagrid')[0].store.load({
        params : {
          meter_eui : record.data.meter_eui
        },
        callback : function(records, options, success) {
        }
      });
    }
  },
  initComponent : function() {
    var me = this;

    me.width = 750;
    me.columns = [ 
//                   {
//      text : '流量计编号',
//      width : '8%',
//      sortable : false,
//      dataIndex : 'meter_id'
//    }, 
    {
      text : '用户编号',
      width : '6%',
      sortable : true,
// formatter : 'usMoney',
      dataIndex : 'user_id'
    }, {
      text : '流量计名称',
      width : '12%',
      sortable : true,
// renderer : function(val) {
// var out = Ext.util.Format.number(val, '0.00');
// if (val > 0) {
// return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
// } else if (val < 0) {
// return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
// }
// return out;
// },
      dataIndex : 'meter_name'
    }, {
      text : '流量计类型',
      width : '12%',
      sortable : true,
// renderer : function(val) {
// var out = Ext.util.Format.number(val, '0.00');
// if (val > 0) {
// return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
// } else if (val < 0) {
// return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
// }
// return out;
// },
      dataIndex : 'meter_type'
    },
    
//    {
//      text : '流量计序列号',
//      width : '12%',
//      sortable : true,
//      dataIndex : 'meter_index'
//    }, 
    
    {
      text : '流量计数据',
      width : '12%',
      sortable : true,
// renderer : function(val) {
// var out = Ext.util.Format.number(val, '0.00%');
// if (val > 0) {
// return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
// } else if (val < 0) {
// return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
// }
// return out;
// },
      dataIndex : 'user_meterdata'
    }, {
      text : '流量计标识',
      width : '12%',
      sortable : true,
      // formatter : 'date("m/d/Y")',
      dataIndex : 'meter_eui'
    }, {
      text : '流量计工况参考值',
      width : '12%',
      sortable : true,
      // formatter : 'date("m/d/Y")',
      dataIndex : 'meter_qb'
    }, {
      text : '流量计标况参考值',
      width : '12%',
      sortable : true,
      // formatter : 'date("m/d/Y")',
      dataIndex : 'meter_qm'
    }];
    
    var meterStore = new ExtMVCOne.store.Meter();
    Ext.apply(this, {
      store : meterStore,
    });
    setInterval(function() {
// _mask.hide();
// Ext.MessageBox.alert("Status", "Restart " + SelectedServer + "
// Successfully");
      meterStore.load();
     }, 60000);
    
    me.callParent();
  }
});