# Apple参数大全 产品需求文档 (PRD)

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档名称 | Apple参数大全 产品需求文档 |
| 版本号 | v1.0 |
| 创建日期 | 2025-05-25 |
| 作者 | 产品团队 |
| 状态 | 初稿 |

## 1. 引言

### 1.1 目的

本文档详细描述了Apple参数大全产品的功能需求和技术规格，作为开发团队实现产品的指导文档。

### 1.2 范围

本文档涵盖Apple参数大全网站的所有功能模块、用户界面、数据结构和技术架构。

### 1.3 参考资料

- Apple官方技术规格网站
- 市场需求文档(MRD)
- iPhone数据表.xlsx（项目目录中的数据源文件）

## 2. 产品概述

Apple参数大全是一个专业的苹果产品参数信息展示平台，支持PC端和移动端访问。网站中展示不同型号的iPhone、iPad、Apple Watch和Mac产品的详细参数，同时提供不同产品的对比功能

## 3. 用户角色

| 角色 | 描述 | 需求重点 |
|------|------|---------|
| 普通消费者 | 对技术了解有限，关注性价比和实用性 | 简单易懂的参数对比，重点突出日常使用体验 |
| 科技爱好者 | 对技术细节敏感，追求高性能 | 全面详尽的技术参数，包括GPU性能数据 |
| 专业人士 | 使用苹果产品进行专业工作 | 特定专业场景下的性能参数和兼容性信息 |
| 企业采购人员 | 关注产品生命周期和兼容性 | 产品支持周期、企业功能信息 |
| 内容维护人员 | 负责产品数据的添加和更新 | 简单高效的数据更新工具 |

## 4. 功能规格

### 4.1 产品数据库

#### 4.1.1 iPhone产品数据

**数据源文件：** `/Users/aron/CascadeProjects/apple-comparison/iPhone数据表.xlsx`

**数据字段：**

| 字段类别 | 具体字段 | 数据类型 | 说明 |
|---------|---------|---------|------|
| 基本信息 | 产品名称 | 字符串 | 如"iPhone 16 Pro" |
| | 发布日期 | 日期 | 格式：YYYY-MM-DD |
| | 价格区间 | 字符串 | 如"5999-9999元" |
| | 型号标识符 | 字符串 | 如"A2650" |
| 外观参数 | 尺寸 | 字符串 | 长x宽x厚(mm) |
| | 重量 | 数值 | 单位：克 |
| | 颜色选项 | 数组 | 可选颜色列表 |
| | 材质 | 字符串 | 如"玻璃背板，不锈钢边框" |
| 显示参数 | 屏幕尺寸 | 数值 | 单位：英寸 |
| | 分辨率 | 字符串 | 如"2556 x 1179" |
| | PPI | 整数 | 像素密度 |
| | 刷新率 | 整数 | 单位：Hz |
| | 亮度(典型) | 整数 | 单位：尼特 |
| | 亮度(峰值) | 整数 | 单位：尼特 |
| | 色域 | 字符串 | 如"P3广色域" |
| | HDR支持 | 布尔值 | true/false |
| 性能参数 | 处理器型号 | 字符串 | 如"A17 Pro" |
| | 架构 | 字符串 | 如"6核心CPU" |
| | 核心数 | 整数 | CPU核心数量 |
| | GPU性能 | 整数 | GPU性能评分 |
| | RAM容量 | 整数 | 单位：GB |
| | 跑分数据 | 对象 | 包含多种跑分结果 |
| 存储参数 | 存储容量选项 | 数组 | 如[128, 256, 512, 1024] |
| 摄像系统 | 摄像头数量 | 整数 | 后置摄像头数量 |
| | 主摄像头像素 | 整数 | 单位：万像素 |
| | 光圈数值 | 字符串 | 如"f/1.8" |
| | 传感器尺寸 | 字符串 | 如"1/1.7英寸" |
| | 变焦能力 | 字符串 | 如"3倍光学变焦" |
| | 视频规格 | 字符串 | 如"4K@60fps" |
| 电池与充电 | 电池容量(mAh) | 整数 | 单位：mAh |
| | 电池容量(Wh) | 数值 | 单位：Wh |
| | 视频播放时间 | 整数 | 单位：小时 |
| | 音频播放时间 | 整数 | 单位：小时 |
| | 充电功率 | 整数 | 单位：W |
| | 无线充电 | 布尔值 | true/false |
| 连接性 | 蜂窝网络 | 字符串 | 如"5G" |
| | Wi-Fi标准 | 字符串 | 如"Wi-Fi 6E" |
| | 蓝牙版本 | 字符串 | 如"蓝牙5.3" |
| | NFC | 布尔值 | true/false |
| | 基带芯片 | 字符串 | 如"高通X70" |
| 系统与安全 | 最高支持iOS版本 | 字符串 | 如"iOS 18" |
| | 生物识别 | 字符串 | 如"Face ID" |
| 其他特性 | 防水等级 | 字符串 | 如"IP68" |
| | 扬声器配置 | 字符串 | 如"立体声扬声器" |
| | 特色功能 | 数组 | 特色功能列表 |
| 官方资料 | 技术规格链接 | 字符串 | URL |
| | 官方宣传口号 | 字符串 | 官方营销语 |

#### 4.1.2 iPad产品数据

**数据字段：** 与iPhone类似，但增加以下特有字段：

| 字段类别 | 具体字段 | 数据类型 | 说明 |
|---------|---------|---------|------|
| 连接与扩展 | Apple Pencil兼容性 | 字符串 | 如"支持Apple Pencil 2" |
| | 键盘兼容性 | 字符串 | 如"支持Magic Keyboard" |
| | 端口类型 | 字符串 | 如"USB-C" |

#### 4.1.3 Apple Watch产品数据

**数据字段：** 包含基本信息、显示、性能、健康功能、连接性、电池等类别的详细参数。

#### 4.1.4 Mac产品数据

**数据字段：** 包含基本信息、处理器、内存与存储、显示、图形、接口与连接性等类别的详细参数。

### 4.2 用户界面

#### 4.2.1 网站架构

网站将采用响应式设计，同时支持PC端和移动端访问。为了提供更直接的用户体验，网站架构简化为以下几个主要页面：

1. 首页（产品线入口）
2. 产品参数对比页（每个产品线独立页面）
   - iPhone产品对比页（iphone-compare.html）
   - iPad产品对比页（计划中的ipad-compare.html）
   - Apple Watch产品对比页（计划中的watch-compare.html）
   - Mac产品对比页（计划中的mac-compare.html）
3. 苹果资讯页
4. 用户反馈页
5. 数据更新工具（非网页形式）

