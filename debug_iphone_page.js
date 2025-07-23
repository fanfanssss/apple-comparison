// 注入到iPhone页面进行调试的脚本
// 将此代码复制到浏览器控制台中运行，或添加到页面底部

(function() {
    console.log('开始调试iPhone页面数据问题...');
    
    // 1. 检查是否成功加载JSON数据
    console.log('全部产品数据:', allProducts);
    
    if (!allProducts || allProducts.length === 0) {
        console.error('错误: 产品数据未加载或为空');
        return;
    }
    
    // 2. 检查第一个产品的数据结构
    const sampleProduct = allProducts[0];
    console.log('样本产品数据:', sampleProduct);
    
    // 3. 验证双语对象处理函数
    console.log('语言选择器状态:', document.querySelector('.language-btn.active')?.dataset.lang);
    
    // 测试getLocalizedText函数
    try {
        if (typeof getLocalizedText === 'function') {
            // 测试普通字符串
            console.log('getLocalizedText测试(字符串):', getLocalizedText('测试', 'zh-CN'));
            
            // 测试双语对象
            const testObj = {'zh-CN': '中文测试', 'en-US': 'English Test'};
            console.log('getLocalizedText测试(中文):', getLocalizedText(testObj, 'zh-CN'));
            console.log('getLocalizedText测试(英文):', getLocalizedText(testObj, 'en-US'));
        } else {
            console.error('错误: getLocalizedText函数未定义');
        }
    } catch (e) {
        console.error('测试getLocalizedText时出错:', e);
    }
    
    // 4. 尝试手动重新生成表格
    try {
        console.log('尝试重新生成表格...');
        generateTable(allProducts);
        console.log('表格重新生成完成');
    } catch (e) {
        console.error('重新生成表格时出错:', e);
        // 打印详细错误堆栈
        console.error(e.stack);
    }
    
    console.log('调试完成');
})();
