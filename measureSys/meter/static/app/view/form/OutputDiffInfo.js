Ext.define('app.view.form.OutputDiffInfo',{
  extend: 'Ext.form.Panel',
  alias: 'widget.outputDiffInfo',
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

    layout : 'column',

    defaults : {
      layout : 'form',
      xtype : 'container',
      defaultType : 'textfield',
      style : 'width: 33%'
    },

    items : [ {
      items : [ {
        fieldLabel : '前一日上游进气总量'
      },{
        fieldLabel : '前一日工业用户售气量'
      },{
        fieldLabel : '前一日居民用气估量'
      },{
        fieldLabel : '其他气量统计'
      },{
        fieldLabel : '前一日输差计算'
      }]
    }]
  }]
});