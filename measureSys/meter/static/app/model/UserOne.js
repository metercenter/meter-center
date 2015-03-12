/**
 * 
 */
Ext.define('ExtMVCOne.model.UserOne', {
    extend: 'Ext.data.Model',
    fields: [
        { name: 'name', type: 'string' },
        { name: 'age', type: 'int' },
        { name: 'phone', type: 'string' }
    ]
});