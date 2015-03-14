Ext.define('ExtMVCOne.view.Meters.View', {
  extend : 'Ext.panel.Panel',
  alias : 'widget.metersview',
  requires : [ 'Ext.layout.container.Border', 'ExtMVCOne.view.user.List',
      'ExtMVCOne.view.user.Tree', 'ExtMVCOne.model.UserLevel' ],
  layout : 'border',
  bodyBorder : false,

  defaults : {
    collapsible : true,
    split : true,
    bodyPadding : 10
  },

  items : [ {
    title : '操作台',
    region : 'south',
    height : 100,
    minHeight : 75,
    maxHeight : 150,
    collapsed : true,
    items : [ {
      xtype : 'button',
      text : '导出到Excel文件',
      style : 'margin:10px 5px 10px 220px;',
      scale : 'medium',
      iconAlign : 'top',
      handler : function() {
        window.location.href = "/get-excel-file";
      }
    }, {
      xtype : 'button',
      text : '注册用户',
      scale : 'medium',
      style : 'margin:10px 5px 10px 50px;',
      iconAlign : 'top',
      handler : function() {
        var myForm = new Ext.form.Panel({
          width : 500,
          height : 300,
          title : '注册用户',
          floating : true,
          closable : true,
          items : [ {
            xtype : 'fieldset',
            title : '用户信息',
            defaultType : 'textfield',
            defaults : {
              anchor : '100%'
            },

            items : [ {
              allowBlank : false,
              fieldLabel : '用户名',
              name : 'user',
              emptyText : '客户登录名'
            }, {
              allowBlank : false,
              fieldLabel : '密码',
              name : 'pass',
              emptyText : 'password',
              inputType : 'password'
            }, {
              allowBlank : false,
              fieldLabel : '确认密码',
              name : 'pass',
              emptyText : 'password',
              inputType : 'password'
            } ]
          }, {
            xtype : 'fieldset',
            title : '联系信息',

            defaultType : 'textfield',
            defaults : {
              anchor : '100%'
            },

            items : [ {
              fieldLabel : '客户名称',
              name : 'company'
            }, {
              fieldLabel : '客户电话',
              name : 'phone',
            }, {
              xtype : 'combobox',
              id : 'user_company',
              fieldLabel : '主管单位',
              displayField : 'user_company',
              store : {
                fields : [ 'user_id', 'user_company' ],
                proxy : {
                  type : 'ajax',
                  url : '/get-user-level',
                  reader : {
                    type : 'json'
                  }
                },
                autoLoad : true
              },
              queryMode : 'local',
            } ]
          } ],
          //
          buttons : [ {
            text : '注册',
            formBind : true,
            handler : function() {
//              console.log(Ext.ComponentQuery.query('#userTree'));
              // alert('nihao');
              var f = myForm.getForm();
              Ext.Ajax.request({
                url : '/register_company',
                method : 'POST',
                params : f.getValues(),
                success: function(response,opts) {
                  Ext.MessageBox.confirm('提示', '客户信息已注册，是否关闭窗口？', callBack); 
                  Ext.ComponentQuery.query('#userTree')[0].store.load();
                  function callBack(btn,text) { 
                    if(btn !='no')
                       myForm.hide();
                  } 
                },
                failure : function() {
                }
              });
            }
          } ]
        });
        myForm.show();
      }
    }, {
      xtype : 'button',
      text : '添加流量计',
      style : 'margin:10px 5px 10px 50px;',
      scale : 'medium',
      iconAlign : 'top',
      handler : function() {
        var myForm = new Ext.form.Panel({
          width : 500,
          height : 330,
          title : '流量计信息',
          floating : true,
          closable : true,
          items : [ {
            xtype : 'fieldset',
            title : '流量计基本信息',
            defaultType : 'textfield',
            defaults : {
              anchor : '100%'
            },

            items : [ {
              allowBlank : false,
              fieldLabel : '用户/流量计名称',
              name : 'meter_name',
              emptyText : '用户或流量名称'
            },{
              allowBlank : false,
              fieldLabel : '流量计标示',
              name : 'meter_eui',
              emptyText : 'EUI64编号'
            }, {
              xtype : 'combobox',
              id : 'meter_type',
              fieldLabel : '流量计类型',
              displayField : 'meter_type_name',
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
            } ]
          }, {
            xtype : 'fieldset',
            title : '校准及参考值',

            defaultType : 'textfield',
            defaults : {
              anchor : '100%'
            },

            items : [ {
              fieldLabel : '用户校准值',
              name : 'user_revise'
            }, {
              fieldLabel : '标况参考值',
              name : 'meter_qb',
            }, {
              fieldLabel : '工况参考值',
              name : 'meter_qm',
            },{
              xtype : 'combobox',
              id : 'user_company',
              fieldLabel : '隶属客户',
              displayField : 'user_company',
              store : {
                fields : [ 'user_id', 'user_company' ],
                proxy : {
                  type : 'ajax',
                  url : '/get-usermeter-level',
                  reader : {
                    type : 'json'
                  }
                },
                autoLoad : true
              },
              queryMode : 'local',
            } ]
          } ],
          //
          buttons : [ {
            text : '登记',
            formBind : true,
            handler : function() {
              // alert('nihao');
              var f = myForm.getForm();
              Ext.Ajax.request({
                url : '/register_meter',
                method : 'POST',
                params : f.getValues(),
                success: function() {
                  Ext.MessageBox.confirm('提示', '流量计信息已登记，是否关闭窗口？', callBack); 
                  function callBack(btn,text) { 
                    if(btn !='no')
                       myForm.hide();
                  } 
                },
                failure : function() {
                  console.log('failure');
                }
              });
            }
          } ]
        });
        myForm.show();
      }
    } ]
  }, {
    title : '用户群',
    itemId: 'userTree',
    region : 'west',
    floatable : false,
    margin : '5 0 0 0',
    width : 125,
    minWidth : 200,
    maxWidth : 250,
    xtype : 'treeList'
  }, {
    title : '实时数据显示',
    collapsible : true,
    region : 'center',
    margin : '5 0 0 0',
    xtype : 'userlist'
  } ],

});