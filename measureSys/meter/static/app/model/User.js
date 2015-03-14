///**
// * 
// */
//
Ext.define('ExtMVCOne.model.User', {
  extend : 'Ext.data.Model',
  fields : [ "id", {
    name : "user_company",
//    defaultValue : "newuser"
  }, {
    name : "user_phone",
//    defaultValue : "newuser@email.com"
  }, {
    name : "user_name",
//    defaultValue : "普通用户"
  }, {
    name : "user_password",
//    type : "date",
//    dateFormat : "Y-m-d H:i:s",
//    defaultValue : new Date()
  }, {
    name : "IsApproved",
    type : "bool",
    defaultValue : true
  } ],
  idProperty : "id"
});