#### 4.2.2 语言切换功能

**功能需求：**
- 支持中文和英文两种语言切换
- 自动检测用户浏览器语言设置，默认显示对应语言
- 保存用户语言偏好设置到localStorage，下次访问时自动应用
- 无需刷新页面即可切换语言
- 所有页面保持一致的语言切换体验

**UI元素：**
- 所有页面顶部导航栏中添加语言切换按钮
- 语言切换按钮包含中文和英文两个选项
- 当前选中语言以视觉差异方式呈现（如高亮、加粗等）

**交互规格：**
- 点击语言按钮：切换网站语言，无需刷新页面
- 语言切换后：所有页面文本内容更新为对应语言
- 语言设置保存：使用localStorage存储用户语言偏好
- URL参数：支持通过URL参数（如?lang=en）指定语言

#### 4.2.3 页面详细规格

##### 4.2.2.1 首页

**功能需求：**
- 展示四大产品线入口（iPhone、iPad、Apple Watch、Mac）
- 响应式设计，适配PC和移动端

**UI元素：**
- 顶部导航栏
- 产品线快速入口卡片（4个，以后会扩张多个）
- 网站简介和使用说明
- 页脚信息

**交互规格：**
- 点击产品线卡片：直接跳转至对应产品线的参数对比页

##### 4.2.2.2 产品参数展示页（按产品线独立实现）

**功能需求：**
- 按产品线分类，展示该产品线所有产品的完整参数
- 默认展示该产品线的所有产品，并按发布时间从新到旧排序
- 支持产品选择和取消，筛选后只显示关注的产品
- 页面底部展示数据可视化图表，包括：单核跑分对比图、多核跑分对比图、GPU分数对比图。图表设定容器高度为1600px，确保能完整显示所有机型。
- 性能图表需满足以下要求：
  - 以横向柱状图形式展示，确保所有机型名称完整显示在左侧
  - 每个机型名称右侧对应其性能得分柱状图
  - 图表标签不得被截断，需确保文本完整可见
  - 为每个产品项分配适当高度（14px），保持布局紧凑但清晰
  - 在用户悬停时显示详细信息，包括产品名称和具体性能分数
  - 标题与内容之间保持适当间距，提高视觉层次感

**UI元素：**
- 产品选择器（复选框）
- 性能对比图表
- “重置”按钮
- “对比”按钮

**交互规格：**
- 用户左右滚动网页时，确保表格第一束列固定显示（重要）
- 所有的参数都默认显示出来，不要折叠参数，不要对参数进行分类
- “重置”按钮：点击后重新展示所有产品和对应的参数
- “对比”按钮：点击后，只显示已经勾选的产品和对应的参数

##### 4.2.2.3 苹果资讯页（ui4_资讯页.html）

**功能需求：**

1. 苹果最新资讯文章列表
2. 热门机型对比文章
3. 文章分类筛选功能
4. 支持搜索文章
5. 分页浏览文章列表

**UI元素：**

1. 顶部导航栏（与其他页面一致）
2. 文章分类过滤器（标签式设计）
   - 所有文章
   - 新品发布（new_release）
   - 技术分析（tech_analysis）
   - 产品对比（comparison）
   - 使用技巧（tips）
   - 行业动态（industry）
3. 搜索框（右上角）
4. 文章卡片网格布局（每行2-3个卡片，响应式设计）
5. 每个文章卡片包含：
   - 缩略图、标题、摘要、发布日期、分类标签、阅读更多按钮
6. 分页导航（底部）
7. 热门文章侧边栏（PC端可见，移动端展示在底部）

**交互规格：**

1. 文章卡片点击：跳转到相应文章详情页
2. 分类标签点击：筛选当前分类的文章
3. 搜索框：输入关键词后点击搜索按钮或回车，显示符合条件的文章
4. 分页导航：点击页码或上一页/下一页按钮切换页面
5. 热门文章：点击跳转到相应文章

**数据交互：**

1. 加载时从本地JSON文件加载文章数据（/data/articles/articles.json）
2. 分类筛选、搜索和分页在前端实现
3. 每页默认显示9篇文章（可配置）

**应用状态管理：**

1. 使用URL参数保存当前状态：分类、搜索关键词、页码
   - 分类：?category=comparison
   - 搜索：?search=iPhone
   - 页码：?page=2
   - 组合：?category=comparison&search=iPhone&page=2

##### 4.2.2.4 文章详情页（ui5_文章详情页.html）

**功能需求：**

1. 展示完整文章内容，支持Markdown格式渲染
2. 展示文章相关信息（标题、作者、发布日期、分类等）
3. 相关产品参数快速查看和跳转
4. 相关文章推荐

**UI元素：**

1. 顶部导航栏（与其他页面一致）
2. 面包屑导航（首页 > 资讯 > 当前文章）
3. 文章头部：
   - 文章标题（大标题）
   - 发布信息（作者、日期、分类标签）
4. 文章正文：
   - 支持Markdown格式渲染
   - 支持图片、表格、代码块等元素
   - 清晰的段落和标题层次
5. 相关产品区域：
   - 展示文章中提到的产品卡片
   - 每个卡片包含产品名称、简要参数和跳转链接
6. 相关文章推荐：
   - 展示3-5篇相关文章卡片
7. 返回顶部按钮

**交互规格：**

1. 从文章URL加载文章ID（如ui5_文章详情页.html?id=iphone-16-vs-15-comparison）
2. 根据ID从文章数据中获取并渲染文章内容
3. 点击分类标签：跳转到资讯页并筛选该分类
4. 点击相关产品卡片：跳转到产品参数展示页
5. 点击相关文章：跳转到相应文章详情页
6. 图片点击：可放大查看（可选实现）

**数据交互：**

1. 从本地JSON文件加载文章数据（/data/articles/articles.json）
2. 使用Markdown渲染库（如marked.js）渲染文章内容
3. 相关产品数据从产品数据文件中获取（related_products字段关联）
4. 相关文章推荣基于当前文章的分类和标签生成

##### 4.2.2.5 用户反馈页

**功能需求：**

1. 简单的反馈表单，包含一个多行文本输入框
2. 显示站长联系信息（邮箱、QQ、QQ群）

**交互规格：**

1. 用户可在文本输入框中自由填写反馈内容、联系方式等信息
2. 提交按钮发送反馈内容
3. 页面显示站长联系方式：
   - 邮箱：fzpzac@qq.com
   - QQ：996208608
   - QQ群：待定

##### 4.2.2.6 数据更新工具

