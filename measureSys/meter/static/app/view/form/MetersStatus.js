Ext.define('app.view.form.MetersStatus', {
  extend : 'Ext.panel.Panel',
  alias : 'widget.metersStatus',

  title : '设备运行状况(自检)',

  bodyStyle : {
    padding : '10px'
  },
  
  items : [ {
    xtype : 'fieldset',

    defaultType : 'textfield',
    defaults : {
      anchor : '100%'
    },
    padding : '10px',

    // frame : true,
    // resizable : true,
//    minHeight : 150,

    layout : 'column',

    defaults : {
      layout : 'form',
      xtype : 'container',
      defaultType : 'textfield',
      style : 'width: 33%'
    },

    items : [ {
      items : [ {
        fieldLabel : '接入点总数'
      }]},{
      items :[{
        fieldLabel : '正常上报数'
      }],},{
      items: [{
        fieldLabel : '通讯异常数'
      }]
    } ]
  }]

})