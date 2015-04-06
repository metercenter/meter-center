Ext.define('app.view.grid.MeterData', {
  extend : 'Ext.grid.Panel',
  alias : 'widget.meterData',

  requires : [ 'Ext.data.*', 
               'Ext.grid.*', 
               'Ext.util.*', 
               'Ext.toolbar.Paging',
               'Ext.ux.ProgressBarPager', 
               'app.model.grid.MeterDataModel',
               'app.store.meterdata.MeterDataStore',
               'Ext.grid.RowNumberer' ,
               'app.view.grid.PagingTool'
               ],

  title: '实时数据',
  padding: '10 10',
  id: 'meterDataGrid',
  stripeRows: true,
  initComponent : function() {
    var me = this;
    me.columns = [ {
      text : '数据编号',
      width : 120,
      sortable : false,
      dataIndex : 'data_id'
    }, 
    
//    {
//      text : '流量计编号',
//      width : '8%',
//      sortable : true,
//      dataIndex : 'meter_id'
//    }, 
    
    {
      text : '接收时间',
      width : '12%',
      sortable : true,
      dataIndex : 'data_date'
    }, {
      text : '标况总累计(Nm3)',
      width : '12%',
      sortable : true,
      dataIndex : 'data_vb'
    }, {
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
    }, ];
    var store = Ext.create('store.meterDataStore');
    Ext.apply(this, {
      store : store,
      bbar : {
        xtype : 'pagingToolBarRefresh',
        pageSize : 10,
        store : store,
        displayInfo : true,
        plugins : new Ext.ux.ProgressBarPager()
      }
    });

    this.callParent();
  }
});