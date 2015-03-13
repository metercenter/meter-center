Ext.define('ExtMVCOne.view.user.Tree', {
    extend:'Ext.tree.Panel',
    alias:'widget.treeList',
    autoScroll:true,
    scroll:'vertical',
    useArrows:true,
    stateful:false,
    border:true,
    rootVisible:true,
    config:{
      deplacementDepart:null
    },
    viewConfig:{
      loadMask:false,
      plugins:{
          ptype:'treeviewdragdrop',
          expandDelay:100
       }
    },
    listeners: {
      itemclick: function(view, record, item, index, e, eOpts) {
//        console.log(item);
//        alert(record.data.text);
//        console.log(Ext.ComponentQuery.query('#datagrid'));
        Ext.ComponentQuery.query('#datagrid')[0].store.load({
          params : {
            user_name : record.data.text
          },
          callback : function(records, options, success) {
          }
        });
        Ext.ComponentQuery.query('#metergrid')[0].store.load({
          params : {
            user_name : record.data.text
          },
          callback : function(records, options, success) {
          }
        });
      }
    },

  initComponent: function() {
        var store = Ext.create('ExtMVCOne.store.Files');
        Ext.apply(this, {
            store: store,
        });
        this.rootVisible = false;
        this.callParent(arguments);
    }

});