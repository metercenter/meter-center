Ext.define('ExtMVCOne.view.data.Grid', {
    extend: 'Ext.grid.Panel',
    alias: 'widget.datagrid',
    requires: [
        'Ext.grid.column.Action'
    ],
    xtype: 'array-grid',
    store: 'Data',
    stateful: true,
    collapsible: true,
    scroll:'vertical',
    multiSelect: true,
    stateId: 'stateGrid',
    height: 350,
    title: 'Array Grid',
    viewConfig: {
        enableTextSelection: true
    },

    initComponent: function () {
        var me = this;

        me.width = 750;
//        me.columns = [
//            {
//                text     : 'Company',
//                flex     : 1,
//                sortable : false,
//                dataIndex: 'name'
//            },
//            {
//                text     : 'Price',
//                width    : 95,
//                sortable : true,
//                formatter: 'usMoney',
//                dataIndex: 'price'
//            },
//            {
//                text     : 'Change',
//                width    : 80,
//                sortable : true,
//                renderer : function(val) {
//                    var out = Ext.util.Format.number(val, '0.00');
//                    if (val > 0) {
//                        return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
//                    } else if (val < 0) {
//                        return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
//                    }
//                    return out;
//                },
//                dataIndex: 'change'
//            },
//            {
//                text     : '% Change',
//                width    : 100,
//                sortable : true,
//                renderer : function(val) {
//                    var out = Ext.util.Format.number(val, '0.00%');
//                    if (val > 0) {
//                        return '<span style="color:' + "#73b51e" + ';">' + out + '</span>';
//                    } else if (val < 0) {
//                        return '<span style="color:' + "#cf4c35" + ';">' + out + '</span>';
//                    }
//                    return out;
//                },
//                dataIndex: 'pctChange'
//            },
//            {
//                text     : 'Last Updated',
//                width    : 115,
//                sortable : true,
//                formatter: 'date("m/d/Y")',
//                dataIndex: 'lastChange'
//            },
//            {
//                menuDisabled: true,
//                sortable: false,
//                xtype: 'actioncolumn',
//                width: 50,
//                items: [{
//                    iconCls: 'sell-col',
//                    tooltip: 'Sell stock',
//                    handler: function(grid, rowIndex, colIndex) {
//                        var rec = grid.getStore().getAt(rowIndex);
//                        Ext.Msg.alert('Sell', 'Sell ' + rec.get('name'));
//                    }
//                }, {
//                    getClass: function(v, meta, rec) {
//                        if (rec.get('change') < 0) {
//                            return 'alert-col';
//                        } else {
//                            return 'buy-col';
//                        }
//                    },
//                    getTip: function(v, meta, rec) {
//                        if (rec.get('change') < 0) {
//                            return 'Hold stock';
//                        } else {
//                            return 'Buy stock';
//                        }
//                    },
//                    handler: function(grid, rowIndex, colIndex) {
//                        var rec = grid.getStore().getAt(rowIndex),
//                            action = (rec.get('change') < 0 ? 'Hold' : 'Buy');
//
//                        Ext.Msg.alert(action, action + ' ' + rec.get('name'));
//                    }
//                }]
//            }
//        ];
        
        me.columns = [ {
          text : '数据编号',
          width : '6%',
          sortable : false,
          dataIndex : 'data_id'
        }, {
          text : '流量计编号',
          width : '8%',
          sortable : true,
          dataIndex : 'meter_id'
        }, {
          text : '接收时间',
          width : '12%',
          sortable : true,
          dataIndex : 'data_date'
        }, {
          text : '标况总累计(Nm3)',
          width : '12%',
          sortable : true,
          dataIndex : 'data_vb'
        },{
          text : '工况总累计(m3)',
          width : '12%',
          sortable : true,
          dataIndex : 'data_vm'
        }, {
          text : '压力',
          width : '12%',
          sortable : true,
          dataIndex : 'data_p'
        }, {
          text : '温度',
          width : '12%',
          sortable : true,
          dataIndex : 'data_t'
        }, {
          text : '标况瞬时流量(Nm3/h)',
          width : '12%',
          sortable : true,
          dataIndex : 'data_qb'
        }, {
          text : '工况瞬时流量(m3/h)',
          width : '12%',
          sortable : true,
          dataIndex : 'data_qm'
        }, 
        ];
        me.callParent();
    }
});