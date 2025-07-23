/**
 * 语言切换功能
 * 实现多语言切换、本地存储、自动检测浏览器语言等功能
 */

// 初始化语言设置
function initLanguage() {
  // 尝试从localStorage获取用户语言偏好
  let currentLang = localStorage.getItem('preferredLanguage');
  
  // 如果没有存储的偏好，检测浏览器语言
  if (!currentLang) {
    const browserLang = navigator.language || navigator.userLanguage;
    currentLang = browserLang.startsWith('zh') ? 'zh-CN' : 'en-US';
    localStorage.setItem('preferredLanguage', currentLang);
  }
  
  // 应用语言
  applyLanguage(currentLang);
  
  // 更新语言按钮状态
  updateLanguageButtons(currentLang);
}

// 应用语言到页面
function applyLanguage(lang) {
  const resources = languageResources[lang];
  if (!resources) return;
  
  // 查找所有带有data-lang-key属性的元素
  const elements = document.querySelectorAll('[data-lang-key]');
  elements.forEach(el => {
    const key = el.getAttribute('data-lang-key');
    if (resources[key]) {
      // 根据元素类型设置文本
      if (el.tagName === 'INPUT' && el.getAttribute('type') === 'placeholder') {
        el.placeholder = resources[key];
      } else {
        el.textContent = resources[key];
      }
    }
  });
  
  // 更新页面标题
  if (resources['page.title']) {
    document.title = resources['page.title'];
  }
  
  // 触发自定义事件，通知其他可能需要更新的组件
  // 添加强制刷新选项，以便其他组件可以区分是否需要强制重新加载数据
  document.dispatchEvent(new CustomEvent('languageChanged', { 
    detail: { 
      language: lang,
      forceReload: true
    } 
  }));
}

// 更新语言按钮状态
function updateLanguageButtons(currentLang) {
  const buttons = document.querySelectorAll('.language-btn');
  buttons.forEach(btn => {
    const btnLang = btn.getAttribute('data-lang');
    if (btnLang === currentLang) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

// 从URL参数中获取语言设置
function getLanguageFromUrl() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get('lang');
}

// 文档加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
  // 检查URL参数中是否有语言设置
  const urlLang = getLanguageFromUrl();
  if (urlLang && (urlLang === 'zh-CN' || urlLang === 'en-US')) {
    localStorage.setItem('preferredLanguage', urlLang);
  }
  
  // 初始化语言
  initLanguage();
  
  // 为语言按钮添加点击事件
  const langButtons = document.querySelectorAll('.language-btn');
  langButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      const lang = this.getAttribute('data-lang');
      // 先设置全局语言状态变量（供其他组件使用）
      window.currentLanguage = lang;
      localStorage.setItem('preferredLanguage', lang);
      
      // 标记语言已更改
      document.documentElement.setAttribute('data-language-changed', 'true');
      
      // 更新UI
      applyLanguage(lang);
      updateLanguageButtons(lang);
      
      // 添加直接调用重新加载数据的支持
      // 如果页面有loadProductData函数，尝试调用它重新加载数据
      if (typeof window.reloadDataWithLanguage === 'function') {
        console.log('检测到reloadDataWithLanguage函数，调用重新加载数据...');
        window.reloadDataWithLanguage(lang);
      }
    });
  });
});
