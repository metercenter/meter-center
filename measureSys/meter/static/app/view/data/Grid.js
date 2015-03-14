Ext.define('ExtMVCOne.view.data.Grid', {
  extend : 'Ext.grid.Panel',
  alias : 'widget.datagrid',
  requires : [ 'Ext.grid.column.Action' ],
  xtype : 'array-grid',
  //    store: dataStore,
  stateful : true,
  collapsible : true,
  scroll : 'vertical',
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
      text : '数据编号',
      width : '6%',
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
    //         var store = new 
    var dataStore = new ExtMVCOne.store.Data();
    Ext.apply(this, {
      store : dataStore,
    });
    setInterval(function() {
//      _mask.hide();
//      Ext.MessageBox.alert("Status", "Restart " + SelectedServer + " Successfully");
      dataStore.load();
     }, 60000);
    
    me.callParent();
  }
});