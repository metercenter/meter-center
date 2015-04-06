Ext.define('app.controller.main.BrowseAreaController', {
	extend: 'Ext.app.ViewController',
	alias: 'controller.browseAreaController',

	views:  [
// 'main.BrowseArea',
				'main.OperationArea'
			],

	init: function() {
		// alert('nihao');
		var me = this;

		this.getView().items.items[4].toggleCollapse();

		this.control({
			'#addUserBtn':{
				click: function(){
//				  console.log(Ext.ComponentQuery.query('#userTree'));
//				  Ext.ComponentQuery.query('#userTree')[0].view.getRootNode().expand()
					me.getView().items.items[5].setCollapsed(false);
          Ext.ComponentQuery.query('#addUser')[0].setHidden(false);
          Ext.ComponentQuery.query('#addMeter')[0].setHidden(true);
				}
			}
		});
		
		this.control({
      '#addMeterBtn':{
        click: function(){
// me.getView().items.items[5].toggleCollapse();
          me.getView().items.items[5].setCollapsed(false);
          Ext.ComponentQuery.query('#addUser')[0].setHidden(true);
          Ext.ComponentQuery.query('#addMeter')[0].setHidden(false);
        }
      }
    });
		
		this.control({
		  '#registorBtn':{
        click: function(){
          var formData = Ext.ComponentQuery.query('#addUser')[0].getForm();
          Ext.MessageBox.confirm('提示', '您确定要添加该客户信息？', callBack);
          function callBack(btn, text) {
            if (btn != 'no'){
              Ext.Ajax.request({
                url : '/register_company',
                method : 'POST',
                params : formData.getValues(),
                success : function(response, opts) {
                  Ext.MessageBox.confirm('提示', '客户信息已注册，是否关闭窗口？', callBack);
                  Ext.ComponentQuery.query('#userTree')[0].store.load();
                  
                  function callBack(btn, text) {
                    if (btn != 'no')
                      me.getView().items.items[5].setCollapsed(true);
                  }
                },
                failure : function() {
                }
              })
            }
              
          }
        }
		  }
		});
		
		this.control({
		  '#modifyMeter' :{
		    click: function() {
		      Ext.ComponentQuery.query('#meterFieldset')[0].setDisabled(false);
		    }
		  }
		  
		});
		
		
		this.control({
		  '#registorMeterBtn':{
		    click: function() {
		      var formData = Ext.ComponentQuery.query('#addMeter')[0].getForm();
		      Ext.MessageBox.confirm('提示', '您确定要添加该流量计信息？', callBack);
          function callBack(btn, text) {
            if (btn != 'no'){
              Ext.Ajax.request({
                url : '/register_meter',
                method : 'POST',
                params : formData.getValues(),
                success : function(response, opts) {
                  result = Ext.decode(response.responseText);
                  if (result.status == 'SUCCESS'){
                    Ext.MessageBox.confirm('提示', '流量计信息已成功添加，是否关闭窗口？', callBack);
                    Ext.ComponentQuery.query('#userTree')[0].store.load();
                    
                    function callBack(btn, text) {
                      if (btn != 'no')
                        me.getView().items.items[5].setCollapsed(true);
                    }
                  } else {
                    Ext.MessageBox.alert('提醒',result.data);
                  }
                },
                failure : function() {
                }
              })
            }
              
          }
		    }
		  }
		});
	},

});