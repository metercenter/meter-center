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

  initComponent : function() {
    var me = this;

    me.width = 750;
    me.columns = [ {
      text : '流量计编号',
      width : '12%',
      sortable : false,
      dataIndex : 'meter_id'
    }, {
      text : '用户编号',
      width : '12%',
      sortable : true,
//      formatter : 'usMoney',
      dataIndex : 'user_id'
    }, {
      text : '流量计名称',
      width : '12%',
      sortable : true,
//      renderer : function(val) {
//        var out = Ext.util.Format.number(val, '0.00');
//        if (val > 0) {
//          return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
//        } else if (val < 0) {
//          return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
//        }
//        return out;
//      },
      dataIndex : 'meter_name'
    }, {
      text : '流量计类型',
      width : '12%',
      sortable : true,
//      renderer : function(val) {
//        var out = Ext.util.Format.number(val, '0.00');
//        if (val > 0) {
//          return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
//        } else if (val < 0) {
//          return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
//        }
//        return out;
//      },
      dataIndex : 'meter_type'
    },{
      text : '流量计序列号',
      width : '12%',
      sortable : true,
//      renderer : function(val) {
//        var out = Ext.util.Format.number(val, '0.00%');
//        if (val > 0) {
//          return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
//        } else if (val < 0) {
//          return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
//        }
//        return out;
//      },
      dataIndex : 'meter_index'
    }, {
      text : '流量计数据',
      width : '12%',
      sortable : true,
//      renderer : function(val) {
//        var out = Ext.util.Format.number(val, '0.00%');
//        if (val > 0) {
//          return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
//        } else if (val < 0) {
//          return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
//        }
//        return out;
//      },
      dataIndex : 'user_meterdata'
    }, {
      text : '流量计标识',
      width : '12%',
      sortable : true,
      //formatter : 'date("m/d/Y")',
      dataIndex : 'meter_eui'
    }, {
      text : '用户校准',
      width : '12%',
      sortable : true,
      //formatter : 'date("m/d/Y")',
      dataIndex : 'user_revise'
    }, {
      text : '校准编号',
      width : '12%',
      sortable : true,
      //formatter : 'date("m/d/Y")',
      dataIndex : 'user_reviseid'
    }, 
//    {
//      menuDisabled : true,
//      sortable : false,
//      xtype : 'actioncolumn',
//      width : 50,
//      items : [ {
//        iconCls : 'sell-col',
//        tooltip : 'Sell stock',
//        handler : function(grid, rowIndex, colIndex) {
//          var rec = grid.getStore().getAt(rowIndex);
//          Ext.Msg.alert('Sell', 'Sell ' + rec.get('name'));
//        }
//      }, {
//        getClass : function(v, meta, rec) {
//          if (rec.get('change') < 0) {
//            return 'alert-col';
//          } else {
//            return 'buy-col';
//          }
//        },
//        getTip : function(v, meta, rec) {
//          if (rec.get('change') < 0) {
//            return 'Hold stock';
//          } else {
//            return 'Buy stock';
//          }
//        },
//        handler : function(grid, rowIndex, colIndex) {
//          var rec = grid.getStore().getAt(rowIndex), action = (rec.get('change') < 0 ? 'Hold' : 'Buy');
//
//          Ext.Msg.alert(action, action + ' ' + rec.get('name'));
//        }
//      } ]
//    } 
    ];

    me.callParent();
  }
});