**功能需求：**
- 产品数据管理（添加、编辑、删除）
- 资讯文章管理（撰写、编辑、发布）
- 用户反馈查看和处理
- JSON数据导入导出
- 从电子表格（如iPhone数据表.xlsx）导入数据
- Markdown格式文章编辑

**实现方式：**
- 轻量级命令行工具（基于Node.js）
- 交互式命令行界面（使用inquirer等库提供友好交互）
- 简单的菜单选择和表单填写流程
- 文本编辑器集成（用于Markdown内容编辑）

**交互规格：**
- 主菜单选择功能：产品管理、文章管理、反馈处理等
- 添加新产品：通过命令行问答填写产品信息
- 编辑产品：选择产品和参数，输入新值
- 导入电子表格：指定Excel文件路径，自动解析并映射到JSON结构
- 处理用户反馈：查看反馈列表，选择操作
- 发布更新：自动提交到Git并触发部署

### 4.3 API规格（后期扩展计划）

> 注意：以下API规格为后期扩展计划。MVP阶段采用静态JSON文件架构，前端直接加载JSON文件并处理数据。

#### 4.3.1 产品列表API

**端点：** `GET /api/products`

**参数：**
- `type`: 产品类型（iphone/ipad/watch/mac）
- `year`: 发布年份
- `price_min`: 最低价格
- `price_max`: 最高价格
- `feature`: 特定功能
- `sort`: 排序方式（date/price/performance）
- `order`: 排序顺序（asc/desc）
- `page`: 页码
- `limit`: 每页数量

**响应：**
```json
{
  "total": 36,
  "page": 1,
  "limit": 20,
  "products": [
    {
      "id": "iphone-16-pro",
      "name": "iPhone 16 Pro",
      "release_date": "2024-09-20",
      "price_range": "8999-11999元",
      "image_url": "/images/iphone-16-pro.jpg",
      "key_specs": {
        "screen": "6.3英寸",
        "processor": "A18 Pro",
        "camera": "4800万像素三摄",
        "battery": "4422mAh"
      }
    },
    // 更多产品...
  ]
}
```

#### 4.3.2 产品详情API

**端点：** `GET /api/products/:id`

**参数：**
- `id`: 产品ID或型号标识符

**响应：**
```json
{
  "id": "iphone-16-pro",
  "name": "iPhone 16 Pro",
  "type": "iphone",
  "release_date": "2024-09-20",
  "price_range": "8999-11999元",
  "model_identifier": "A2650",
  "images": [
    "/images/iphone-16-pro-front.jpg",
    "/images/iphone-16-pro-back.jpg"
  ],
  "basic_info": {
    // 基本信息字段
  },
  "display": {
    // 显示参数字段
  },
  "performance": {
    "processor": "A18 Pro",
    "architecture": "6核心CPU",
    "cores": 6,
    "gpu_performance": 32746,
    "ram": 8,
    "benchmarks": {
      "geekbench_single": 2890,
      "geekbench_multi": 7230,
      "antutu": 1520000
    }
  },
  // 其他参数类别...
}
```

#### 4.3.3 产品对比API

**端点：** `GET /api/compare`

**参数：**
- `products`: 产品ID列表，逗号分隔
- `fields`: 对比字段类别，逗号分隔（可选）

**响应：**
```json
{
  "products": [
    {
      "id": "iphone-16-pro",
      "name": "iPhone 16 Pro",
      // 完整产品数据
    },
    {
      "id": "iphone-15-pro",
      "name": "iPhone 15 Pro",
      // 完整产品数据
    }
  ],
  "differences": {
    "display.screen_size": {
      "iphone-16-pro": 6.3,
      "iphone-15-pro": 6.1
    },
    "performance.gpu_performance": {
      "iphone-16-pro": 32746,
      "iphone-15-pro": 28542
    },
    // 其他差异字段
  }
}
```

#### 4.3.4 苹果资讯API

**文章分类对应表：**

| 分类代码 | 中文显示名称 | 描述 |
|---------|------------|------|
| new_release | 新品发布 | 苹果新产品发布相关资讯 |
| tech_analysis | 技术分析 | 苹果产品技术特性深度分析 |
| comparison | 产品对比 | 不同苹果产品间的参数对比 |
| tips | 使用技巧 | 苹果产品使用技巧和窍门 |
| industry | 行业动态 | 苹果公司及相关行业新闻 |

**端点：** `GET /api/articles`

**参数：**
- `category`: 文章分类（参见上方分类对应表）
- `page`: 页码
- `limit`: 每页数量

**响应：**
```json
{
  "total": 42,
  "page": 1,
  "limit": 10,
  "articles": [
    {
      "id": "iphone-16-vs-15-comparison",
      "title": "iPhone 16 vs iPhone 15：值得升级吗？",
      "category": "comparison",
      "summary": "详细对比两代iPhone的性能、相机和电池续航...",
      "thumbnail": "/images/articles/iphone-16-vs-15.jpg",
      "published_at": "2025-05-20T10:00:00Z",
      "tags": ["iPhone 16", "iPhone 15", "产品对比"]
    },
    // 更多文章...
  ]
}
```

**端点：** `GET /api/articles/:id`

**参数：**
- `id`: 文章ID

**响应：**
```json
{
  "id": "iphone-16-vs-15-comparison",
  "title": "iPhone 16 vs iPhone 15：值得升级吗？",
  "category": "comparison",
  "content": "# iPhone 16 vs iPhone 15\n\n苹果在上月发布了最新的iPhone 16系列...",
  "thumbnail": "/images/articles/iphone-16-vs-15.jpg",
  "published_at": "2025-05-20T10:00:00Z",
  "author": "Apple Compare 编辑部",
  "tags": ["iPhone 16", "iPhone 15", "产品对比"],
  "related_products": ["iphone-16", "iphone-15"],
  "meta": {
    "seo_title": "iPhone 16 vs iPhone 15详细对比分析 - Apple Compare",
    "seo_description": "详细对比iPhone 16与iPhone 15的性能、相机、电池续航等关键参数，帮您决定是否值得升级。",
    "seo_keywords": "iPhone 16, iPhone 15, 对比, 参数, 升级, 苹果"
  }
}
```

#### 4.3.5 用户反馈API

**端点：** `POST /api/feedback`

**请求体：**
```json
{
  "content": "反馈内容，可能包含用户自行填写的联系方式等信息"
}
```

**响应：**
```json
{
  "success": true,
  "message": "感谢您的反馈，我们会尽快处理"
}
```

### 4.4 数据模型

#### 4.4.1 产品数据模型

