var headerBackgroundColor = "url(/static/resources/images/headerbackground.png) repeat-x", headerHeight = 69, headerColorInactive = "#BCBCBC", headerColorActive = "#FFFFFF", footerHeight = 24;

var headerLogo = new Ext.Component({
  autoEl : {
   tag : "img",
   src : "/static/resources/images/logo.png",
   alt : "Cisco",
   id : "header-logo",
   width: "50px",
   height: "40px",
   style : {
     margin: "10px",
     background : "none"
     // lineHeight : headerHeight + "px"
    }
  }
 });

var headerTitle = new Ext.Component({
  autoEl : {
   tag : "h1",
   html : '<h1 id="header-title" class="header">计量管理系统</h1>',
   id : "header-title"
  }
 });


var headerButtonTemplate = new Ext.Template('<div id="{4}" 	class="x-btn {3}"><div class="{1}">',
		  '<em class="{2}" unselectable="on"><button type="{0}"></button></em>', '</div></div>', {
		   compiled : false
		  });
var HeaderButton = Ext.extend(Ext.Button, {
	template : headerButtonTemplate,
	height : headerHeight,
	style : {
		float : "left",
		marginRight : "15px",
		background : "none"
		// lineHeight : headerHeight + "px"
	}
});

var headerLogout = new HeaderButton({
	   id : "header-logout",
	   text : "",
	   icon : "/static/resources/images/logout.png",
	   cls : "header-button-active",
	   handler : function(_ele, _evt) {
	    // TODO: Add Ajax handler to LOGOUT
	    window.location = "/logout";
	   }
});

var headerButtonGroup = new Ext.Panel({
	   border : false,
	   id : "header-button-group",
	   height : headerHeight,
	   bodyStyle : {
	    float : "right",
	    background : "none"
	   },
	   items : [headerLogout]
});

var headerPanel = new Ext.Panel({
  id : "header",
  region : "north",
  height : headerHeight,
  border : false,
  items : [headerLogo, headerTitle, headerButtonGroup],
  bodyStyle : {
   background : headerBackgroundColor,
   width : "100%"
  }
 });


Ext.define('app.view.main.Main', {
    extend: 'Ext.container.Container',
    layout: 'border',
    requires:['app.view.main.BrowseArea',
              'app.view.main.Menu'],
    id : "titlePage",
    viewModel: {
      data: {
        companyName: '金昇'
      }
    },
    
 
    items: [
    //{
//        region: 'north',
//        id: 'North',
//        xtype : 'component',
//        cls: 'logo',
//        bind: {
//          html: '<h1 class="header" >{companyName}计量管理系统</h1><div class="test"><ul><li><a href="javascript:alert(\'请联系宋争，他再找人\')">联系我们</a></li><li><a href="logout">退出</a></li><li><a href="main">刷新</a></li><li><a href="main">首页</a></li></ul></div>'
//        },
//        border: false,
//        height: 50,
//        margin: '0 0 5 0'
//    }
    headerPanel,
//    {  
//        xtype: 'panel',  
//        region: 'north',  
//        height: 69,
//        bodyStyle: {  
//            background: "url(/static/resources/images/headerbackground.png) repeat-x",  
//            padding: '10px'  
//        },
//    	items: [headerLogo, headerTitle],
//    	      {  
//    			id : "header-logout",
//    			text : "退出",
//    			icon : "/static/resources/images/logout.png",
//    			cls : "header-button-active",
//    			handler : function(_ele, _evt) {
//    				window.location = "/logout";
//    			}
//    	      }
//	}, 
	{
//        region: 'north',
//        xtype: 'menubar'
//    }, {
        region: 'center',
        xtype: 'browseArea'
//        items: [{
//        	id: 'dataarea',
//            xtype: 'browseArea',
//            height: 700
//        },{
//        	id: 'warnarea',
//            xtype: 'button',
//            text: 'test',
//            hidden: true
//        }]
    }, {
        region:'south',
        xtype : 'component',
        id: "South",
        height: 8
    }]

});
