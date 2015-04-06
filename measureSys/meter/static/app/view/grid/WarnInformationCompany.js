Ext.define('app.view.grid.WarnInformationCompany',{
  extend: 'Ext.grid.Panel',
  alias: 'widget.warnInformationCompany',
  requires: [
             'Ext.data.*',
             'Ext.grid.*',
             'Ext.util.*',
             'Ext.toolbar.Paging',
             'Ext.ux.ProgressBarPager',
             'app.model.grid.WarnInformationModel',
             'app.store.grid.WarnInformationStore'
         ],
  
  
  title:'重要报警信息',
  padding:'10 10',
  
  initComponent: function(){
    var store = Ext.create('store.warnInformationStore');
    Ext.apply(this, {
          store: store,
          columns: [{ 
              text: '用户',
              sortable: true,
              dataIndex: 'user_id',
//              flex: 1
              width: 75
          },{
              text: '企业名称',
              sortable: true,
//              formatter: 'usMoney',
              dataIndex: 'company',
              width: 75
          },{
              text: '表计信息',
              sortable: true,
              renderer: this.changeRenderer,
              dataIndex: 'meter_info',
              width: 80
          },{
              text: '报警信息',
              sortable: true,
              renderer: this.pctChangeRenderer,
              dataIndex: 'warn_info',
              width: 100
          },{
              text: '处理方法',
              sortable: true,
              dataIndex: 'solution',
              width: 115,
//              formatter: 'date("m/d/Y")'
          },{
            
              text: '其他',
              sortable: true,
              dataIndex: 'other',
              width: 115,
          }],

          bbar: {
              xtype: 'pagingtoolbar',
              pageSize: 10,
              store: store,
              displayInfo: true,
              plugins: new Ext.ux.ProgressBarPager()
          }
      });
  
  this.callParent();
  }
});