/**
 * controller 
 */

Ext.define('MyApp.controller.User', {
    extend: 'Ext.app.Controller',
    //成员属性字符数组么
    stores: ['User'],
    models: ['User'],
    views: ['Viewport', 'user.List', 'user.Edit'],
    init: function () {
        this.control({
            'userlist': {
                itemdblclick: this.editUser
            },
            'useredit button[action=save]': {
                click: this.saveUser
            }
        });
    },
    editUser: function (grid, record, item, index) {
        var win = Ext.widget("useredit"); 
        win.down("form").loadRecord(record);
        alert(index);
        console.log(grid);
        console.log(win.down("form"));
        win.show();
    },
    saveUser: function (btn) {
        var win = btn.up("window"),
            form = win.down("form"),
            record = form.getRecord();
        form.updateRecord();
        record.commit();
        win.close();
    }
});