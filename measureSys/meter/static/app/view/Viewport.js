Ext.define('ExtMVCOne.view.Viewport', {
  extend : 'Ext.container.Viewport',
  layout : {
    type : 'vbox',
    align : 'stretch'
  },
  requires : [ 'ExtMVCOne.view.MainPanel' ],
  initComponent : function() {
    var me = this;
    me.items = [ {
      xtype : "toolbar",
      height : 53,
      id:"North",
      items : [ {
        xtype : 'component',
        cls : 'logo',
        id: "app-header-title",
        html : '计量管理系统'
      }, "->", {
        iconCls : "logout",
        tooltip : "退出",
        scale : "large",
        handler : function() {
          window.location = "Logout";
        }
      } ]
    },
    {
      xtype : "mainpanel",
      id : "mainPanel"
    }, {
      xtype : "component",
      height : 13,
      id : "South"
    } ];
    me.callParent(arguments);
  }
});