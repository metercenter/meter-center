Ext.define("ExtMVCOne.store.Roles", {
    extend: 'Ext.data.ArrayStore',
    fields: ["text"],
    data: [["普通用户"], ["系统管理员"]]
})
