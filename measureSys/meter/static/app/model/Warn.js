///**
// * 
// */
//
Ext.define('ExtMVCOne.model.Warn', {
  extend : 'Ext.data.Model',
  fields : [ "id", {
    name : 'data_id'
  }, {
    name : 'meter_id'
  }, {
    name : 'data_date'
  }, {
    name : 'data_vb'
  }, {
    name : 'data_vm'
  }, {
    name : 'data_p'
  }, {
    name : 'data_t'
  }, {
    name : 'data_qb'
  }, {
    name : 'data_qm'
  }],
  idProperty : "id"
});
