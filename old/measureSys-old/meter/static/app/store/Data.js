Ext.define('ExtMVCOne.store.Data', {
    extend: 'Ext.data.Store',
    alias: 'store.data',
    model: 'ExtMVCOne.model.Data',
    batchActions : false,
    autoLoad : true,
    proxy : {
      type : 'ajax',
      url : '/get-data',
      reader : {
        type : 'json',
        root : "data",
        messageProperty : "Msg"
      },
      writer : {
        type : "json",
        encode : true,
        root : "data",
        allowSingle : false
      }
    }
});

//var dataStore = new ExtMVCOne.store.Data();

//var dataStore = Ext.create('Ext.data.Store', {
//  model : 'ExtMVCOne.model.Data',
//  batchActions : false,
//  // //autoLoad : true,
//  proxy : {
//    type : 'ajax',
//    url : '/get-data',
//    reader : {
//      type : 'json',
//      root : "data",
//      messageProperty : "Msg"
//    },
//    writer : {
//      type : "json",
//      encode : true,
//      root : "data",
//      allowSingle : false
//    }
//  }
//});
//
//dataStore.load({
//  params:{user_name: '0001'},
//  callback : function(records, options, success) {
//    Ext.Msg.alert('info', '加载完毕');
//  }
//});
