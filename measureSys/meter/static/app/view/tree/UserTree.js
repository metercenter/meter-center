Ext.define('app.view.tree.UserTree', {
    extend:'Ext.tree.Panel',
    alias:'widget.userTree',
    requires:[
      'app.store.tree.UserTreeStore',
      'app.store.tree.SelectPanelStore',
      'app.store.tree.SelectMeterStore',
      'app.store.meterdata.MeterDataStore'
    ],
    id: 'userTree',
    autoScroll:true,
    scroll:'vertical',
    useArrows:true,
    stateful:false,
    border:true,
    rootVisible:true,
    config:{
      deplacementDepart:null
    },
    viewConfig:{
      loadMask:false,
      plugins:{
          ptype:'treeviewdragdrop',
          expandDelay:100
       }
    },
    listeners: {
      itemclick: function(view, record, item, index, e, eOpts) {
        var selectStore = Ext.create('store.selectPanelStore');
//        Ext.ComponentQuery.query('#meterFieldset')[0].setDisabled(true);
        selectStore.load({
          params : {
            user_name : record.data.text
          },
          callback : function(records, options, success) {
            Ext.ComponentQuery.query('#operationarea')[0].setTitle ( record.data.text+'---数据信息');
            Ext.ComponentQuery.query('#userTree')[0].selectPanel(records[0].data.user_id, records[0].data.user_company);
          }
        });
      }
    },

  initComponent: function() {
        var store = Ext.create('store.userTreeStore');
        Ext.apply(this, {
            store: store,
        });
        this.rootVisible = false;
        var selectStore = Ext.create('store.selectPanelStore');
        
        selectStore.load({
          callback : function(records, options, success) {
            Ext.ComponentQuery.query('#operationarea')[0].setTitle ( records[0].data.user_company+'---数据信息');
            Ext.ComponentQuery.query('#userTree')[0].selectPanel(records[0].data.user_id, records[0].data.user_company);
          }
        });
        this.callParent(arguments);
    },
    
    selectPanel: function (user_id, company) {
      var len = user_id.length;
      var timer;
      
      
      if(len == 2){
        Ext.ComponentQuery.query('#companycontainer')[0].setHidden(false);
      }else{
        Ext.ComponentQuery.query('#companycontainer')[0].setHidden(true);
      }
      
      if(len == 4 && company != '检定中心'){
        Ext.ComponentQuery.query('#gascoperationcontainer')[0].setHidden(false);
      }else{
        Ext.ComponentQuery.query('#gascoperationcontainer')[0].setHidden(true);
        if (company == '检定中心') {
          Ext.ComponentQuery.query('#identifycontainer')[0].setHidden(false);
        }else{
          Ext.ComponentQuery.query('#identifycontainer')[0].setHidden(true);
        }
      }
      
      if(len == 8){
        Ext.ComponentQuery.query('#chartcontainer')[0].setHidden(false);
      }else{
        Ext.ComponentQuery.query('#chartcontainer')[0].setHidden(true);
      }
      
      
      if(len > 8){
//          timer = setInterval(function() {
//          Ext.ComponentQuery.query('#meterDataGrid')[0].store.load({
//            params : {
//              user_name : company
//            }
//          });
//       }, 6000);
        Ext.ComponentQuery.query('#metercontainer')[0].setHidden(false);
        var selectMeterStore = Ext.create('store.selectMeterStore');
        Ext.ComponentQuery.query('#browseArea')[0].userName = company;
        selectMeterStore.load({
          params : {
            user_id : user_id
          },
          callback : function(records, options, success) {
            Ext.ComponentQuery.query('#meterbasicInfo')[0].getForm().setValues({
              meter_name:records[0].data.meter_name,
              meter_version: records[0].data.meter_index,
              meter_type: records[0].data.meter_type,
              meter_eui: records[0].data.meter_eui
            });
            Ext.ComponentQuery.query('#meterDataGrid')[0].store.load({
              params : {
                user_name : company
              }
            });
          }
        });  
       
      }else{
        Ext.ComponentQuery.query('#metercontainer')[0].setHidden(true);
      } 
    }
});