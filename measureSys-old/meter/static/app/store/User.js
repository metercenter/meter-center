/**
 * 
 */

//Ext.define("ExtMVCOne.store.User", {
//    extend: "Ext.data.Store",
//    model: "ExtMVCOne.model.User",
//    data: [
//        { name: "Tom", age: 5, phone: "123456" },
//        { name: "Jerry", age: 3, phone: "654321" }
//    ]
//});

Ext.define("ExtMVCOne.store.User", {
  extend: "Ext.data.Store",
  model: "ExtMVCOne.model.User",
  autoLoad: true,
  autoSync: true,
  proxy: {
      type: 'rest',
      url: '/users',
      reader: {
          type: 'json',
          rootProperty: 'data'
      },
      writer: {
          type: 'json'
      }
  },
  listeners: {
//      write: function(store, operation){
//          var record = operation.getRecords()[0],
//              name = Ext.String.capitalize(operation.action),
//              verb;
//              
//              
//          if (name == 'Destroy') {
//              verb = 'Destroyed';
//          } else {
//              verb = name + 'd';
//          }
//          Ext.example.msg(name, Ext.String.format("{0} user: {1}", verb, record.getId()));
//          
//      }
  }
});