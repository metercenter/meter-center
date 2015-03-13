Ext.define('ExtMVCOne.view.Meters.View', {
  extend : 'Ext.panel.Panel',
  alias : 'widget.metersview',
  requires : [ 'Ext.layout.container.Border', 'ExtMVCOne.view.user.List',
      'ExtMVCOne.view.user.Tree' ],
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
        new Ext.window.Window({
          autoShow : true,
          title : '客户信息',
           fieldDefaults: {
           labelAlign: 'right',
           labelWidth: 115,
           msgTarget: 'side'
           },
          //          
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
              emptyText : '客户登陆名'
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

            items : [{
              fieldLabel : '客户名称',
              name : 'company'
            }, {
              fieldLabel : '客户电话',
              name : 'phone',
            }, {
              xtype : 'combobox',
              fieldLabel : '客户等级',
              name : 'state',
//              store : {
//                type : 'states'
//              },
              valueField : 'abbr',
              displayField : 'level',
              typeAhead : true,
              queryMode : 'local',
              emptyText : '选择用户类型'
            } ]
          } ],
          //
          buttons : [ {
            text : '注册',
            formBind : true
          } ]
        });
      }
    }, {
      xtype : 'button',
      text : '添加流量计',
      style : 'margin:10px 5px 10px 50px;',
      scale : 'medium',
      iconAlign : 'top',
      handler : function() {
        window.location.href = "/get-excel-file";
      }
    } ]
  }, {
    title : '用户群',
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