# 文件命名与URL结构说明

> 注意：本文档是[产品需求文档(PRD)](prd.md)的补充，专门针对项目的文件命名约定和URL结构提供详细指南。开发者应结合PRD一起阅读本文档。

## 开发阶段与发布阶段的文件命名约定

为确保开发过程清晰且最终产品符合标准网站结构，本项目采用了两套文件命名约定：

### 1. 开发阶段文件命名

在开发阶段，我们使用描述性的文件名，以便于区分不同页面原型：

| 开发阶段文件名 | 描述 |
|--------------|------|
| `ui1_首页.html` | 网站首页原型 |
| `ui2_对比页.html` | 产品参数对比页原型 |
| `ui3_反馈页.html` | 用户反馈页原型 |
| `ui4_资讯页.html` | 苹果资讯列表页原型 |
| `ui5_文章详情页.html` | 文章详情页原型 |

### 2. 发布阶段文件命名

在发布阶段，文件将重命名为符合标准网站结构的命名：

| 发布阶段文件名 | 对应开发阶段文件 |
|--------------|-----------------|
| `index.html` | ui1_首页.html |
| `compare.html` | ui2_对比页.html |
| `feedback.html` | ui3_反馈页.html |
| `news.html` | ui4_资讯页.html |
| `article.html` | ui5_文章详情页.html |

## URL结构规范

发布后的网站将使用以下URL结构：

| 页面 | URL格式 | 示例 |
|-----|--------|------|
| 首页 | `/` 或 `/index.html` | `https://applecompare.com/` |
| 产品对比页 | `/compare.html?type=产品类型` | `https://applecompare.com/compare.html?type=iphone` |
| 用户反馈页 | `/feedback.html` | `https://applecompare.com/feedback.html` |
| 资讯列表页 | `/news.html` 或 `/news.html?category=分类代码` | `https://applecompare.com/news.html?category=comparison` |
| 文章详情页 | `/article.html?id=文章ID` | `https://applecompare.com/article.html?id=iphone-16-vs-15-comparison` |

## 开发指南

为了确保从开发阶段到发布阶段的平滑过渡，请遵循以下指南：

1. **HTML链接属性**：
   - 在所有HTML文件中，使用`data-production-url`属性标记发布阶段的URL：
   ```html
   <a href="ui1_首页.html" data-production-url="index.html">首页</a>
   ```

2. **JavaScript链接处理**：
   - 在文章卡片点击事件中，使用条件判断处理不同阶段的URL：
   ```javascript
   // 示例：文章卡片点击处理
   function handleArticleClick(articleId) {
     const isProduction = process.env.NODE_ENV === 'production';
     const baseUrl = isProduction ? 'article.html' : 'ui5_文章详情页.html';
     location.href = `${baseUrl}?id=${articleId}`;
   }
   ```

3. **构建过程**：
   - 在构建脚本中添加文件重命名和链接替换逻辑：
   ```javascript
   // 构建脚本示例
   function processHtmlFiles() {
     // 重命名文件
     renameFile('ui1_首页.html', 'index.html');
     renameFile('ui2_对比页.html', 'compare.html');
     // ...
     
     // 替换链接
     replaceLinks('a[data-production-url]', (el) => {
       el.href = el.getAttribute('data-production-url');
       el.removeAttribute('data-production-url');
     });
   }
   ```

## 注意事项

1. 确保所有页面间的链接都使用相对路径，而不是绝对路径。
2. 在开发过程中使用`data-production-url`属性标记所有需要在发布时替换的链接。
3. 在JavaScript代码中处理动态生成的链接时，考虑当前环境（开发/生产）。
4. 确保所有API调用和资源引用也遵循相同的命名约定。

通过遵循这些指南，我们可以在开发阶段使用更具描述性的文件名，同时确保最终产品符合标准的网站URL结构。
