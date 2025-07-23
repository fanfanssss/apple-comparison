// 此脚本用于测试iPhone页面数据显示问题
// 在浏览器控制台中运行以验证修复是否成功

(function() {
    console.log('开始测试iPhone页面数据显示...');
    
    // 检查数据是否已正确加载
    if (!window.allProducts || window.allProducts.length === 0) {
        console.error('错误: 产品数据未加载!');
        return;
    }
    
    console.log(`已加载 ${window.allProducts.length} 个iPhone产品`);
    
    // 查看表格数据
    const tableRows = document.querySelectorAll('table tbody tr');
    console.log(`表格行数: ${tableRows.length}`);
    
    // 检测是否有空白参数
    const emptyValues = document.querySelectorAll('.param-value.empty-value');
    console.log(`空参数单元格数: ${emptyValues.length}`);
    
    // 检测双语对象渲染
    const currentLanguage = document.querySelector('.language-btn.active')?.dataset.lang || 'zh-CN';
    console.log(`当前语言: ${currentLanguage}`);
    
    // 尝试检查产品名称和一些重要参数
    if (window.allProducts[0]) {
        const sample = window.allProducts[0];
        console.log('样本产品:', sample.id);
        console.log('名称:', sample.name);
        console.log('发布日期:', sample.releaseDate);
        
        // 测试本地化函数
        if (typeof window.getLocalizedText === 'function' && sample.name) {
            console.log('本地化名称测试:', window.getLocalizedText(sample.name, currentLanguage));
        }
        
        // 测试一些重要字段的渲染
        const displayedName = document.querySelector(`label[for="${sample.id}"]`)?.textContent;
        console.log('页面显示的产品名称:', displayedName);
        
        // 检查参数表格值
        const firstProductValues = document.querySelectorAll(`td[data-product="${sample.id}"]`);
        console.log(`${sample.id} 的参数值数量: ${firstProductValues.length}`);
        
        // 如果太少参数值，说明显示有问题
        if (firstProductValues.length < 10) {
            console.error('警告: 产品参数显示不完整!');
        } else {
            console.log('参数显示数量正常');
        }
    }
    
    // 测试语言切换
    console.log('测试语言切换功能...');
    const langBtns = document.querySelectorAll('.language-btn');
    console.log(`语言按钮数量: ${langBtns.length}`);
    
    console.log('测试完成');
})();