```javascript
// MongoDB产品集合示例结构
{
  "_id": ObjectId("..."),
  "id": "iphone-16-pro",
  "name": "iPhone 16 Pro",
  "type": "iphone",
  "release_date": ISODate("2024-09-20"),
  "price_range": "8999-11999元",
  "model_identifier": "A2650",
  "images": [...],
  "basic_info": {...},
  "display": {...},
  "performance": {...},
  "storage": {...},
  "camera": {...},
  "battery": {...},
  "connectivity": {...},
  "system": {...},
  "other_features": {...},
  "official_info": {...},
  "created_at": ISODate("..."),
  "updated_at": ISODate("...")
}
```

#### 4.4.2 苹果资讯文章数据模型

```javascript
// articles/articles.json
{
  "version": "2025-05-26",
  "articles": [
    {
      "id": "iphone-16-vs-15-comparison",
      "title": "iPhone 16 vs iPhone 15：值得升级吗？",
      "category": "comparison", // 文章分类代码，参见4.3.4节分类对应表
      "summary": "详细对比两代iPhone的性能、相机和电池续航...",
      "content": "# iPhone 16 vs iPhone 15\n\n苹果在上月发布了最新的iPhone 16系列...",
      "thumbnail": "/images/articles/iphone-16-vs-15.jpg",
      "published_at": "2025-05-20T10:00:00Z",
      "author": "Apple Compare 编辑部",
      "tags": ["iPhone 16", "iPhone 15", "产品对比"],
      "related_products": ["iphone-16", "iphone-15"],
      "meta": {
        "seo_title": "iPhone 16 vs iPhone 15详细对比分析 - Apple Compare",
        "seo_description": "详细对比iPhone 16与iPhone 15的性能、相机、电池续航等关键参数，帮您决定是否值得升级。",
        "seo_keywords": "iPhone 16, iPhone 15, 对比, 参数, 升级, 苹果"
      },
      "created_at": "2025-05-19T14:30:00Z",
      "updated_at": "2025-05-20T09:45:00Z"
    }
  ]
}
```

#### 4.4.3 用户反馈数据模型

```javascript
// 用户反馈JSON文件结构
{
  "_id": "fb-12345",
  "content": "用户反馈内容，包含用户自行填写的联系方式",
  "created_at": "2025-05-26T13:45:00Z"
}
```

## 5. 非功能需求

### 5.1 性能需求

- 页面加载时间：首次加载 < 3秒，后续页面 < 1秒
- 并发用户支持：同时支持1000+用户访问
- 对比功能响应时间：< 500ms
- 移动端流量优化：首页加载资源 < 2MB

### 5.2 安全需求

- 数据更新工具访问控制：仅授权人员可使用
- 静态资源保护：防止未授权修改
- 数据备份：Git版本控制系统自动跟踪和备份所有数据文件变更
- 部署安全：仅允许通过CI/CD流程部署更新

### 5.3 兼容性需求

- 浏览器兼容性：支持最新版Chrome、Firefox、Safari、Edge
- 移动设备兼容性：支持iOS 14+和Android 10+
- 响应式设计：适配从320px到2560px的各种屏幕尺寸

### 5.4 可访问性需求

- 符合WCAG 2.1 AA级标准
- 支持屏幕阅读器
- 提供足够的颜色对比度
- 键盘导航支持

## 6. 技术架构

### 6.1 技术架构优化方案

为了实现最快上线并简化开发流程，本项目采用基于JSON文件的静态网站方案，而非传统的前后端分离架构。这种方案无需开发管理员后台，显著减少开发时间和维护成本。同时，静态文件架构支持文章内容的SEO优化，便于搜索引擎发现网站内容。

#### 6.1.1 前端技术栈

**MVP阶段（快速上线）：**
- **原生技术**：HTML5 + CSS3 + JavaScript（原生）
- **轻量级库**：Marked.js（Markdown解析）
- **数据加载**：fetch API
- **响应式设计**：原生CSS媒体查询

**后期扩展（可选）：**
- **框架**：React.js
- **UI库**：Material-UI或Ant Design
- **状态管理**：Redux或Context API
- **数据可视化**：D3.js或Chart.js
- **响应式设计**：Tailwind CSS

#### 6.1.2 数据管理方案

**JSON文件存储结构：**

```javascript
// 产品数据：products/iphones.json
{
  "version": "2025-05-25",
  "products": [
    {
      "id": "iphone-16-pro",
      "name": "iPhone 16 Pro",
      // 所有详细参数...
    },
    // 更多iPhone产品...
  ]
}
```

**数据组织方式：**
- 按产品类别分文件存储（iphones.json, ipads.json等）
- 所有JSON文件保存在项目的`/data/products/`目录下
- 前端直接导入或通过fetch加载这些JSON文件

**前端实现示例：**

```javascript
// 在React组件中
import iphoneData from '/data/products/iphones.json';
import ipadData from '/data/products/ipads.json';

// 合并所有产品数据
const allProducts = {
  iphone: iphoneData.products,
  ipad: ipadData.products,
  // ...其他产品线
};

// 使用数据
function ProductList({ type }) {
  const products = allProducts[type] || [];
  return (
    <div>
      {products.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}
```

#### 6.1.3 数据更新工具

为了方便非技术人员更新数据，开发一个简单的数据更新工具。该工具将提供以下功能：

1. 产品数据管理（添加、编辑、删除）
2. 资讯文章管理（撰写、编辑、发布）
3. 从电子表格导入数据
4. 用户反馈管理
5. 数据验证与发布

##### 工具实现示例

