var ua = navigator.userAgent;
var ipad = ua.match(/(iPad).*OS\s([\d_]+)/),
isIphone =!ipad && ua.match(/(iPhone\sOS)\s([\d_]+)/),
isAndroid = ua.match(/(Android)\s+([\d.]+)/),
isMobile = isIphone || isAndroid;
//判断
var applejudge = sessionStorage.getItem('applejudge');
if(applejudge=='已提示'){}else{
	if(isMobile){
		alert("您正使用移动设备浏览，建议横屏显示效果更佳！");
		sessionStorage.setItem('applejudge', '已提示');
	}else{}
}
//禁止右键
document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});
//禁止复制
document.addEventListener("keydown", function(e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'C' || e.key === 'x' || e.key === 'X')) {
        e.preventDefault();
    }
});
