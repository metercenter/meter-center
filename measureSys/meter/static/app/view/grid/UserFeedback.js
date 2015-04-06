Ext.define('app.view.grid.UserFeedback',{
	extend: 'Ext.grid.Panel',
	alias: 'widget.userFeedback',

	requires: [
        'Ext.data.*',
        'Ext.grid.*',
        'Ext.util.*',
        'Ext.toolbar.Paging',
        'Ext.ux.ProgressBarPager',
        'app.model.grid.UserFeedbackModel',
        'app.store.grid.UserFeedbackStore'
    ],
    title: '用户反馈信息',
    padding: '10 10',
    height: 200,
    initComponent: function(){
      var store = Ext.create('store.userFeedbackStore');
    	Ext.apply(this, {
            store: store,
            columns: [{ 
                text: '客户',
                sortable: true,
                dataIndex: 'user_id',
//                flex: 1
                width: 75
            },{
                text: '反馈时间',
                sortable: true,
                formatter: 'usMoney',
                dataIndex: 'report_time',
                width: 75
            },{
                text: '处理时限',
                sortable: true,
                renderer: this.changeRenderer,
                dataIndex: 'solution_deadline',
                width: 80
            },{
                text: '问题描述',
                sortable: true,
                renderer: this.pctChangeRenderer,
                dataIndex: 'problem',
                width: 100
            },{
                text: '处理结果',
                sortable: true,
                dataIndex: 'solution_result',
                width: 115,
//                formatter: 'date("m/d/Y")'
            }],

            bbar: {
                xtype: 'pagingtoolbar',
                pageSize: 10,
                store: store,
                displayInfo: true,
                plugins: new Ext.ux.ProgressBarPager()
            }
        });
		
		this.callParent();
    }
});