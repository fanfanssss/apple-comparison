/**
 * 苹果资讯页面JavaScript功能
 * 
 * 主要功能：
 * 1. 文章分类筛选
 * 2. 产品相关筛选
 * 3. 文章搜索
 * 4. 文章分页
 */

document.addEventListener('DOMContentLoaded', function() {
    // 初始化变量
    let currentCategory = 'all';
    let currentProduct = null;
    let searchQuery = '';
    let currentPage = 1;
    const articlesPerPage = 6;
    
    // 模拟文章数据
    // 实际项目中应该从JSON文件或API获取
    const articlesData = [
        // 这里会有更多文章数据，现在先使用页面上已有的文章
        {
            id: '001',
            title: 'iPhone 16 Pro性能测试：A18 Pro芯片提升幅度惊人',
            excerpt: '苹果公司最新发布的iPhone 16 Pro搭载A18 Pro芯片，根据我们的详细测试，其GPU性能比上一代提升了近25%，CPU多核性能提升约20%。本文将带您深入了解这款强大芯片的各项性能表现。',
            category: 'news',
            date: '2024-10-15',
            image: '../public/images/news/featured-article.jpg',
            featured: true,
            products: ['iphone'],
            views: 5200
        },
        {
            id: '002',
            title: 'iPad Pro M4 vs M2：是否值得升级？',
            excerpt: '苹果最新的iPad Pro M4带来了哪些变化？相比上一代M2版本是否值得升级？本文将从显示屏、性能、续航等多方面进行详细对比。',
            category: 'comparisons',
            date: '2024-10-10',
            image: '../public/images/news/article1.jpg',
            featured: false,
            products: ['ipad'],
            views: 3200
        },
        {
            id: '003',
            title: 'Apple Watch Series 10深度评测：更大的屏幕，更强的续航',
            excerpt: '全新的Apple Watch Series 10采用了更大的显示屏和更高效的处理器，续航能力得到明显提升。我们进行了为期一周的深度测试。',
            category: 'reviews',
            date: '2024-10-05',
            image: '../public/images/news/article2.jpg',
            featured: false,
            products: ['watch'],
            views: 2800
        },
        {
            id: '004',
            title: '消息称MacBook Pro M4有望年底发布，将搭载M4 Pro和M4 Max芯片',
            excerpt: '根据供应链消息，苹果计划于今年12月推出搭载M4 Pro和M4 Max芯片的新款MacBook Pro，性能预计将有30%以上的提升。',
            category: 'rumors',
            date: '2024-09-30',
            image: '../public/images/news/article3.jpg',
            featured: false,
            products: ['mac'],
            views: 4500
        },
        {
            id: '005',
            title: 'iOS 18.1正式版新功能详解：Apple Intelligence全面体验',
            excerpt: 'iOS 18.1正式版已经推送，带来了Apple Intelligence的首批功能。本文详细介绍如何使用和设置这些AI功能，提升您的使用体验。',
            category: 'guides',
            date: '2024-09-25',
            image: '../public/images/news/article4.jpg',
            featured: false,
            products: ['ios'],
            views: 2100
        },
        {
            id: '006',
            title: '苹果收购AI初创公司，为Apple Intelligence添加更多功能',
            excerpt: '苹果公司近日收购了一家专注于自然语言处理的AI初创公司，据分析师称，这将为Apple Intelligence添加更强大的文本生成和理解能力。',
            category: 'news',
            date: '2024-09-20',
            image: '../public/images/news/article5.jpg',
            featured: false,
            products: ['ios'],
            views: 1900
        },
        // 更多文章数据...
    ];
    
    // 初始化页面
    initPage();
    
    /**
     * 初始化页面
     */
    function initPage() {
        // 绑定事件处理器
        bindEventHandlers();
        
        // 初始化返回顶部按钮
        initBackToTopButton();
        
        // 初始化文章展示
        renderArticles();
    }
    
    /**
     * 绑定事件处理器
     */
    function bindEventHandlers() {
        // 分类筛选
        document.querySelectorAll('.category-list li').forEach(category => {
            category.addEventListener('click', function() {
                currentCategory = this.dataset.category;
                
                // 更新选中状态
                document.querySelectorAll('.category-list li').forEach(item => {
                    item.classList.remove('active');
                });
                this.classList.add('active');
                
                // 重置页码
                currentPage = 1;
                
                // 重新渲染文章
                renderArticles();
            });
        });
        
        // 产品筛选
        document.querySelectorAll('.product-list li').forEach(product => {
            product.addEventListener('click', function() {
                // 如果点击当前选中的产品，则取消选择
                if (currentProduct === this.dataset.product) {
                    currentProduct = null;
                    this.classList.remove('active');
                } else {
                    currentProduct = this.dataset.product;
                    
                    // 更新选中状态
                    document.querySelectorAll('.product-list li').forEach(item => {
                        item.classList.remove('active');
                    });
                    this.classList.add('active');
                }
                
                // 重置页码
                currentPage = 1;
                
                // 重新渲染文章
                renderArticles();
            });
        });
        
        // 搜索
        const searchInput = document.querySelector('.search-box input');
        const searchButton = document.querySelector('.search-box button');
        
        // 点击搜索按钮
        searchButton.addEventListener('click', function() {
            searchQuery = searchInput.value.trim().toLowerCase();
            currentPage = 1;
            renderArticles();
        });
        
        // 按Enter键搜索
        searchInput.addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                searchQuery = this.value.trim().toLowerCase();
                currentPage = 1;
                renderArticles();
            }
        });
        
        // 分页
        document.querySelector('.pagination').addEventListener('click', function(event) {
            if (event.target.tagName === 'A') {
                event.preventDefault();
                
                // 如果点击的是下一页按钮
                if (event.target.innerHTML.includes('fa-chevron-right')) {
                    currentPage++;
                } else {
                    // 否则获取页码
                    currentPage = parseInt(event.target.textContent);
                }
                
                // 重新渲染文章
                renderArticles();
                
                // 滚动到文章列表顶部
                document.querySelector('.news-content').scrollIntoView({ behavior: 'smooth' });
            }
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
     * 渲染文章列表
     */
    function renderArticles() {
        // 筛选文章
        let filteredArticles = articlesData.filter(article => {
            // 分类筛选
            const categoryMatch = currentCategory === 'all' || article.category === currentCategory;
            
            // 产品筛选
            const productMatch = !currentProduct || article.products.includes(currentProduct);
            
            // 搜索筛选
            const searchMatch = !searchQuery || 
                article.title.toLowerCase().includes(searchQuery) || 
                article.excerpt.toLowerCase().includes(searchQuery);
            
            return categoryMatch && productMatch && searchMatch;
        });
        
        // 提取置顶文章
        const featuredArticle = filteredArticles.find(article => article.featured);
        
        // 从列表中移除置顶文章，以避免重复显示
        if (featuredArticle) {
            filteredArticles = filteredArticles.filter(article => article.id !== featuredArticle.id);
        }
        
        // 计算分页
        const totalPages = Math.ceil(filteredArticles.length / articlesPerPage);
        
        // 确保当前页不超出范围
        if (currentPage > totalPages) {
            currentPage = totalPages > 0 ? totalPages : 1;
        }
        
        // 获取当前页的文章
        const startIndex = (currentPage - 1) * articlesPerPage;
        const paginatedArticles = filteredArticles.slice(startIndex, startIndex + articlesPerPage);
        
        // 渲染置顶文章
        const featuredArticleContainer = document.querySelector('.featured-article');
        
        if (featuredArticle && currentPage === 1 && !currentProduct && currentCategory === 'all' && !searchQuery) {
            // 只在第一页且没有筛选条件时显示置顶文章
            featuredArticleContainer.style.display = 'flex';
            
            // 更新置顶文章内容
            featuredArticleContainer.querySelector('.article-title').textContent = featuredArticle.title;
            featuredArticleContainer.querySelector('.article-excerpt').textContent = featuredArticle.excerpt;
            featuredArticleContainer.querySelector('.article-category').textContent = getCategoryName(featuredArticle.category);
            featuredArticleContainer.querySelector('.article-date').textContent = formatDate(featuredArticle.date);
            featuredArticleContainer.querySelector('.featured-image img').src = featuredArticle.image;
            featuredArticleContainer.querySelector('.read-more').href = `article.html?id=${featuredArticle.id}`;
        } else {
            // 有筛选条件时不显示置顶文章
            featuredArticleContainer.style.display = 'none';
        }
        
        // 渲染文章列表
        const articlesGrid = document.querySelector('.articles-grid');
        articlesGrid.innerHTML = '';
        
        if (paginatedArticles.length === 0) {
            articlesGrid.innerHTML = `
                <div class="no-results">
                    <i class="fas fa-search"></i>
                    <p data-lang-key="news.noResults">没有找到相关文章</p>
                </div>
            `;
        } else {
            paginatedArticles.forEach(article => {
                const articleCard = document.createElement('div');
                articleCard.className = 'article-card';
                
                articleCard.innerHTML = `
                    <div class="article-image">
                        <img src="${article.image}" alt="${article.title}">
                        <div class="article-category" data-lang-key="news.category.${article.category}">${getCategoryName(article.category)}</div>
                    </div>
                    <div class="article-details">
                        <div class="article-meta">
                            <span class="article-date">${formatDate(article.date)}</span>
                            <span class="article-views"><i class="fas fa-eye"></i> ${formatViews(article.views)}</span>
                        </div>
                        <h3 class="article-title">${article.title}</h3>
                        <p class="article-excerpt">${article.excerpt}</p>
                        <a href="article.html?id=${article.id}" class="read-more" data-lang-key="news.readMore">阅读全文 <i class="fas fa-arrow-right"></i></a>
                    </div>
                `;
                
                articlesGrid.appendChild(articleCard);
            });
        }
        
        // 更新分页
        renderPagination(totalPages);
        
        // 应用语言本地化
        applyLanguage(localStorage.getItem('preferredLanguage') || 'zh-CN');
    }
    
    /**
     * 渲染分页控件
     */
    function renderPagination(totalPages) {
        const pagination = document.querySelector('.pagination');
        pagination.innerHTML = '';
        
        if (totalPages <= 1) {
            pagination.style.display = 'none';
            return;
        }
        
        pagination.style.display = 'flex';
        
        // 确定要显示的页码范围
        let startPage = Math.max(1, currentPage - 2);
        let endPage = Math.min(totalPages, startPage + 4);
        
        // 调整起始页，确保始终显示5个页码（如果有足够的页数）
        if (endPage - startPage < 4 && totalPages > 5) {
            startPage = Math.max(1, endPage - 4);
        }
        
        // 添加页码
        for (let i = startPage; i <= endPage; i++) {
            const pageLink = document.createElement('a');
            pageLink.href = '#';
            pageLink.textContent = i;
            
            if (i === currentPage) {
                pageLink.classList.add('active');
            }
            
            pagination.appendChild(pageLink);
        }
        
        // 添加下一页按钮（如果当前不是最后一页）
        if (currentPage < totalPages) {
            const nextLink = document.createElement('a');
            nextLink.href = '#';
            nextLink.innerHTML = '<i class="fas fa-chevron-right"></i>';
            pagination.appendChild(nextLink);
        }
    }
    
    /**
     * 获取分类名称
     */
    function getCategoryName(categoryKey) {
        const categories = {
            'news': '新闻动态',
            'reviews': '产品评测',
            'guides': '使用指南',
            'comparisons': '产品对比',
            'rumors': '传闻爆料'
        };
        
        return categories[categoryKey] || categoryKey;
    }
    
    /**
     * 格式化日期
     */
    function formatDate(dateString) {
        const date = new Date(dateString);
        return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`;
    }
    
    /**
     * 格式化浏览量
     */
    function formatViews(views) {
        if (views >= 1000) {
            return (views / 1000).toFixed(1) + 'k';
        }
        return views.toString();
    }
    
    /**
     * 应用语言本地化
     */
    function applyLanguage(lang) {
        // 这个函数会由language-switcher.js调用
        // 不需要在这里实现
    }
});
