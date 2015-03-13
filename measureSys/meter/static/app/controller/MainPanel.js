Ext.define('ExtMVCOne.controller.MainPanel', {
    extend: 'Ext.app.Controller',
    init: function () {
        this.control({
          '#picPanel': {
            activate: {
              single: true,
              fn: function (panel) {
                Ext.Msg.alert("提示信息", "该模块正在建设中...");
              }
            }
          },
            '#contentPanel': {
                activate: {
                    single: true,
                    fn: function (panel) {
//                        Ext.Msg.alert("提示信息",panel.title);
                        this.application.getController('Meters').init();
                    }
                }
            },
            '#userPanel': {
                activate: {
                    single: true,
                    fn: function (panel) {
                        //Ext.Msg.alert("提示信息", panel.title);
                        this.application.getController('Users').init();
                    }
                }
            }
//            '#exportXLS': {
//              activate: {
//                  single: true,
//                  fn: function (panel) {
//                      Ext.Msg.alert("提示信息", panel.title);
////                      this.application.getController('Users').init();
//                  }
//              }
//          }
        });
    }
});