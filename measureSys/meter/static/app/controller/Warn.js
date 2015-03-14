Ext.define('ExtMVCOne.controller.Warn', {
  extend : 'Ext.app.Controller',
  requires : [ 
               'ExtMVCOne.view.warn.View'
             ],
  models : [ 'Warn' ],
  stores : [ 'Warn' ],
  views : [ 'warn.View' ],
  refs : [ {
    ref : "PicPanel",
    selector : "#picPanel"
  } ],

  init : function() {
    var me = this, panel = me.getPicPanel(), view = Ext.widget("warnview");
    console.log(view);
    panel.add(view);
    me.control({});
  }
});
