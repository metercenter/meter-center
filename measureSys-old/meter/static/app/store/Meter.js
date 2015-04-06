Ext.define("ExtMVCOne.store.Meter", {
  extend : "Ext.data.Store",
  model : "ExtMVCOne.model.Meter",
  alias : 'store.meter',
  batchActions : false,
  autoLoad : true,
  proxy : {
    type : 'ajax',
    url : '/get-meter',
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
//  proxy: {
//    type: "rest",
//    api: {
//        read: '/get-meter',
//        destroy: 'Users/Delete',
//        update: "Users/Edit",
//        create: "Users/Add"
//    },
//    reader: {
//        type: 'json',
//        root: "data",
//        messageProperty: "Msg"
//    },
//    writer: {
//        type: "json",
//        encode: true,
//        root: "data",
//        allowSingle: false
//    }
//}
});
