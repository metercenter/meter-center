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