```javascript
// update-tool.js
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const xlsx = require('xlsx');
const inquirer = require('inquirer');

// 读取现有数据
const productsPath = path.join(__dirname, '../data/products/iphones.json');
const productsData = JSON.parse(fs.readFileSync(productsPath, 'utf8'));

// 读取文章数据
const articlesPath = path.join(__dirname, '../data/articles/articles.json');
let articlesData;
try {
  articlesData = JSON.parse(fs.readFileSync(articlesPath, 'utf8'));
} catch (error) {
  // 如果文件不存在，创建一个新的文章集合
  articlesData = {
    version: new Date().toISOString().split('T')[0],
    articles: []
  };
  // 确保目录存在
  const articlesDir = path.dirname(articlesPath);
  if (!fs.existsSync(articlesDir)) {
    fs.mkdirSync(articlesDir, { recursive: true });
  }
}

// 添加新产品
async function addNewProduct() {
  const answers = await inquirer.prompt([
    { type: 'input', name: 'id', message: '请输入产品ID(如iphone-17-pro):' },
    { type: 'input', name: 'name', message: '请输入产品名称:' },
    { type: 'input', name: 'releaseDate', message: '请输入发布日期(YYYY-MM-DD):' },
    // 更多参数字段...
  ]);
  
  productsData.products.push({
    id: answers.id,
    name: answers.name,
    releaseDate: answers.releaseDate,
    // 其他参数...
  });
  
  // 保存更新后的数据
  fs.writeFileSync(productsPath, JSON.stringify(productsData, null, 2));
  console.log(`成功添加产品: ${answers.name}`);
}

// 添加新文章
async function addNewArticle() {
  const answers = await inquirer.prompt([
    { type: 'input', name: 'id', message: '请输入文章ID(如iphone-16-vs-15-comparison):' },
    { type: 'input', name: 'title', message: '请输入文章标题:' },
    { type: 'list', name: 'category', message: '请选择文章分类:', 
      choices: ['new_release', 'tech_analysis', 'comparison', 'tips', 'industry'] },
    { type: 'input', name: 'summary', message: '请输入文章摘要(150字以内):' },
    { type: 'input', name: 'thumbnail', message: '请输入缩略图路径:' },
    { type: 'input', name: 'author', message: '请输入作者:' },
    { type: 'editor', name: 'content', message: '请编写文章内容(Markdown格式):' },
    { type: 'input', name: 'tags', message: '请输入标签(逗号分隔):' },
    { type: 'input', name: 'related_products', message: '请输入相关产品ID(逗号分隔):' },
    { type: 'input', name: 'seo_title', message: '请输入SEO标题:' },
    { type: 'input', name: 'seo_description', message: '请输入SEO描述:' },
    { type: 'input', name: 'seo_keywords', message: '请输入SEO关键词(逗号分隔):' }
  ]);
  
  const now = new Date().toISOString();
  
  articlesData.articles.unshift({
    id: answers.id,
    title: answers.title,
    category: answers.category,
    summary: answers.summary,
    content: answers.content,
    thumbnail: answers.thumbnail,
    published_at: now,
    author: answers.author,
    tags: answers.tags.split(',').map(tag => tag.trim()),
    related_products: answers.related_products.split(',').map(id => id.trim()),
    meta: {
      seo_title: answers.seo_title,
      seo_description: answers.seo_description,
      seo_keywords: answers.seo_keywords
    },
    created_at: now,
    updated_at: now
  });
  
  // 更新版本号
  articlesData.version = new Date().toISOString().split('T')[0];
  
  // 保存更新后的数据
  fs.writeFileSync(articlesPath, JSON.stringify(articlesData, null, 2));
  console.log(`成功添加文章: ${answers.title}`);
}

// 从 Excel 导入数据
function importFromExcel() {
  const excelPath = path.join(__dirname, 'iPhone数据表.xlsx');
  const workbook = xlsx.readFile(excelPath);
  const sheetName = workbook.SheetNames[0];
  const sheet = workbook.Sheets[sheetName];
  const excelData = xlsx.utils.sheet_to_json(sheet);
  
  // 处理导入的数据
  excelData.forEach(row => {
    // 映射 Excel 列到 JSON 字段
    const product = {
      id: `iphone-${row['型号'].toLowerCase().replace(/\s+/g, '-')}`,
      name: row['型号'],
      releaseDate: row['发布日期'],
      // 映射其他字段...
    };
    
    // 检查是否已存在该产品
    const existingIndex = data.products.findIndex(p => p.id === product.id);
    if (existingIndex >= 0) {
      // 更新现有产品
      data.products[existingIndex] = { ...data.products[existingIndex], ...product };
      console.log(`更新产品: ${product.name}`);
    } else {
      // 添加新产品
      data.products.push(product);
      console.log(`添加产品: ${product.name}`);
    }
  });
  
  // 保存更新后的数据
  fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
  console.log(`导入完成，共处理 ${excelData.length} 条数据`);
}

// 发布更新到Git仓库
function publishChanges() {
  try {
    // Git 操作
    execSync('git add .');
    execSync('git commit -m "Update product data"');
    execSync('git push');
    console.log('数据更新已提交到Git仓库，网站将自动部署更新');
  } catch (error) {
    console.error('提交失败:', error.message);
  }
}

// 管理用户反馈
async function manageFeedback() {
  // 读取反馈数据
  const feedbackPath = path.join(__dirname, '../data/feedback.json');
  const feedback = JSON.parse(fs.readFileSync(feedbackPath, 'utf8'));
  
  // 显示所有反馈
  console.log(`共有 ${feedback.items.length} 条反馈`);
  
  for (const item of feedback.items) {
    console.log(`
反馈ID: ${item._id}`);
    console.log(`内容: ${item.content}`);
    console.log(`提交时间: ${item.created_at}`);
    
    const { action } = await inquirer.prompt([
      {
        type: 'list',
        name: 'action',
        message: '请选择操作:',
        choices: ['删除', '保留', '下一条']
      }
    ]);
    
    if (action === '删除') {
      feedback.items = feedback.items.filter(f => f._id !== item._id);
      fs.writeFileSync(feedbackPath, JSON.stringify(feedback, null, 2));
      console.log(`已删除反馈 ${item._id}`);
    }
  }
}

// 主菜单
async function mainMenu() {
  while (true) {
    const { action } = await inquirer.prompt([
      {
        type: 'list',
        name: 'action',
        message: '请选择操作:',
        choices: [
          '添加新产品',
          '编辑现有产品',
          '从 Excel 导入数据',
          '管理用户反馈',
          '发布更新',
          '退出'
        ]
      }
    ]);
    
    switch (action) {
      case '添加新产品':
        await addNewProduct();
        break;
      case '编辑现有产品':
        await editProduct();
        break;
      case '从 Excel 导入数据':
        importFromExcel();
        break;
      case '管理用户反馈':
        await manageFeedback();
        break;
      case '发布更新':
        publishChanges();
        break;
      case '退出':
        console.log('感谢使用数据更新工具，再见!');
        return;
    }
  }
}

// 启动工具
mainMenu().catch(console.error);

// 更新版本
data.version = new Date().toISOString().split('T')[0];

// 保存数据
fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
console.log('数据更新完成!');

// 自动提交并部署
execSync('git add .');
execSync('git commit -m "Update product data"');
execSync('git push');

console.log('数据已更新并部署');
```

##### 数据更新工具使用指南

为了确保内容维护人员能够高效地使用数据更新工具，以下是详细的使用指南：

**安装与配置**

1. 确保您的计算机已安装 Node.js (版本 14 或更高)
2. 首次使用前，请在命令行中运行以下命令安装必要的依赖包：
   ```
   npm install inquirer@8.2.4 xlsx
   ```
3. 确保您已经配置好 Git 账户并有权限提交到项目仓库

**启动工具**

