const fs = require('fs');
const path = require('path');

// 读取iPhone JSON数据
const jsonPath = path.join(__dirname, 'public/data/iphone_refined.json');
const iphones = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// 定义正确的CPU和GPU性能数据（从跑分数据表中提取）
const performanceData = {
  'iphone-16-pro-max': { singleCore: '3437', multiCore: '8504', gpuPerformance: 32730 },
  'iphone-16-pro': { singleCore: '3452', multiCore: '8570', gpuPerformance: 32746 },
  'iphone-16-plus': { singleCore: '3321', multiCore: '8180', gpuPerformance: 27717 },
  'iphone-16': { singleCore: '3324', multiCore: '8189', gpuPerformance: 27695 },
  'iphone-15-pro-max': { singleCore: '2883', multiCore: '7145', gpuPerformance: 27228 },
  'iphone-15-pro': { singleCore: '2893', multiCore: '7181', gpuPerformance: 27295 },
  'iphone-15-plus': { singleCore: '2547', multiCore: '6346', gpuPerformance: 22857 },
  'iphone-15': { singleCore: '2543', multiCore: '6324', gpuPerformance: 22813 },
  'iphone-14-pro-max': { singleCore: '2598', multiCore: '6664', gpuPerformance: 22652 },
  'iphone-14-pro': { singleCore: '2604', multiCore: '6692', gpuPerformance: 22746 },
  'iphone-14-plus': { singleCore: '2257', multiCore: '5541', gpuPerformance: 20530 },
  'iphone-14': { singleCore: '2255', multiCore: '5530', gpuPerformance: 20486 },
  'iphone-13-pro-max': { singleCore: '2340', multiCore: '5739', gpuPerformance: 20001 },
  'iphone-13-pro': { singleCore: '2339', multiCore: '5724', gpuPerformance: 20219 }
};

// 更新iPhone数据
let updatedCount = 0;
iphones.forEach(phone => {
  if (performanceData[phone.id]) {
    const data = performanceData[phone.id];
    
    // 更新CPU性能数据
    if (phone.cpuPerformance) {
      phone.cpuPerformance.singleCore = data.singleCore;
      phone.cpuPerformance.multiCore = data.multiCore;
    }
    
    // 更新GPU性能数据
    if (phone.gpuPerformance !== data.gpuPerformance) {
      phone.gpuPerformance = data.gpuPerformance;
      updatedCount++;
    }
  }
});

// 保存更新后的数据
fs.writeFileSync(jsonPath, JSON.stringify(iphones, null, 2), 'utf8');
console.log(`已更新 ${updatedCount} 个iPhone型号的性能数据`);
