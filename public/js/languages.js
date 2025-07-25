/**
 * 多语言资源文件
 * 包含网站所有页面的中英文翻译文本
 */

const languageResources = {
  'zh-CN': {
    // 页面标题
    'page.title': 'Apple参数大全 - 苹果产品参数对比平台',
    
    // Apple Watch参数
    'param.marketingSlogan': '宣传口号',
    'param.releaseDate': '发布日期',
    'param.os': '系统支持',
    'param.model': '型号',
    'param.colors': '颜色',
    'param.processor': '处理器',
    'param.wirelessChip': '无线芯片',
    'param.ultraWidebandChip': '超宽带芯片',
    'param.displayResolution': '屏幕分辨率',
    'param.displayTechnology': '屏幕技术',
    'param.displayBrightness': '屏幕亮度',
    'param.displayGlass': '屏幕玻璃',
    'param.backMaterial': '后盖材质',
    'param.baseband': '基带芯片',
    'param.wifiStandard': 'Wi-Fi标准',
    'param.bluetoothVersion': '蓝牙版本',
    'param.batteryCapacity': '电池容量',
    'param.batteryLife': '电池续航',
    'param.waterResistance': '防水等级',
    'param.accelerometer': '加速度计',
    'param.gyroscope': '陀螺仪',
    'param.ambientLightSensor': '环境光传感器',
    'param.heartRateSensor': '心率传感器',
    'param.ecgSensor': '心电图传感器',
    'param.barometer': '气压高度计',
    'param.compass': '磁力计',
    'param.bloodOxygenSensor': '血氧传感器',
    'param.temperatureSensor': '体温传感器',
    'param.waterTemperatureSensor': '水温传感器',
    'param.depthGauge': '深度计',
    'param.technicalSpecsLink': '技术规格链接',
    'compare.paramHeader': '参数 / 产品',
    'compare.performanceCharts': '性能图表',
    'chart.title': '性能对比图表',
    'chart.cpuSingle.title': 'CPU单核性能对比',
    'chart.cpuMulti.title': 'CPU多核性能对比',
    'chart.gpu.title': 'GPU性能对比',
    'chart.cpuSingle': 'CPU单核性能',
    'chart.cpuMulti': 'CPU多核性能',
    'chart.gpu': 'GPU性能',
    'chart.axis.score': '性能得分',
    
    // 导航
    'nav.home': '首页',
    'nav.feedback': '提出建议',
    'site.name': 'Apple参数大全',
    
    // 首页
    'hero.title': 'Apple参数大全',
    'hero.subtitle': '全面的苹果产品参数对比',
    'product.iphone.title': 'iPhone',
    'product.iphone.description': '比较不同iPhone型号的性能、相机、屏幕和电池规格，包括GPU性能、电池容量和处理器架构等详细参数',
    'product.ipad.title': 'iPad',
    'product.ipad.description': '对比iPad、iPad Air、iPad Pro和iPad mini的功能与规格，了解不同机型的屏幕分辨率、处理器和存储选项',
    'product.watch.title': 'Apple Watch',
    'product.watch.description': '比较不同Apple Watch系列的健康功能、屏幕尺寸和电池续航，了解各系列的传感器和监测能力',
    'product.mac.title': 'Mac',
    'product.mac.description': '对比MacBook Air、MacBook Pro、iMac和Mac mini的性能与特性，了解各机型的处理器、内存和图形性能',
    'compare.button': '查看对比',
    
    // 对比页
    'compare.select': '选择',
    'compare.reset': '重置',
    'compare.title.iphone': 'iPhone 产品参数对比',
    'compare.title.ipad': 'iPad 产品参数对比',
    'compare.title.watch': 'Apple Watch 产品参数对比',
    'compare.view': '查看对比',
    'compare.showAll': '显示所有参数',
    'compare.hideEmpty': '隐藏空参数',
    'compare.showDiff': '仅显示差异',
    'compare.basicInfo': '基本信息',
    'compare.dimensions': '尺寸与重量',
    'compare.display': '显示屏',
    'compare.performance': '性能',
    
    // 反馈页
    'feedback.title': '用户反馈',
    'feedback.welcome': '欢迎提供您的宝贵意见和建议！您可以在下方自由填写反馈内容，包括网站功能改进、数据错误报告、新产品建议等任何内容。',
    'feedback.content.label': '反馈内容',
    'feedback.content.placeholder': '请在此输入您的反馈内容，如果需要我们回复，请留下您的联系方式...',
    'feedback.submit': '提交反馈',
    'feedback.contact.title': '站长联系方式',
    'feedback.contact.email': '邮箱：',
    'feedback.contact.group': 'QQ群：',
    'feedback.contact.groupValue': '1046732889',
    'feedback.contact.note': '如果您发现数据错误或建议，请通过以上联系方式与我联系，感谢！',
    
    // 页脚
    'footer.about.title': '关于我们',
    'footer.about.who': '我们是谁',
    'footer.about.mission': '我们的使命',
    'footer.about.contact': '联系我们',
    'footer.legal.title': '法律信息',
    'footer.legal.terms': '使用条款',
    'footer.legal.privacy': '隐私政策',
    'footer.legal.cookies': 'Cookie 政策',
    'footer.resources.title': '资源链接',
    'footer.resources.apple': 'Apple 官网',
    'footer.resources.support': 'Apple 支持',
    'footer.resources.developer': 'Apple 开发者',
    'footer.copyright': '© 2025 Apple参数大全',
    'footer.disclaimer': '本网站与Apple Inc.没有任何关联。Apple、iPhone、iPad、Mac、Apple Watch等是Apple Inc.的商标。',
    'footer.friendLinks': '友情链接',
    'footer.link1': 'Apple官网',
    'footer.link2': '苹果设备支持',
    'footer.link3': '苹果开发者', 
    'footer.icp': '浙ICP备XXXXXXXX号-X'
  },
  'en-US': {
    // Page Title
    'page.title': 'Apple Specs Library - Apple Product Specifications Platform',
    
    // Apple Watch Parameters
    'param.marketingSlogan': 'Marketing Slogan',
    'param.releaseDate': 'Release Date',
    'param.os': 'Operating System',
    'param.model': 'Model',
    'param.colors': 'Colors',
    'param.processor': 'Processor',
    'param.wirelessChip': 'Wireless Chip',
    'param.ultraWidebandChip': 'Ultra Wideband Chip',
    'param.displayResolution': 'Display Resolution',
    'param.displayTechnology': 'Display Technology',
    'param.displayBrightness': 'Display Brightness',
    'param.displayGlass': 'Display Glass',
    'param.backMaterial': 'Back Material',
    'param.baseband': 'Baseband Chip',
    'param.wifiStandard': 'Wi-Fi Standard',
    'param.bluetoothVersion': 'Bluetooth Version',
    'param.batteryCapacity': 'Battery Capacity',
    'param.batteryLife': 'Battery Life',
    'param.waterResistance': 'Water Resistance',
    'param.accelerometer': 'Accelerometer',
    'param.gyroscope': 'Gyroscope',
    'param.ambientLightSensor': 'Ambient Light Sensor',
    'param.heartRateSensor': 'Heart Rate Sensor',
    'param.ecgSensor': 'ECG Sensor',
    'param.barometer': 'Barometer',
    'param.compass': 'Compass',
    'param.bloodOxygenSensor': 'Blood Oxygen Sensor',
    'param.temperatureSensor': 'Temperature Sensor',
    'param.waterTemperatureSensor': 'Water Temperature Sensor',
    'param.depthGauge': 'Depth Gauge',
    'param.technicalSpecsLink': 'Technical Specifications',
    'compare.paramHeader': 'Parameter / Product',
    'compare.performanceCharts': 'Performance Charts',
    'chart.title': 'Performance Comparison Charts',
    'chart.cpuSingle.title': 'CPU Single-Core Performance Comparison',
    'chart.cpuMulti.title': 'CPU Multi-Core Performance Comparison',
    'chart.gpu.title': 'GPU Performance Comparison',
    'chart.cpuSingle': 'CPU Single-Core Performance',
    'chart.cpuMulti': 'CPU Multi-Core Performance',
    'chart.gpu': 'GPU Performance',
    'chart.axis.score': 'Performance Score',
    
    // Navigation
    'nav.home': 'Home',
    'nav.feedback': 'Suggestions',
    'site.name': 'Apple Specs Library',
    
    // Home Page
    'hero.title': 'Apple Specs Library',
    'hero.subtitle': 'Comprehensive Apple Product Comparison',
    'product.iphone.title': 'iPhone',
    'product.iphone.description': 'Compare performance, camera, display, and battery specifications of different iPhone models, including detailed parameters such as GPU performance, battery capacity, and processor architecture',
    'product.ipad.title': 'iPad',
    'product.ipad.description': 'Compare features and specifications of iPad, iPad Air, iPad Pro and iPad mini, and learn about screen resolution, processor and storage options for different models',
    'product.watch.title': 'Apple Watch',
    'product.watch.description': 'Compare health features, screen size and battery life of different Apple Watch series, and learn about the sensors and monitoring capabilities of each series',
    'product.mac.title': 'Mac',
    'product.mac.description': 'Compare performance and features of MacBook Air, MacBook Pro, iMac and Mac mini, and learn about processor, memory and graphics performance of each model',
    'compare.button': 'Compare',
    
    // Compare Page
    'compare.select': 'Select',
    'compare.reset': 'Reset',
    'compare.title.iphone': 'iPhone Product Specifications',
    'compare.title.ipad': 'iPad Product Specifications',
    'compare.title.watch': 'Apple Watch Product Specifications',
    'compare.view': 'Compare',
    'compare.showAll': 'Show All Parameters',
    'compare.hideEmpty': 'Hide Empty Parameters',
    'compare.showDiff': 'Show Differences Only',
    'compare.basicInfo': 'Basic Information',
    'compare.dimensions': 'Dimensions & Weight',
    'compare.display': 'Display',
    'compare.performance': 'Performance',
    
    // Feedback Page
    'feedback.title': 'Feedback',
    'feedback.welcome': 'Welcome to provide your valuable opinions and suggestions! You can freely fill in the feedback below, including website functionality improvements, data error reports, new product suggestions, etc.',
    'feedback.content.label': 'Feedback Content',
    'feedback.content.placeholder': 'Please enter your feedback here. If you need us to reply, please leave your contact information...',
    'feedback.submit': 'Submit Feedback',
    'feedback.contact.title': 'Contact Information',
    'feedback.contact.email': 'Email:',
    'feedback.contact.group': 'QQ Group:',
    'feedback.contact.groupValue': '1046732889',
    'feedback.contact.note': 'If you find any data errors or have suggestions, please contact me through the above methods. Thank you!',
    
    // Footer
    'footer.about.title': 'About Us',
    'footer.about.who': 'Who We Are',
    'footer.about.mission': 'Our Mission',
    'footer.about.contact': 'Contact Us',
    'footer.legal.title': 'Legal',
    'footer.legal.terms': 'Terms of Use',
    'footer.legal.privacy': 'Privacy Policy',
    'footer.legal.cookies': 'Cookie Policy',
    'footer.resources.title': 'Resources',
    'footer.resources.apple': 'Apple Website',
    'footer.resources.support': 'Apple Support',
    'footer.resources.developer': 'Apple Developer',
    'footer.copyright': '© 2025 Apple Specs Library. All rights reserved.',
    'footer.disclaimer': 'This website is not affiliated with Apple Inc. Apple, iPhone, iPad, Mac, Apple Watch are trademarks of Apple Inc.',
    'footer.friendLinks': 'Friend Links',
    'footer.link1': 'Apple Website',
    'footer.link2': 'Apple Support',
    'footer.link3': 'Apple Developer',
    'footer.icp': 'ICP License XXXXXXXX-X'
  }
};
