/**
 * 文章详情页面JavaScript功能
 * 
 * 主要功能：
 * 1. 根据URL参数加载对应文章
 * 2. 处理相关产品链接
 * 3. 文章分享功能
 * 4. 评论功能
 */

document.addEventListener('DOMContentLoaded', function() {
    // 初始化变量
    let articleId = null;
    
    // 模拟文章数据
    // 实际项目中应该从JSON文件或API获取
    const articlesData = [
        {
            id: '001',
            title: 'iPhone 16 Pro性能测试：A18 Pro芯片提升幅度惊人',
            content: document.getElementById('article-body').innerHTML, // 使用当前页面的内容作为默认内容
            category: 'news',
            date: '2024-10-15',
            author: 'Apple Compare 编辑部',
            image: '../public/images/news/article-detail.jpg',
            imageCaption: 'iPhone 16 Pro展示了强大的A18 Pro芯片性能',
            tags: ['iPhone 16 Pro', 'A18 Pro', '性能测试', '苹果芯片'],
            relatedProducts: [
                {
                    id: 'iphone-16-pro',
                    name: 'iPhone 16 Pro',
                    image: '../public/images/products/iphone16pro.jpg'
                },
                {
                    id: 'iphone-16-pro-max',
                    name: 'iPhone 16 Pro Max',
                    image: '../public/images/products/iphone16promax.jpg'
                },
                {
                    id: 'iphone-15-pro',
                    name: 'iPhone 15 Pro',
                    image: '../public/images/products/iphone15pro.jpg'
                }
            ],
            relatedArticles: [
                {
                    id: '007',
                    title: 'iPhone 16系列摄像头全面评测：Ultra新增变焦功能',
                    date: '2024-10-12',
                    image: '../public/images/news/related1.jpg'
                },
                {
                    id: '008',
                    title: 'iOS 18.1新功能详解：Apple Intelligence体验报告',
                    date: '2024-10-08',
                    image: '../public/images/news/related2.jpg'
                },
                {
                    id: '009',
                    title: 'M4芯片跑分曝光：性能提升超预期，Mac产品线或将全面更新',
                    date: '2024-10-03',
                    image: '../public/images/news/related3.jpg'
                }
            ],
            comments: [
                {
                    author: '王小明',
                    date: '2024-10-15 15:30',
                    content: '文章写得很详细，对于A18 Pro芯片的性能分析非常专业。我特别关注GPU性能的提升，因为我经常用iPhone玩游戏，25%的提升确实很可观。',
                    likes: 12,
                    avatar: '../public/images/user-avatar1.jpg'
                },
                {
                    author: '李晓华',
                    date: '2024-10-15 16:45',
                    content: '能否再详细说明一下A18 Pro在AI方面的具体应用场景？特别是与安卓旗舰机型相比，苹果的AI处理有什么优势？',
                    likes: 8,
                    avatar: '../public/images/user-avatar2.jpg'
                },
                {
                    author: '张科技',
                    date: '2024-10-15 18:20',
                    content: '温度控制这部分很有价值，之前用iPhone 15 Pro玩游戏时确实会感到明显发热。如果16 Pro真的能把温度降低2-3度，体验会好很多。另外，电池续航在游戏时提升15%也是个好消息。',
                    likes: 15,
                    avatar: '../public/images/user-avatar3.jpg'
                }
            ]
        },
        // 更多文章数据...
    ];
    
    // 初始化页面
    initPage();
    
    /**
     * 初始化页面
     */
    function initPage() {
        // 获取URL参数中的文章ID
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('id')) {
            articleId = urlParams.get('id');
            loadArticle(articleId);
        }
        
        // 绑定事件处理器
        bindEventHandlers();
        
        // 初始化返回顶部按钮
        initBackToTopButton();
    }
    
    /**
     * 加载文章内容
     */
    function loadArticle(id) {
        // 查找对应ID的文章
        const article = articlesData.find(article => article.id === id);
        
        if (!article) {
            // 文章不存在，显示错误信息
            showArticleNotFound();
            return;
        }
        
        // 更新页面标题
        document.title = `${article.title} - Apple Compare`;
        
        // 更新面包屑导航
        document.getElementById('article-title-breadcrumb').textContent = article.title;
        
        // 更新文章元数据
        document.getElementById('article-category').textContent = getCategoryName(article.category);
        document.getElementById('article-date').textContent = article.date;
        document.getElementById('article-author').textContent = `作者：${article.author}`;
        
        // 更新文章标题
        document.getElementById('article-title').textContent = article.title;
        
        // 更新文章图片
        document.getElementById('article-image').src = article.image;
        document.getElementById('article-image-caption').textContent = article.imageCaption;
        
        // 更新文章内容（这里不需要更新，因为我们使用的是当前页面的内容）
        // document.getElementById('article-body').innerHTML = article.content;
        
        // 更新文章标签
        updateArticleTags(article.tags);
        
        // 更新相关产品
        updateRelatedProducts(article.relatedProducts);
        
        // 更新相关文章
        updateRelatedArticles(article.relatedArticles);
        
        // 更新评论
        updateComments(article.comments);
    }
    
    /**
     * 显示文章未找到错误
     */
    function showArticleNotFound() {
        const articleContainer = document.querySelector('.article-content');
        articleContainer.innerHTML = `
            <div class="article-not-found">
                <i class="fas fa-exclamation-circle"></i>
                <h2 data-lang-key="article.notFound.title">文章未找到</h2>
                <p data-lang-key="article.notFound.message">
                    很抱歉，您请求的文章不存在或已被删除。
                </p>
                <a href="news.html" class="back-to-news" data-lang-key="article.notFound.back">
                    <i class="fas fa-arrow-left"></i> 返回资讯页面
                </a>
            </div>
        `;
    }
    
    /**
     * 更新文章标签
     */
    function updateArticleTags(tags) {
        const tagsContainer = document.querySelector('.article-tags');
        const tagsList = tagsContainer.querySelectorAll('.tag');
        
        // 清除现有标签
        tagsList.forEach(tag => tag.remove());
        
        // 添加新标签
        tags.forEach(tag => {
            const tagElement = document.createElement('a');
            tagElement.href = `news.html?search=${encodeURIComponent(tag)}`;
            tagElement.className = 'tag';
            tagElement.textContent = tag;
            tagsContainer.appendChild(tagElement);
        });
    }
    
    /**
     * 更新相关产品
     */
    function updateRelatedProducts(products) {
        const productsContainer = document.querySelector('.related-products');
        const productCards = productsContainer.querySelectorAll('.product-card');
        
        // 清除现有产品卡片
        productCards.forEach(card => card.remove());
        
        // 添加新产品卡片
        products.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';
            
            productCard.innerHTML = `
                <img src="${product.image}" alt="${product.name}">
                <div class="product-info">
                    <h4>${product.name}</h4>
                    <a href="compare.html?type=iphone&highlight=${product.id}" data-lang-key="article.viewSpecs">查看详细参数</a>
                </div>
            `;
            
            productsContainer.appendChild(productCard);
        });
    }
    
    /**
     * 更新相关文章
     */
    function updateRelatedArticles(articles) {
        const articlesContainer = document.querySelector('.related-article-list');
        
        // 清除现有文章
        articlesContainer.innerHTML = '';
        
        // 添加新文章
        articles.forEach(article => {
            const articleItem = document.createElement('a');
            articleItem.href = `article.html?id=${article.id}`;
            articleItem.className = 'related-article-item';
            
            articleItem.innerHTML = `
                <div class="related-article-image">
                    <img src="${article.image}" alt="${article.title}">
                </div>
                <div class="related-article-info">
                    <h4>${article.title}</h4>
                    <span class="related-article-date">${article.date}</span>
                </div>
            `;
            
            articlesContainer.appendChild(articleItem);
        });
    }
    
    /**
     * 更新评论
     */
    function updateComments(comments) {
        const commentsContainer = document.querySelector('.comments-list');
        
        // 清除现有评论
        commentsContainer.innerHTML = '';
        
        // 添加新评论
        comments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.className = 'comment';
            
            commentElement.innerHTML = `
                <div class="comment-avatar">
                    <img src="${comment.avatar}" alt="User avatar">
                </div>
                <div class="comment-content">
                    <div class="comment-header">
                        <span class="comment-author">${comment.author}</span>
                        <span class="comment-date">${comment.date}</span>
                    </div>
                    <p class="comment-text">${comment.content}</p>
                    <div class="comment-actions">
                        <button><i class="fas fa-thumbs-up"></i> ${comment.likes}</button>
                        <button><i class="fas fa-reply"></i> <span data-lang-key="article.reply">回复</span></button>
                    </div>
                </div>
            `;
            
            commentsContainer.appendChild(commentElement);
        });
    }
    
    /**
     * 绑定事件处理器
     */
    function bindEventHandlers() {
        // 分享按钮
        document.querySelector('.social-btn:first-child').addEventListener('click', function() {
            // 创建分享链接
            const shareUrl = encodeURIComponent(window.location.href);
            const shareTitle = encodeURIComponent(document.getElementById('article-title').textContent);
            
            // 创建分享弹窗
            const shareModal = document.createElement('div');
            shareModal.className = 'share-modal';
            
            shareModal.innerHTML = `
                <div class="share-modal-content">
                    <h3 data-lang-key="article.share.title">分享文章</h3>
                    <div class="share-options">
                        <a href="https://twitter.com/intent/tweet?url=${shareUrl}&text=${shareTitle}" target="_blank" class="share-option">
                            <i class="fab fa-twitter"></i>
                            <span>Twitter</span>
                        </a>
                        <a href="https://www.facebook.com/sharer/sharer.php?u=${shareUrl}" target="_blank" class="share-option">
                            <i class="fab fa-facebook"></i>
                            <span>Facebook</span>
                        </a>
                        <a href="https://www.linkedin.com/shareArticle?mini=true&url=${shareUrl}&title=${shareTitle}" target="_blank" class="share-option">
                            <i class="fab fa-linkedin"></i>
                            <span>LinkedIn</span>
                        </a>
                        <button class="share-option" id="copy-link">
                            <i class="fas fa-link"></i>
                            <span data-lang-key="article.share.copyLink">复制链接</span>
                        </button>
                    </div>
                    <button class="close-modal" data-lang-key="article.share.close">关闭</button>
                </div>
            `;
            
            document.body.appendChild(shareModal);
            
            // 复制链接按钮
            document.getElementById('copy-link').addEventListener('click', function() {
                navigator.clipboard.writeText(window.location.href).then(() => {
                    const span = this.querySelector('span');
                    const originalText = span.textContent;
                    span.textContent = '链接已复制';
                    
                    setTimeout(() => {
                        span.textContent = originalText;
                    }, 2000);
                });
            });
            
            // 关闭弹窗
            shareModal.querySelector('.close-modal').addEventListener('click', function() {
                document.body.removeChild(shareModal);
            });
            
            // 点击弹窗外部关闭弹窗
            shareModal.addEventListener('click', function(event) {
                if (event.target === shareModal) {
                    document.body.removeChild(shareModal);
                }
            });
        });
        
        // 收藏按钮
        document.querySelector('.social-btn:last-child').addEventListener('click', function() {
            // 切换收藏状态
            this.classList.toggle('active');
            
            // 更新图标和文本
            const icon = this.querySelector('i');
            const span = this.querySelector('span');
            
            if (this.classList.contains('active')) {
                icon.className = 'fas fa-bookmark';
                span.textContent = '已收藏';
                span.setAttribute('data-lang-key', 'article.saved');
            } else {
                icon.className = 'far fa-bookmark';
                span.textContent = '收藏';
                span.setAttribute('data-lang-key', 'article.save');
            }
            
            // 应用语言本地化
            applyLanguage(localStorage.getItem('preferredLanguage') || 'zh-CN');
        });
        
        // 评论提交
        document.querySelector('.comment-form button').addEventListener('click', function() {
            const commentTextarea = document.querySelector('.comment-form textarea');
            const commentText = commentTextarea.value.trim();
            
            if (commentText === '') {
                // 评论为空，显示提示
                const currentLang = localStorage.getItem('preferredLanguage') || 'zh-CN';
                const alertMsg = currentLang === 'zh-CN' ? '请输入评论内容' : 'Please enter your comment';
                alert(alertMsg);
                return;
            }
            
            // 创建新评论
            const newComment = {
                author: '游客',
                date: formatDate(new Date()),
                content: commentText,
                likes: 0,
                avatar: '../public/images/default-avatar.jpg'
            };
            
            // 添加新评论到列表
            const commentsContainer = document.querySelector('.comments-list');
            const commentElement = document.createElement('div');
            commentElement.className = 'comment';
            
            commentElement.innerHTML = `
                <div class="comment-avatar">
                    <img src="${newComment.avatar}" alt="User avatar">
                </div>
                <div class="comment-content">
                    <div class="comment-header">
                        <span class="comment-author">${newComment.author}</span>
                        <span class="comment-date">${newComment.date}</span>
                    </div>
                    <p class="comment-text">${newComment.content}</p>
                    <div class="comment-actions">
                        <button><i class="fas fa-thumbs-up"></i> ${newComment.likes}</button>
                        <button><i class="fas fa-reply"></i> <span data-lang-key="article.reply">回复</span></button>
                    </div>
                </div>
            `;
            
            // 将新评论插入到评论列表的顶部
            commentsContainer.insertBefore(commentElement, commentsContainer.firstChild);
            
            // 清空评论输入框
            commentTextarea.value = '';
            
            // 应用语言本地化
            applyLanguage(localStorage.getItem('preferredLanguage') || 'zh-CN');
        });
        
        // 加载更多评论按钮
        document.querySelector('.more-comments button').addEventListener('click', function() {
            // 模拟加载更多评论
            const moreComments = [
                {
                    author: '科技达人',
                    date: '2024-10-15 20:05',
                    content: '对比了一下A18 Pro和骁龙8 Gen 3，在单核性能上苹果还是领先不少，但多核差距在缩小。不过AI性能的40%提升确实令人印象深刻，这可能是苹果在这一代最大的突破。',
                    likes: 7,
                    avatar: '../public/images/user-avatar4.jpg'
                },
                {
                    author: '小苹果',
                    date: '2024-10-15 21:18',
                    content: '我已经预订了iPhone 16 Pro，看到这篇文章更期待了。不过我更关心它的实际使用体验，特别是电池续航和发热控制，希望真的像文章中说的那样有明显改善。',
                    likes: 4,
                    avatar: '../public/images/user-avatar5.jpg'
                }
            ];
            
            // 添加新评论到列表
            const commentsContainer = document.querySelector('.comments-list');
            
            moreComments.forEach(comment => {
                const commentElement = document.createElement('div');
                commentElement.className = 'comment';
                
                commentElement.innerHTML = `
                    <div class="comment-avatar">
                        <img src="${comment.avatar}" alt="User avatar">
                    </div>
                    <div class="comment-content">
                        <div class="comment-header">
                            <span class="comment-author">${comment.author}</span>
                            <span class="comment-date">${comment.date}</span>
                        </div>
                        <p class="comment-text">${comment.content}</p>
                        <div class="comment-actions">
                            <button><i class="fas fa-thumbs-up"></i> ${comment.likes}</button>
                            <button><i class="fas fa-reply"></i> <span data-lang-key="article.reply">回复</span></button>
                        </div>
                    </div>
                `;
                
                commentsContainer.appendChild(commentElement);
            });
            
            // 隐藏加载更多按钮，模拟已加载全部评论
            this.parentElement.style.display = 'none';
            
            // 应用语言本地化
            applyLanguage(localStorage.getItem('preferredLanguage') || 'zh-CN');
        });
        
        // 邮件订阅表单
        document.querySelector('.newsletter-form').addEventListener('submit', function(event) {
            event.preventDefault();
            
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();
            
            if (email === '' || !isValidEmail(email)) {
                const currentLang = localStorage.getItem('preferredLanguage') || 'zh-CN';
                const alertMsg = currentLang === 'zh-CN' ? '请输入有效的电子邮箱地址' : 'Please enter a valid email address';
                alert(alertMsg);
                return;
            }
            
            // 模拟订阅成功
            const currentLang = localStorage.getItem('preferredLanguage') || 'zh-CN';
            const successMsg = currentLang === 'zh-CN' ? '订阅成功！感谢您的关注' : 'Successfully subscribed! Thank you for your interest';
            alert(successMsg);
            
            // 清空输入框
            emailInput.value = '';
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
    function formatDate(date) {
        const year = date.getFullYear();
        const month = (date.getMonth() + 1).toString().padStart(2, '0');
        const day = date.getDate().toString().padStart(2, '0');
        const hours = date.getHours().toString().padStart(2, '0');
        const minutes = date.getMinutes().toString().padStart(2, '0');
        
        return `${year}-${month}-${day} ${hours}:${minutes}`;
    }
    
    /**
     * 验证邮箱格式
     */
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    /**
     * 应用语言本地化
     */
    function applyLanguage(lang) {
        // 这个函数会由language-switcher.js调用
        // 不需要在这里实现
    }
});
