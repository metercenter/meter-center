///**
// * 
// */
//
Ext.define('ExtMVCOne.model.User', {
  extend : 'Ext.data.Model',
  fields : [ "id", {
    name : "Username",
    defaultValue : "newuser"
  }, {
    name : "Email",
    defaultValue : "newuser@email.com"
  }, {
    name : "Roles",
    defaultValue : "普通用户"
  }, {
    name : "Created",
    type : "date",
    dateFormat : "Y-m-d H:i:s",
    defaultValue : new Date()
  }, {
    name : "LastLoginDate",
    type : "date",
    dateFormat : "Y-m-d H:i:s"
  }, {
    name : "IsApproved",
    type : "bool",
    defaultValue : true
  } ],
  idProperty : "id"
});
