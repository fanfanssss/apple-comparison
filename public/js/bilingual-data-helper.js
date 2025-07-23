/**
 * 双语数据支持辅助函数
 * 用于处理产品数据中的双语字段
 */

// 获取本地化文本
function getLocalizedText(field, lang) {
  // 如果字段是对象且包含当前语言的键
  if (field && typeof field === 'object' && field[lang]) {
    return field[lang];
  }
  // 如果字段是对象但不包含当前语言，尝试使用另一种语言
  if (field && typeof field === 'object') {
    // 如果请求英文但只有中文
    if (lang === 'en-US' && field['zh-CN']) {
      return field['zh-CN'];
    }
    // 如果请求中文但只有英文
    if (lang === 'zh-CN' && field['en-US']) {
      return field['en-US'];
    }
  }
  // 否则返回原始值（向后兼容）
  return field;
}

// 递归处理嵌套对象中的本地化文本
function processLocalizedObject(obj, lang) {
  if (!obj || typeof obj !== 'object') {
    return obj;
  }
  
  // 处理数组
  if (Array.isArray(obj)) {
    return obj.map(item => processLocalizedObject(item, lang));
  }
  
  // 处理对象
  const result = {};
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      const value = obj[key];
      
      if (value && typeof value === 'object') {
        // 检查是否是语言对象（包含zh-CN或en-US键）
        if ((value['zh-CN'] !== undefined || value['en-US'] !== undefined) && 
            Object.keys(value).length <= 2) {
          result[key] = getLocalizedText(value, lang);
        } else {
          // 递归处理嵌套对象
          result[key] = processLocalizedObject(value, lang);
        }
      } else {
        result[key] = value;
      }
    }
  }
  
  return result;
}

// 监听语言变更事件，更新产品数据显示
document.addEventListener('languageChanged', function(e) {
  const currentLang = e.detail.language;
  console.log(`语言已切换为: ${currentLang}，正在更新产品数据显示...`);
  
  // 触发产品数据重新渲染
  if (typeof updateProductDisplay === 'function') {
    updateProductDisplay(currentLang);
  }
});
