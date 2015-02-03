Ext.define('ExtMVCOne.controller.Meters', {
  extend : 'Ext.app.Controller',
  requires : [ 'ExtMVCOne.view.Meters.View',
               'ExtMVCOne.view.data.Grid',
               'ExtMVCOne.view.meter.Grid'],
  models : [ 'Company','Company' ],
  stores : [ 'Companies','Companies' ],
  views: ['data.Grid','meter.Grid'],
  refs : [ {
    ref : "ContentPanel",
    selector : "#contentPanel"
  } ],

  init : function() {
    var me = this, panel = me.getContentPanel(), view = Ext.widget("metersview");
    panel.add(view);
    me.control({});
  }
});
