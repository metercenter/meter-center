Ext.define('ExtMVCOne.model.Meter', {
    extend: 'ExtMVCOne.model.Base',
    /*
     * meter_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    meter_name = models.CharField(max_length=200)
    meter_type = models.IntegerField(default=0)
    meter_index = models.CharField(max_length=200)
    meter_eui = models.CharField(max_length=200)
    user_meterdata = models.CharField(max_length=200)
    user_revise = models.CharField(max_length=200)
    user_reviseid = models.CharField(max_length=200)
     * 
     * */
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
       // Trend begins with the cerrent price. Changes get pushed onto the end
//       {
//           name: 'trend',
//           convert: function(value, record) {
//               // Record creation call with no trend there: start with current price
//               if (value === null) {
//                   return [record.get('price')];
//               }
//               return Ext.isArray(value) ? value : [ value ];
//           } 
//       },
//       // Rating dependent upon performance 0 = best, 2 = worst
//       {
//           name: 'rating',
//           type: 'int',
//           convert: function(value, record) {
//               var pct = record.get('pctChange');
//               if (pct < 0)
//                   return 2;
//               if (pct < 1)
//                   return 1;
//               return 0;
//           }
//        }
//    ],
//
//    // Override to keep the last 10 prices in the trend field
//    set: function(fieldName, value) {
//        if (fieldName === 'price') {
//            this.callParent([{
//                price: value,
//                trend: this.addToTrend(fieldName.price)
//            }]);
//        }
//        else {
//            if (typeof fieldName !== 'string' && 'price' in fieldName) {
//                fieldName.trend = this.addToTrend(fieldName.price);
//            }
//            this.callParent(arguments);
//        }
//    },
//
//    // Override to keep the last 10 prices in the trend field
//    addToTrend: function(value) {
//        var trend = this.data.trend.concat(value);
//
//        if (trend.length > 10) {
//            Ext.Array.splice(trend, 0, trend.length - 10);
//        }
//        return trend;
//    }
});
