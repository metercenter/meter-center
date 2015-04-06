Ext.define('app.view.form.IdentificationCenter', {
  extend : 'Ext.form.Panel',
  alias : 'widget.indentificationCenter',
  layout : {
    type : 'vbox',
    align : 'stretch'
  },
  items : [ {
    layout : {
      type : 'hbox',
      align : 'stretch'
    },
    items : [ {
      xtype : 'panel',
      title : '基本信息',
      flex : 1,
      bodyStyle : {
        // background: '#ababab',
        padding : '10px'
      },
      items : [ {
        xtype : 'fieldset',
        // title : '用户信息',

        defaultType : 'textfield',
        defaults : {
          anchor : '100%'
        },
        padding : '10px',
        items : [ {
          allowBlank : false,
          fieldLabel : '用户',
          name : 'user',
          emptyText : '流量计用户'
        }, {
          allowBlank : false,
          fieldLabel : '流量计品牌',
          name : 'pass',
          emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          fieldLabel : '型号',
          name : 'pass',
          emptyText : '类型编号',
        // inputType : '类型编号'
        }, {
          allowBlank : false,
          fieldLabel : '序列号',
          name : 'user',
          emptyText : ''
        }, {
          allowBlank : false,
          fieldLabel : '流量范围',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          fieldLabel : '检定日期',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          fieldLabel : '下次检定日期',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        } ]
      } ]
    }, {
      xtype : 'panel',
      title : '检定数据',
      flex : 1,
      bodyStyle : {
        // background: '#ababab',
        padding : '10px'
      },
      items : [ {
        xtype : 'fieldset',
        // title : '用户信息',

        defaultType : 'textfield',
        defaults : {
          anchor : '100%'
        },
        padding : '10px',
        items : [ {
          allowBlank : false,
          fieldLabel : '介质',
          name : 'user',
        // emptyText : '流量计用户'
        }, {
          allowBlank : false,
          fieldLabel : '压力',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          fieldLabel : '温度',
          name : 'pass',
        // emptyText : '类型编号',
        // inputType : '类型编号'
        }, {
          allowBlank : false,
          labelWidth : 200,
          fieldLabel : '检定点100%Qmax偏差',
          name : 'user',
          emptyText : ''
        }, {
          allowBlank : false,
          labelWidth : 200,
          fieldLabel : '检定点60%Qmax偏差',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          labelWidth : 200,
          fieldLabel : '检定点40%Qmax偏差',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          labelWidth : 200,
          fieldLabel : '检定点20%Qmax偏差',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        }, {
          allowBlank : false,
          labelWidth : 200,
          fieldLabel : '检定点10%Qmax偏差',
          name : 'pass',
        // emptyText : 'password',
        // inputType : 'password'
        } ]
      } ]
    } ]
  }, {
    buttons : [ {
      text : '新增录入',
      formBind : true,
      handler : function() {
        var f = myForm.getForm();
        Ext.Ajax.request({
          url : '/register_company',
          method : 'POST',
          params : f.getValues(),
          success : function(response, opts) {
            Ext.MessageBox.confirm('提示', '客户信息已注册，是否关闭窗口？', callBack);
            Ext.ComponentQuery.query('#userTree')[0].store.load();
            function callBack(btn, text) {
              if (btn != 'no')
                myForm.hide();
            }
          },
          failure : function() {
          }
        });
      }
    } ]
  } ]
});