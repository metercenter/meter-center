Ext.define('app.view.form.meter.MeterBasicInfo', {
  extend : 'Ext.form.Panel',
  alias : 'widget.meterBasicInfo',

  layout : {
    type : 'fit',
    align : 'stretch'
  },

  title : '流量计基本信息',
  
  id: 'meterbasicInfo',
  editable: false,
  padding : '10 10',

  items : [ {
    id: 'meterFieldset',
    xtype : 'fieldset',
    style : 'margin:10px 10px 10px 10px;',
    layout : 'column',
    
    defaults : {
      layout : 'form',
      xtype : 'container',
      defaultType : 'textfield',
      editable: false,
      style : 'width: 33%'
    },

    items : [ {
      items : [ {
        fieldLabel : '名称',
        name : 'meter_name',
        //disabled: true
        editable: false,
      }, {
        fieldLabel : '型号',
        name : 'meter_version',
        //disabled: true
      }, {
        fieldLabel : '流量范围',
        name : 'output_range',
        //disabled: true
      }, {
        fieldLabel : '温度范围',
        name : 'temperature_range',
        //disabled: true
      } ]
    }, {
      items : [ {
        xtype : 'combobox',
        name : 'meter_type',
        fieldLabel : '品牌',
        displayField : 'meter_type_name',
        editable: false,
        //disabled: true,
        store : {
          fields : [ 'meter_type', 'meter_type_name' ],
          proxy : {
            type : 'ajax',
            url : '/getMeterType',
            reader : {
              type : 'json'
            }
          },
          autoLoad : true
        },
        queryMode : 'local',
      }, {
        fieldLabel : '序列号',
        name: 'meter_seqNo',
        //disabled: true
      }, {
        fieldLabel : '检定有效期',
        name: 'valid_time',
        //disabled: true
      }, {
        fieldLabel : '铅封编号',
        name: 'wrap_code',
        //disabled: true
      } ]
    }, {
      items : [ {
        xtype : 'combobox',
        name : 'meter_type',
        //disabled: true,
        fieldLabel : '修正仪',
        displayField : 'meter_type_name',
        editable: false,
        store : {
          fields : [ 'meter_type', 'meter_type_name' ],
          proxy : {
            type : 'ajax',
            url : '/getMeterType',
            reader : {
              type : 'json'
            }
          },
          autoLoad : true
        },
        queryMode : 'local',        
      }, {
        fieldLabel : '压力范围',
        name: 'pressure',
        //disabled: true
      }, {
        fieldLabel : '通信方式',
        name:'communication',
        //disabled: true
      }, {
        fieldLabel : '节点号',
        name:'meter_eui',
        //disabled: true
      } ]
    } ],
    // } ],
   
  } ],
  
  buttons : [ {
    text : '修改',
    id: 'modifyMeter'
  }, {
    text : '保存'
  } ],
  
  initComponent : function() {
    var me = this;
    me.callParent(arguments);
  }
})