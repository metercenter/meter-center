Ext.define('app.store.meterdata.MeterDataStore',{
  extend: 'Ext.data.Store',
  alias: 'store.meterDataStore',
  requires: [
              'app.model.grid.MeterDataModel'
             ],
  model: 'app.model.grid.MeterDataModel',
  batchActions : false,
//  autoLoad : true,
  proxy : {
    type : 'ajax',
    url : '/get-data',
    extraParams : {user_name:Ext.ComponentQuery.query('#browseArea')[0] == null? '123':Ext.ComponentQuery.query('#browseArea')[0].userName},  
    reader : {
      type : 'json',
      rootProperty : "data",
      messageProperty : "Msg"
    },
    writer : {
      type : "json",
      encode : true,
      rootProperty : "data",
      allowSingle : false
    }
  }
});