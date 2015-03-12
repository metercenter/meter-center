Ext.define('ExtMVCOne.view.user.List', {
  extend: 'Ext.panel.Panel',
  alias: 'widget.userlist',
  requires: [
      'Ext.layout.container.VBox',
      'ExtMVCOne.view.data.Grid',
      'ExtMVCOne.view.meter.Grid'
  ],
  xtype: 'layout-vertical-box',
  layout: {
      type: 'vbox',
      pack: 'start',
      align: 'stretch'
  },
  
  bodyPadding: 10,

  defaults: {
      frame: true,
      bodyPadding: 10
  },

  items: [
      {
          title: '流量计',
          flex: 1,
          margin: '0 0 10 0',
          xtype: 'metergrid'
          
      },
      {
          title: '数据',
          flex: 1,
          xtype: 'datagrid'
      }
  ]

});