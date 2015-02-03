Ext.define('ExtMVCOne.controller.Users', {
  extend : 'Ext.app.Controller',
  models : [ 'User' ],
  stores : [ 'Users', 'Roles' ],
  views : [ 'Users.View' ],
  refs : [ {
    ref : "UserPanel",
    selector : "#userPanel"
  } ],

  init : function() {
    var me = this, panel = me.getUserPanel(), view = Ext.widget("usersview");
    console.log(view);
    panel.add(view);
    me.control({});
  }
});
