Ext.define('ExtMVCOne.model.Meter', {
    extend: 'ExtMVCOne.model.Base',
    fields: [
       {name: 'meter_id'},
       {name: 'user_id'},
       {name: 'meter_name'},
       {name: 'meter_type'},
       {name: 'meter_index'},
       {name: 'meter_eui'},
       {name: 'user_meterdata'},
       {name: 'user_revise'},
       {name: 'user_reviseid'}
       ]
});
