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
  initComponent: function() {
        var store = Ext.create('ExtMVCOne.store.Files');
        Ext.apply(this, {
            store: store
        });
        this.callParent(arguments);
    }

});