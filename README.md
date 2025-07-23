# Apple参数大全 - 苹果产品参数对比平台

这是一个全面的苹果产品参数对比平台，提供iPhone、iPad、Apple Watch和Mac等产品的详细参数对比、最新资讯和用户反馈功能。

## 文档导航

- **[产品需求文档(PRD)](docs/prd.md)** - 详细的产品功能规格和技术要求
- **[市场需求文档(MRD)](docs/mrd.md)** - 产品定位、市场分析和用户需求
- **[文件命名与URL结构说明](docs/文件命名与URL结构说明.md)** - 项目文件组织和URL规范
- **[资讯文章管理指南](docs/资讯文章管理指南.md)** - 面向内容维护人员的文章管理说明

**推荐阅读顺序**：新加入项目的开发者建议先阅读本README文档了解项目概览，然后查看PRD了解详细功能需求，再参考文件命名规范了解代码组织。

## 项目结构

项目采用以下目录结构进行组织：

```
apple-comparison/
├── docs/                     # 文档文件
│   ├── mrd.md                # 市场需求文档
│   ├── prd.md                # 产品需求文档
│   └── 资讯文章管理指南.md    # 资讯文章管理指南
├── prototype/                # 原型文件
│   ├── ui1_首页.html          # 首页原型
│   ├── ui2_对比页.html        # 产品对比页原型
│   └── ui3_反馈页.html        # 用户反馈页原型
├── public/                   # 公共资源
│   ├── css/                  # CSS样式文件
│   │   ├── common.css        # 通用样式
│   │   ├── home.css          # 首页样式
│   │   ├── compare.css       # 产品对比页样式
│   │   ├── feedback.css      # 用户反馈页样式
│   │   ├── news.css          # 资讯页样式
│   │   └── article.css       # 文章详情页样式
│   ├── js/                   # JavaScript文件
│   │   ├── languages.js      # 语言资源
│   │   ├── language-switcher.js # 语言切换功能
│   │   ├── compare.js        # 产品对比页功能
│   │   ├── news.js           # 资讯页功能
│   │   └── article.js        # 文章详情页功能
│   ├── data/                 # 数据文件
│   │   └── iphone_refined.json # iPhone产品数据
│   └── images/               # 图片资源
│       ├── products/         # 产品图片
│       └── news/             # 资讯图片
└── src/                      # 源HTML文件
    ├── index.html            # 首页
    ├── iphone-compare.html   # iPhone产品对比页
    ├── feedback.html         # 用户反馈页
    ├── news.html             # 资讯页
    └── article.html          # 文章详情页
```

## 功能特点

### 数据维护

本项目采用单一数据源方案，所有iPhone产品数据均存储在 `public/data/iphone_refined.json` 文件中。

#### 数据更新流程

1. 直接编辑 `iphone_refined.json` 文件添加或修改产品数据
2. 或者使用 `tools/refine_iphone_data.js` 脚本进行批量数据处理：
   ```bash
   node tools/refine_iphone_data.js
   ```

#### 注意事项

- 每次更新数据时，脚本会自动创建备份文件
- 所有前端页面直接使用 `iphone_refined.json` 文件作为数据源
- 当添加新参数时，请同时更新前端对应的参数表格配置

### 1. 首页
- 四大产品线入口（iPhone、iPad、Apple Watch、Mac）
- 中英文双语切换功能
- 响应式设计，适配各种屏幕尺寸

**注意**：目前所有产品线入口都临时链接到iPhone对比页面，随着其他产品线对比页面的开发完成，将更新为对应的链接。

### 2. 产品对比页
- 每个产品线（iPhone、iPad、Apple Watch、Mac）设计独立的对比页面
- 当前已实现iPhone产品对比页（iphone-compare.html）
- 产品选择功能，可选择多个产品进行对比
- 参数差异高亮显示
- 固定表头第一横行和左侧列，方便浏览
- 性能数据可视化图表（使用Chart.js展示CPU和GPU性能）
  - 性能图表默认显示所有产品数据，不受产品选择状态影响
  - 图表逻辑独立于"查看对比"按钮，始终展示所有可用产品的性能对比
  - 支持在单核性能、多核性能和GPU性能之间切换

### 3. 用户反馈页
- 简洁的反馈表单，支持自由文本输入
- 站长联系信息展示
- 反馈提交功能

### 4. 苹果资讯页
- 文章分类筛选
- 产品相关筛选
- 文章分页

### 5. 文章详情页
- 文章内容展示
- 相关产品推荐
- 相关文章推荐
- 文章分享功能
- 评论功能

### 6. 全站功能
- 中英文双语切换
- 响应式设计
- 返回顶部按钮

## 运行项目

由于项目采用纯静态HTML/CSS/JavaScript实现，无需复杂的构建过程，可以通过以下方式运行：

### 方法1: 使用本地HTTP服务器

1. 在项目根目录下启动HTTP服务器：

```bash
# 如果安装了Python
python -m http.server

# 如果安装了Node.js
npx serve
```

2. 在浏览器中访问 `http://localhost:8000/src/` 查看网站

### 方法2: 直接在浏览器中打开HTML文件

1. 在文件浏览器中导航到项目的 `src` 目录
2. 双击 `index.html` 文件在浏览器中打开

## 开发和维护指南

### 添加新产品数据

1. 编辑 `public/data/` 目录下对应产品线的JSON文件
2. 按照现有格式添加新产品数据
3. 将产品图片添加到 `public/images/products/` 目录，命名为产品ID

### 添加新文章

1. 在 `public/js/news.js` 文件中的 `articlesData` 数组中添加新文章数据
2. 创建对应的文章详情页数据（在实际项目中应该使用数据库或CMS系统）
3. 将文章相关图片添加到 `public/images/news/` 目录

### 修改语言资源

1. 编辑 `public/js/languages.js` 文件，添加或修改语言键值对
2. 确保HTML元素使用正确的 `data-lang-key` 属性

## 部署指南

项目可以部署到任何静态网站托管服务，如Netlify、Vercel、GitHub Pages等：

1. 将项目上传到Git仓库
2. 在托管服务中连接到该仓库
3. 配置构建命令（如果有需要）
4. 设置发布目录为项目根目录或 `src` 目录（取决于托管服务的要求）

## 后续开发计划

1. 完善iPad、Apple Watch和Mac产品数据
2. 为iPad、Apple Watch和Mac产品线开发独立的对比页面（ipad-compare.html、watch-compare.html、mac-compare.html）
3. 实现数据更新工具，方便非技术人员维护产品数据
4. 增强性能对比图表，添加更多可视化效果
5. 优化移动端体验
6. 添加产品参数历史变化趋势分析功能
7. 集成真实评论系统

## 项目版权

&copy; 2025 Apple Compare. 所有权利均保留。

本网站与Apple Inc.没有任何关联。Apple、iPhone、iPad、Mac、Apple Watch等是Apple Inc.的商标。
