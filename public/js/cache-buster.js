/**
 * 缓存刷新脚本
 * 用于强制浏览器重新加载JavaScript文件
 */

// 为所有脚本URL添加时间戳参数
document.addEventListener('DOMContentLoaded', function() {
    const scripts = document.querySelectorAll('script[src]');
    scripts.forEach(script => {
        if (!script.src.includes('cache-buster.js')) {
            const timestamp = new Date().getTime();
            script.src = script.src.includes('?') 
                ? `${script.src}&_t=${timestamp}` 
                : `${script.src}?_t=${timestamp}`;
        }
    });
    
    console.log('缓存刷新脚本已执行，所有JS文件已添加时间戳参数');
});