在项目根目录下运行以下命令启动数据更新工具：

```
node tools/update-tool.js
```

**主要功能使用说明**

1. **添加新产品**
   - 选择“添加新产品”选项
   - 按照提示输入产品 ID、名称、发布日期等信息
   - 工具会自动将新产品添加到相应的 JSON 文件中

2. **编辑现有产品**
   - 选择“编辑现有产品”选项
   - 选择要编辑的产品类别和具体产品
   - 选择要编辑的参数字段并输入新值
   - 工具会自动更新并保存修改

3. **从 Excel 导入数据**
   - 将产品数据整理到 Excel 表格中（如 “iPhone数据表.xlsx”）
   - 确保 Excel 表格的列名与工具中的映射关系一致
   - 选择“从 Excel 导入数据”选项
   - 工具会自动读取、处理并导入数据，同时显示处理进度

4. **管理用户反馈**
   - 选择"管理用户反馈"选项
   - 工具会显示所有用户反馈
   - 您可以选择删除或保留反馈
   - 如需要回复用户，请使用用户提供的联系方式直接联系

5. **发布更新**
   - 完成数据编辑后，选择“发布更新”选项
   - 工具会自动提交更改到 Git 仓库
   - 如果项目配置了 CI/CD，网站将自动部署更新

**注意事项**

1. 每次运行工具前，建议先使用 `git pull` 命令获取最新的数据
2. 如果遇到 Git 冲突，请联系技术人员协助解决
3. 导入 Excel 数据前，请确保数据格式正确，避免空值或格式错误
4. 工具会自动备份原有数据，但建议在大规模更新前手动备份重要数据

**常见问题解决**

1. 如果工具无法启动，请检查 Node.js 环境是否正确安装
2. 如果遇到“模块未找到”错误，请运行 `npm install` 安装依赖
3. 如果发布更新失败，请检查 Git 账户权限和网络连接

如果需要更多帮助，请联系技术支持团队。

这个轻量级命令行工具设计简单直观，即使非技术人员经过简单培训也能快速上手使用，满足MVP阶段的数据管理需求。

#### 6.1.4 文件结构与部署架构

为了实现最快上线，本项目采用静态HTML结合JavaScript动态加载的方式，无需额外的后端服务。

##### 开发阶段与发布阶段的文件命名约定

**1. 开发阶段文件命名**

在开发阶段，我们使用描述性的文件名，以便于区分不同页面原型：

| 开发阶段文件名 | 描述 |
|--------------|------|
| `ui1_首页.html` | 网站首页原型 |
| `ui2_对比页.html` | 产品参数对比页原型 |
| `ui3_反馈页.html` | 用户反馈页原型 |
| `ui4_资讯页.html` | 苹果资讯列表页原型 |
| `ui5_文章详情页.html` | 文章详情页原型 |

**2. 发布阶段文件命名**

在发布阶段，文件将重命名为符合标准网站结构的命名：

| 发布阶段文件名 | 对应开发阶段文件 |
|--------------|------------------|
| `index.html` | ui1_首页.html |
| `compare.html` | ui2_对比页.html |
| `feedback.html` | ui3_反馈页.html |
| `news.html` | ui4_资讯页.html |
| `article.html` | ui5_文章详情页.html |

##### URL结构规范

> 注意：关于更详细的文件命名约定和URL结构规范，请参考[文件命名与URL结构说明](文件命名与URL结构说明.md)文档。

发布后的网站将使用以下URL结构：

| 页面 | URL格式 | 示例 |
|------|--------|------|
| 首页 | /index.html | https://example.com/index.html |
| iPhone对比页 | /iphone-compare.html | https://example.com/iphone-compare.html |
| iPad对比页 | /ipad-compare.html | https://example.com/ipad-compare.html |
| Apple Watch对比页 | /watch-compare.html | https://example.com/watch-compare.html |
| Mac对比页 | /mac-compare.html | https://example.com/mac-compare.html |
| 资讯页 | /news.html | https://example.com/news.html |
| 文章详情页 | /article.html?id={articleId} | https://example.com/article.html?id=iphone-16-review |
| 用户反馈页 | /feedback.html | https://example.com/feedback.html |

##### 完整项目结构

发布阶段的完整项目结构如下：

```
/
├─ index.html (首页)
├─ compare.html (产品对比页)
├─ feedback.html (用户反馈页)
├─ news.html (资讯列表页)
├─ article.html (文章详情页)
├─ css/
│   └─ styles.css
├─ js/
│   ├─ main.js (主要功能脚本)
│   ├─ compare.js (对比功能脚本)
│   ├─ articles.js (文章加载脚本)
│   └─ marked.min.js (Markdown解析库)
├─ data/
│   ├─ products/
│   │   ├─ iphones.json
│   │   ├─ ipads.json
│   │   ├─ watches.json
│   │   └─ macs.json
│   ├─ articles/
│   │   └─ articles.json
│   └─ feedback/
│       └─ feedback.json
└─ images/
    ├─ products/
    ├─ articles/
    └─ ui/
    └─ articles/
```

**URL结构：**

发布后的网站将使用以下URL结构：

- 首页：`/`或`/index.html`
- 产品对比页：`/compare.html?type=iphone`
- 资讯列表页：`/news.html`或`/news.html?category=comparison`
- 文章详情页：`/article.html?id=iphone-16-vs-15-comparison`
- 反馈页：`/feedback.html`

**文章列表页实现：**

