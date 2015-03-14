Ext.define("ExtMVCOne.store.Warn", {
    extend: 'Ext.data.Store',
    model: 'ExtMVCOne.model.Warn',
    batchActions: false,
    autoLoad: true,
    proxy: {
        type: "ajax",
        contentType: "application/json; charset=utf-8;",
        api: {
            read: 'Warn/List',
            destroy: 'Warn/Delete',
            update: "Warn/Edit",
            create: "Warn/Add"
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
