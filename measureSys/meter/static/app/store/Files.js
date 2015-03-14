/**
 * 
 */
Ext.define('ExtMVCOne.store.Files', {
    extend: 'Ext.data.TreeStore',
    alias: 'store.files',
//    autoLoad : true,
//    model: 'ExtMVCOne.model.Tree',
    proxy:{
      type: 'ajax',
      url:'/get-user-group',
      reader:{
        type : 'json',
        root: 'children'
      }
    },
    
//    folderSort: true
    root: {
      text: '当前用户',
      expanded: true
    },
    rootVisible : false,
    
});