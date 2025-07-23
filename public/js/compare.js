/**
 * 产品对比页面JavaScript功能
 * 
 * 主要功能：
 * 1. 根据URL参数加载对应产品线数据
 * 2. 动态生成产品对比表格
 * 3. 实现表格固定表头和左侧列
 * 4. 产品选择与取消功能
 * 5. 参数差异高亮显示
 * 6. 性能数据可视化
 */

document.addEventListener('DOMContentLoaded', function() {
    // 初始化变量
    let productType = 'iphone'; // 默认产品类型
    let productData = []; // 存储产品数据
    let selectedProducts = []; // 存储已选中的产品
    
    // 获取URL参数中的产品类型
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('type')) {
        productType = urlParams.get('type');
        
        // 更新产品类型标签页选中状态
        document.querySelectorAll('.product-type-tab').forEach(tab => {
            if (tab.dataset.type === productType) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        });
    }
    
    // 处理要高亮显示的产品
    let highlightProduct = null;
    if (urlParams.has('highlight')) {
        highlightProduct = urlParams.get('highlight');
    }
    
    // 初始化页面
    initPage();
    
    /**
     * 初始化页面
     */
    function initPage() {
        // 加载产品数据
        loadProductData();
        
        // 绑定事件处理器
        bindEventHandlers();
        
        // 初始化表格固定效果
        initTableFixedEffect();
        
        // 初始化返回顶部按钮
        initBackToTopButton();
    }
    
    /**
     * 加载产品数据
     */
    function loadProductData() {
        // 构建数据文件路径，添加时间戳参数防止缓存
        const timestamp = new Date().getTime();
        const dataUrl = `../public/data/${productType}.json?_t=${timestamp}`;
        
        console.log('加载产品数据，路径：', dataUrl);
        
        // 使用fetch API加载数据
        fetch(dataUrl, { cache: 'no-store' }) // 禁用缓存
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                productData = data;
                
                // 默认按发布时间从新到旧排序
                productData.sort((a, b) => {
                    return new Date(b.releaseDate) - new Date(a.releaseDate);
                });
                
                // 默认选择所有产品（按照PRD要求）
                selectedProducts = productData.map(product => product.id);
                
                // 更新已选择产品数量
                updateSelectedCount();
                
                // 生成表格
                generateTables();
                
                // 生成性能图表
                generatePerformanceCharts();
                
                // 如果URL中指定了要高亮显示的产品，确保它被选中
                if (highlightProduct && !selectedProducts.includes(highlightProduct)) {
                    const productIndex = productData.findIndex(p => p.id === highlightProduct);
                    if (productIndex !== -1) {
                        // 如果已经选择了最大数量的产品，移除最后一个
                        if (selectedProducts.length >= 6) {
                            selectedProducts.pop();
                        }
                        // 添加高亮产品到选择列表的开头
                        selectedProducts.unshift(highlightProduct);
                        // 重新生成表格
                        generateTables();
                    }
                }
            })
            .catch(error => {
                console.error('加载产品数据出错:', error);
                // 显示错误消息给用户
                const errorMsg = document.createElement('div');
                errorMsg.className = 'error-message';
                errorMsg.innerHTML = `
                    <i class="fas fa-exclamation-circle"></i>
                    <p>加载产品数据失败。请稍后重试。</p>
                `;
                document.querySelector('.parameter-section').appendChild(errorMsg);
            });
    }
    
    /**
     * 绑定事件处理器
     */
    function bindEventHandlers() {
        // 产品类型切换
        document.querySelectorAll('.product-type-tab').forEach(tab => {
            tab.addEventListener('click', function() {
                productType = this.dataset.type;
                
                // 更新选中状态
                document.querySelectorAll('.product-type-tab').forEach(t => {
                    t.classList.remove('active');
                });
                this.classList.add('active');
                
                // 更新URL而不刷新页面
                const url = new URL(window.location);
                url.searchParams.set('type', productType);
                window.history.pushState({}, '', url);
                
                // 重新加载数据
                loadProductData();
            });
        });
        
        // 重置选择按钮
        document.getElementById('reset-selection').addEventListener('click', function() {
            // 重新选择最新的6个产品
            selectedProducts = productData.slice(0, 6).map(product => product.id);
            updateSelectedCount();
            generateTables();
        });
        

        
        // 图表切换
        document.querySelectorAll('.chart-tab').forEach(tab => {
            tab.addEventListener('click', function() {
                document.querySelectorAll('.chart-tab').forEach(t => {
                    t.classList.remove('active');
                });
                this.classList.add('active');
                
                const chartType = this.dataset.chart;
                updatePerformanceChart(chartType);
            });
        });
    }
    
    /**
     * 初始化表格固定效果
     */
    function initTableFixedEffect() {
        // 监听滚动事件
        window.addEventListener('scroll', function() {
            const tables = document.querySelectorAll('.comparison-table');
            
            tables.forEach(table => {
                const headerRow = table.querySelector('thead tr');
                const firstColumn = table.querySelectorAll('tr > *:first-child');
                
                // 表头固定
                if (headerRow) {
                    if (table.getBoundingClientRect().top < 70) {
                        headerRow.classList.add('sticky');
                    } else {
                        headerRow.classList.remove('sticky');
                    }
                }
                
                // 左侧列固定
                firstColumn.forEach(cell => {
                    if (table.getBoundingClientRect().left < 0) {
                        cell.classList.add('sticky');
                    } else {
                        cell.classList.remove('sticky');
                    }
                });
            });
        });
    }
    
    /**
     * 初始化返回顶部按钮
     */
    function initBackToTopButton() {
        const backToTopButton = document.getElementById('backToTop');
        
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });
        
        backToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    

    
    /**
     * 更新已选择产品数量
     */
    function updateSelectedCount() {
        const countElement = document.querySelector('#selected-count span');
        countElement.textContent = selectedProducts.length;
    }
    
    /**
     * 生成产品对比表格
     */
    function generateTables() {
        // 获取所有参数分组表格
        const tables = {
            'basic-info': document.getElementById('basic-info-table'),
            'dimensions': document.getElementById('dimensions-table'),
            'display': document.getElementById('display-table'),
            'performance': document.getElementById('performance-table')
        };
        
        // 清空表格内容
        for (const table of Object.values(tables)) {
            // 清空表头
            const thead = table.querySelector('thead tr');
            while (thead.children.length > 1) {
                thead.removeChild(thead.lastChild);
            }
            
            // 清空表格内容
            const tbody = table.querySelector('tbody');
            tbody.innerHTML = '';
        }
        
        // 按照选择的产品顺序获取产品数据
        const selectedProductsData = selectedProducts.map(productId => {
            return productData.find(product => product.id === productId);
        }).filter(product => product !== undefined);
        
        // 生成表头
        for (const table of Object.values(tables)) {
            const thead = table.querySelector('thead tr');
            
            selectedProductsData.forEach(product => {
                const th = document.createElement('th');
                th.className = 'product-header';
                th.dataset.productId = product.id;
                
                th.innerHTML = `
                    <div class="product-name">${product.name}</div>
                    <div class="product-select">
                        <input type="checkbox" id="${product.id}-checkbox" class="product-checkbox" checked>
                        <label for="${product.id}-checkbox">选择</label>
                    </div>
                    <div class="product-image">
                        <img src="../public/images/products/${product.id}.jpg" alt="${product.name}">
                    </div>
                `;
                
                thead.appendChild(th);
            });
        }
        
        // 为每个表格生成参数行
        // 基本信息表格
        generateTableRows(tables['basic-info'], selectedProductsData, [
            { key: 'name', label: '型号', isHeader: true },
            { key: 'model', label: '型号标识' },
            { key: 'releaseDate', label: '发布日期' },
            { key: 'price', label: '起始价格' },
            { key: 'colors', label: '颜色' },
            { key: 'storage', label: '存储容量' }
        ]);
        
        // 尺寸与重量表格
        generateTableRows(tables['dimensions'], selectedProductsData, [
            { key: 'dimensions', label: '尺寸', isHeader: true },
            { key: 'weight', label: '重量' },
            { key: 'materials', label: '材质' }
        ]);
        
        // 显示屏表格
        generateTableRows(tables['display'], selectedProductsData, [
            { key: 'displaySize', label: '屏幕尺寸', isHeader: true },
            { key: 'displayResolution', label: '分辨率' },
            { key: 'displayTechnology', label: '屏幕技术' },
            { key: 'displayBrightness', label: '亮度' },
            { key: 'displayRefreshRate', label: '刷新率' }
        ]);
        
        // 性能表格
        generateTableRows(tables['performance'], selectedProductsData, [
            { key: 'processor', label: '处理器', isHeader: true },
            { key: 'processorDetails', label: '处理器详情' },
            { key: 'cpuPerformance', label: 'CPU性能分数' },
            { key: 'gpuPerformance', label: 'GPU性能分数' },
            { key: 'ram', label: '内存' },
            { key: 'battery', label: '电池容量' },
            { key: 'batteryLife', label: '电池续航' }
        ]);
        
        // 绑定产品选择/取消选择事件
        bindProductSelectionEvents();
        
        // 应用语言本地化
        applyLanguage(localStorage.getItem('preferredLanguage') || 'zh-CN');
    }
    
    /**
     * 生成表格行
     */
    function generateTableRows(table, productsData, parameters) {
        const tbody = table.querySelector('tbody');
        
        parameters.forEach(param => {
            // 检查是否所有产品该参数都相同
            let allSame = true;
            let firstValue = productsData[0] ? productsData[0][param.key] : null;
            
            for (let i = 1; i < productsData.length; i++) {
                if (productsData[i][param.key] !== firstValue) {
                    allSame = false;
                    break;
                }
            }
            
            const tr = document.createElement('tr');
            if (param.isHeader) {
                tr.className = 'parameter-header-row';
            }
            
            // 添加参数名称列
            const th = document.createElement('th');
            th.className = 'parameter-name fixed-column';
            th.setAttribute('data-lang-key', `param.${param.key}`);
            th.textContent = param.label;
            tr.appendChild(th);
            
            // 添加各产品的参数值
            productsData.forEach(product => {
                const td = document.createElement('td');
                let value = product[param.key] || '-';
                
                // 特殊格式化处理
                if (param.key === 'releaseDate') {
                    // 日期格式化
                    const date = new Date(value);
                    value = `${date.getFullYear()}年${date.getMonth() + 1}月`;
                } else if (param.key === 'price') {
                    // 价格格式化
                    value = `¥${value}起`;
                } else if (param.key === 'colors') {
                    // 颜色格式化为彩色圆点
                    if (Array.isArray(value)) {
                        const colorCircles = value.map(color => {
                            return `<span class="color-circle" style="background-color: ${color.code};" title="${color.name}"></span>`;
                        }).join('');
                        value = colorCircles;
                    }
                }
                
                // 为不同的参数设置高亮
                if (!allSame && !param.isHeader) {
                    td.classList.add('highlight-diff');
                }
                
                td.innerHTML = value;
                tr.appendChild(td);
            });
            
            tbody.appendChild(tr);
        });
    }
    
    /**
     * 绑定产品选择/取消选择事件
     */
    function bindProductSelectionEvents() {
        document.querySelectorAll('.product-checkbox').forEach(checkbox => {
            const productId = checkbox.id.replace('-checkbox', '');
            
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    // 添加产品到选择列表
                    if (!selectedProducts.includes(productId)) {
                        selectedProducts.push(productId);
                    }
                } else {
                    // 从选择列表中移除产品
                    const index = selectedProducts.indexOf(productId);
                    if (index > -1) {
                        selectedProducts.splice(index, 1);
                    }
                }
                
                // 更新已选择产品数量
                updateSelectedCount();
                
                // 重新生成表格
                generateTables();
                
                // 更新性能图表
                updatePerformanceChart(document.querySelector('.chart-tab.active').dataset.chart);
            });
        });
    }
    
    /**
     * 生成性能图表
     */
    function generatePerformanceCharts() {
        // 初始化GPU性能图表
        updatePerformanceChart('gpu');
    }
    
    /**
     * 更新性能图表
     */
    function updatePerformanceChart(chartType) {
        const chartArea = document.getElementById('performance-chart');
        chartArea.innerHTML = '';
        
        // 创建canvas元素
        const canvas = document.createElement('canvas');
        chartArea.appendChild(canvas);
        
        // 获取选中的产品数据
        const selectedProductsData = selectedProducts.map(productId => {
            return productData.find(product => product.id === productId);
        }).filter(product => product !== undefined);
        
        // 准备图表数据
        let labels = selectedProductsData.map(product => product.name);
        let dataKey = '';
        let chartTitle = '';
        let chartColor = '';
        
        switch (chartType) {
            case 'gpu':
                dataKey = 'gpuPerformance';
                chartTitle = 'GPU性能对比';
                chartColor = 'rgba(255, 99, 132, 0.8)';
                break;
            case 'cpu':
                dataKey = 'cpuPerformance';
                chartTitle = 'CPU性能对比';
                chartColor = 'rgba(54, 162, 235, 0.8)';
                break;
            case 'battery':
                dataKey = 'batteryLifeScore';
                chartTitle = '电池续航对比';
                chartColor = 'rgba(75, 192, 192, 0.8)';
                break;
        }
        
        // 获取数据
        const chartData = selectedProductsData.map(product => product[dataKey] || 0);
        
        // 创建图表
        new Chart(canvas, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: chartTitle,
                    data: chartData,
                    backgroundColor: chartColor,
                    borderColor: chartColor.replace('0.8', '1'),
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        position: 'top'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                label += context.parsed.y;
                                return label;
                            }
                        }
                    }
                }
            }
        });
    }
    
    /**
     * 应用语言本地化
     */
    function applyLanguage(lang) {
        // 这个函数会由language-switcher.js调用
        // 不需要在这里实现
    }
});
