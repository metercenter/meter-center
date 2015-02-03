Ext.define("ExtMVCOne.store.Users", {
    extend: 'Ext.data.Store',
    model: 'ExtMVCOne.model.User',
    batchActions: false,
    autoLoad: true,
    proxy: {
        type: "ajax",
        api: {
            read: 'Users/List',
            destroy: 'Users/Delete',
            update: "Users/Edit",
            create: "Users/Add"
        },
        reader: {
            type: 'json',
            root: "data",
            messageProperty: "Msg"
        },
        writer: {
            type: "json",
            encode: true,
            root: "data",
            allowSingle: false
        }
   }
})