```javascript
// 加载文章列表
try {
  // 显示加载状态
  const articlesContainer = document.querySelector('.article-grid');
  articlesContainer.innerHTML = '<div class="loading-indicator">正在加载文章...</div>';
  
  fetch('/data/articles/articles.json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`网络响应异常: ${response.status} ${response.statusText}`);
      }
      return response.json();
    })
    .then(data => {
      if (!data || !data.articles || !Array.isArray(data.articles) || data.articles.length === 0) {
        throw new Error('文章数据为空或格式不正确');
      }
      
      const articles = data.articles;
      
      // 清空容器
      articlesContainer.innerHTML = '';
      
      // 添加特色文章（最新的一篇）
      const featuredArticle = articles[0];
      const featuredArticleHTML = `
        <div class="article-card featured-article" onclick="location.href='article.html?id=${featuredArticle.id}'">
          <div class="article-image">
            <img src="${featuredArticle.thumbnail}" alt="${featuredArticle.title}" onerror="this.src='/images/placeholder.jpg'; this.onerror=null;">
          </div>
          <div class="article-content">
            <span class="article-category ${featuredArticle.category}">${getCategoryName(featuredArticle.category)}</span>
            <h2 class="article-title">${featuredArticle.title}</h2>
            <div class="article-summary">${featuredArticle.summary}</div>
            <div class="article-meta">
              <div class="article-date">${formatDate(featuredArticle.published_at)}</div>
              <div class="article-tags">
                ${featuredArticle.tags.map(tag => `<span class="article-tag">${tag}</span>`).join('')}
              </div>
            </div>
          </div>
        </div>
      `;
      articlesContainer.innerHTML += featuredArticleHTML;
      
      // 添加其他文章
      for (let i = 1; i < articles.length; i++) {
        const article = articles[i];
        try {
          const articleHTML = `
            <div class="article-card" onclick="location.href='article.html?id=${article.id}'">
              <div class="article-image">
                <img src="${article.thumbnail}" alt="${article.title}" onerror="this.src='/images/placeholder.jpg'; this.onerror=null;">
              </div>
              <div class="article-content">
                <span class="article-category ${article.category}">${getCategoryName(article.category)}</span>
                <h2 class="article-title">${article.title}</h2>
                <div class="article-summary">${article.summary}</div>
                <div class="article-meta">
                  <div class="article-date">${formatDate(article.published_at)}</div>
                  <div class="article-tags">
                    ${article.tags.map(tag => `<span class="article-tag">${tag}</span>`).join('')}
                  </div>
                </div>
              </div>
            </div>
          `;
          articlesContainer.innerHTML += articleHTML;
        } catch (articleError) {
          console.error(`渲染文章ID ${article.id || i} 时出错:`, articleError);
          // 继续处理下一篇文章，不中断整个循环
        }
      }
    })
    .catch(error => {
      console.error('加载文章列表失败:', error);
      articlesContainer.innerHTML = `
        <div class="error-message">
          <h3>加载文章失败</h3>
          <p>${error.message}</p>
          <button onclick="location.reload()">重试</button>
        </div>
      `;
    });
} catch (error) {
  console.error('文章列表初始化错误:', error);
  document.querySelector('.article-grid').innerHTML = `
    <div class="error-message">
      <h3>系统错误</h3>
      <p>加载文章列表时发生错误。请刷新页面重试。</p>
      <button onclick="location.reload()">刷新页面</button>
    </div>
  `;
}

// 分类筛选功能
document.querySelectorAll('.filter-button').forEach(button => {
  button.addEventListener('click', function() {
    // 移除所有按钮的active类
    document.querySelectorAll('.filter-button').forEach(btn => btn.classList.remove('active'));
    // 添加active类到点击的按钮
    this.classList.add('active');
    
    const category = this.textContent === '全部' ? '' : getCategoryValue(this.textContent);
    loadArticles(category);
  });
});
```

**文章详情页实现：**

```javascript
// 获取文章ID
try {
  const articleContainer = document.querySelector('.article-detail-content');
  articleContainer.innerHTML = '<div class="loading-indicator">正在加载文章内容...</div>';
  
  const urlParams = new URLSearchParams(window.location.search);
  const articleId = urlParams.get('id');
  
  if (!articleId) {
    throw new Error('文章ID不能为空');
  }

  // 加载文章详情
  fetch('/data/articles/articles.json')
    .then(response => {
      if (!response.ok) {
        throw new Error(`网络响应异常: ${response.status} ${response.statusText}`);
      }
      return response.json();
    })
    .then(data => {
      if (!data || !data.articles || !Array.isArray(data.articles)) {
        throw new Error('文章数据格式不正确');
      }
      
      const article = data.articles.find(a => a.id === articleId);
      if (!article) {
        throw new Error(`未找到ID为 ${articleId} 的文章`);
      }
      
      try {
        // 设置页面标题和元数据
        document.title = article.meta?.seo_title || article.title || '文章详情';
        
        if (article.meta) {
          if (article.meta.seo_description) {
            document.querySelector('meta[name="description"]').setAttribute('content', article.meta.seo_description);
          }
          if (article.meta.seo_keywords) {
            document.querySelector('meta[name="keywords"]').setAttribute('content', article.meta.seo_keywords);
          }
        }
      } catch (metaError) {
        console.error('设置元数据时出错:', metaError);
        // 继续执行，不中断整个过程
      }
      
      try {
        // 填充文章内容
        document.querySelector('.article-detail-title').textContent = article.title;
        
        const categoryElement = document.querySelector('.article-category');
        categoryElement.textContent = getCategoryName(article.category);
        categoryElement.classList.add(article.category);
        
        document.querySelector('.article-detail-meta div:first-child').textContent = `发布日期：${formatDate(article.published_at)}`;
        document.querySelector('.article-detail-meta div:last-child').textContent = `作者：${article.author || '匿名'}`;
      } catch (contentError) {
        console.error('填充文章头部内容时出错:', contentError);
        // 继续执行，不中断整个过程
      }
      
      try {
        // 检查marked是否已加载
        if (typeof marked === 'undefined') {
          throw new Error('Markdown解析器未加载');
        }
        
        // 使用marked.js将Markdown转换为HTML
        articleContainer.innerHTML = marked.parse(article.content);
      } catch (parseError) {
        console.error('Markdown解析错误:', parseError);
        // 如果markdown解析失败，直接显示原始内容
        articleContainer.innerHTML = `<pre>${article.content}</pre>`;
      }
      
      // 加载相关产品
      if (article.related_products && Array.isArray(article.related_products)) {
        loadRelatedProducts(article.related_products);
      } else {
        console.warn('没有相关产品数据或数据格式不正确');
        document.querySelector('.related-products').style.display = 'none';
      }
    })
    .catch(error => {
      console.error('加载文章详情失败:', error);
      articleContainer.innerHTML = `
        <div class="error-message">
          <h3>加载文章失败</h3>
          <p>${error.message}</p>
          <p><a href="news.html">返回文章列表</a></p>
          <button onclick="location.reload()">重试</button>
        </div>
      `;
    });
} catch (error) {
  console.error('文章详情页初始化错误:', error);
  document.querySelector('.article-detail-content').innerHTML = `
    <div class="error-message">
      <h3>系统错误</h3>
      <p>加载文章时发生错误。请刷新页面重试。</p>
      <p><a href="news.html">返回文章列表</a></p>
    </div>
  `;
}

// 加载相关产品
function loadRelatedProducts(productIds) {
  try {
    if (!productIds || !Array.isArray(productIds) || productIds.length === 0) {
      console.warn('没有相关产品数据');
      document.querySelector('.related-products').style.display = 'none';
      return;
    }
    
    const productsContainer = document.querySelector('.related-products-grid');
    if (!productsContainer) {
      console.error('相关产品容器不存在');
      return;
    }
    
    productsContainer.innerHTML = '<div class="loading-indicator">正在加载相关产品...</div>';
    
    // 加载产品数据
    Promise.all([
      fetch('/data/products/iphones.json')
        .then(res => {
          if (!res.ok) throw new Error(`加载iPhone数据失败: ${res.status}`);
          return res.json();
        })
        .catch(() => ({ products: [] })),
      fetch('/data/products/ipads.json')
        .then(res => {
          if (!res.ok) throw new Error(`加载iPad数据失败: ${res.status}`);
          return res.json();
        })
        .catch(() => ({ products: [] })),
      fetch('/data/products/watches.json')
        .then(res => {
          if (!res.ok) throw new Error(`加载Apple Watch数据失败: ${res.status}`);
          return res.json();
        })
        .catch(() => ({ products: [] })),
      fetch('/data/products/macs.json')
        .then(res => {
          if (!res.ok) throw new Error(`加载Mac数据失败: ${res.status}`);
          return res.json();
        })
        .catch(() => ({ products: [] }))
    ])
    .then(([iphones, ipads, watches, macs]) => {
      // 合并所有产品
      const allProducts = [
        ...(iphones?.products || []),
        ...(ipads?.products || []),
        ...(watches?.products || []),
        ...(macs?.products || [])
      ];
      
      if (allProducts.length === 0) {
        throw new Error('没有找到产品数据');
      }
      
      // 过滤相关产品
      const relatedProducts = allProducts.filter(product => productIds.includes(product.id));
      
      if (relatedProducts.length === 0) {
        productsContainer.innerHTML = '<p>暂无相关产品信息</p>';
        return;
      }
      
      // 清空容器
      productsContainer.innerHTML = '';
      
      // 渲染相关产品
      relatedProducts.forEach(product => {
        try {
          // 确保产品数据完整
          if (!product || !product.id || !product.name) {
            console.warn('产品数据不完整:', product);
            return; // 跳过这个产品
          }
          
          const productImage = product.images && product.images.length > 0 ? 
            product.images[0] : 
            '/images/product-placeholder.jpg';
          
          const productHTML = `
            <div class="related-product-card" onclick="location.href='compare.html?product=${product.id}'">
              <div class="related-product-image">
                <img src="${productImage}" alt="${product.name}" onerror="this.src='/images/product-placeholder.jpg'; this.onerror=null;">
              </div>
              <div class="related-product-name">${product.name}</div>
            </div>
          `;
          productsContainer.innerHTML += productHTML;
        } catch (productError) {
          console.error(`渲染产品ID ${product?.id || '未知'} 时出错:`, productError);
          // 继续处理下一个产品，不中断整个循环
        }
      });
    })
    .catch(error => {
      console.error('加载相关产品失败:', error);
      productsContainer.innerHTML = `<p>加载相关产品失败: ${error.message}</p>`;
    });
  } catch (error) {
    console.error('相关产品加载函数错误:', error);
    try {
      document.querySelector('.related-products-grid').innerHTML = '<p>加载相关产品时发生错误</p>';
    } catch (e) {
      // 如果连错误信息也无法显示，则静默失败
    }
  }
}
}
```

#### 6.1.5 部署方案架构

**MVP阶段部署架构：**

- **静态网站托管**：Netlify、Vercel或GitHub Pages
- **版本控制**：Git管理所有代码和数据文件
- **CI/CD**：GitHub Actions（自动构建和部署）
- **CDN**：使用托管平台自带的CDN

**部署流程：**

1. 开发人员或内容维护人员提交更改到Git仓库
2. GitHub Actions自动触发构建流程
3. 构建过程中完成文件重命名、链接替换等处理
4. 部署到静态网站托管平台
5. CDN自动缓存并分发静态资源

#### 6.1.6 后期扩展计划

当网站流量增长且数据更新频率提高时，可以考虑升级为传统的前后端架构：

1. **开发轻量级管理后台**
   - 基于React或Vue的前端管理界面
   - 用户认证与权限管理
   
2. **数据存储升级**
   - 将数据迁移到MongoDB等数据库
   - 实现数据版本控制和历史记录
   
3. **API层开发**
   - 实现Node.js或Python的API接口
   - 构建统一的数据访问层
   - 支持更复杂的数据查询和过滤
   
4. **性能优化**
   - 实现服务器端数据缓存
   - 优化大数据量下的查询性能
   - 实现数据分析和统计功能

## 7. 开发计划

### 7.1 MVP阶段（2个月）

| 周次 | 任务 | 负责团队 | 交付物 |
|------|------|---------|--------|
| 1-2周 | 需求细化与设计 | 产品+设计 | 详细UI设计稿、数据库结构 |
| 3-4周 | 基础架构开发 | 前端+后端 | 项目框架、数据库连接 |
| 5-6周 | 核心功能开发 | 前端+后端 | 产品列表、详情页、基础对比功能 |
| 7-8周 | 完善与测试 | 全团队 | MVP版本发布 |

### 7.2 MVP功能范围

- 基础产品数据库（最近3年的iPhone和iPad产品）
- 核心UI功能：首页、产品列表、产品详情、简单对比
- 响应式设计（PC和移动端基础适配）
- 简单的管理员后台

## 8. 验收标准

### 8.1 功能验收标准

1. **产品数据展示**
   - 能够正确显示所有产品的详细参数
   - 参数分类清晰，易于查找

2. **产品对比功能**
   - 能够同时对比2-4款产品
   - 参数差异明显高亮
   - 性能数据可视化正确

3. **响应式设计**
   - PC端和移动端均能正常访问和使用
   - 界面元素适应不同屏幕尺寸

4. **管理员功能**
   - 能够添加、编辑和删除产品数据
   - 能够处理用户反馈

### 8.2 性能验收标准

- 页面加载时间符合性能需求
- 对比功能响应时间符合要求
- 移动端流量消耗在预期范围内

## 9. 附录

### 9.1 数据源文件

- iPhone数据表.xlsx - 位于项目根目录，包含所有iPhone型号的详细参数

### 9.2 术语表

| 术语 | 定义 |
|------|------|
| GPU性能 | 图形处理单元性能评分，数值范围从iPhone 6s的2848到iPhone 16 Pro系列的32746不等 |
| PPI | 每英寸像素数(Pixels Per Inch)，表示屏幕清晰度 |
| 尼特 | 亮度单位，1尼特=1坎德拉/平方米 |

### 9.3 修订历史

| 版本 | 日期 | 修订内容 | 作者 |
|------|------|---------|------|
| v1.0 | 2025-05-25 | 初始版本 | 产品团队 |
