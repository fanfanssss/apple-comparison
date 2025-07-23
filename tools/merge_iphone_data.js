/**
 * 数据合并脚本
 * 将iphone.json中的数据合并到iphone_refined.json中，实现数据文件统一
 */

const fs = require('fs');
const path = require('path');

// 文件路径
const originalDataPath = path.join(__dirname, '../public/data/iphone.json');
const refinedDataPath = path.join(__dirname, '../public/data/iphone_refined.json');
const backupPath = path.join(__dirname, `../public/data/iphone_refined.json.bak.${Date.now()}`);

// 检查文件是否存在
if (!fs.existsSync(originalDataPath)) {
    console.error('错误: iphone.json 文件不存在');
    process.exit(1);
}

// 读取原始数据
console.log('读取 iphone.json 数据...');
const originalData = JSON.parse(fs.readFileSync(originalDataPath, 'utf8'));
console.log(`成功读取 ${originalData.length} 个iPhone型号数据`);

// 读取优化后的数据（如果存在）
let refinedData = [];
if (fs.existsSync(refinedDataPath)) {
    console.log('读取 iphone_refined.json 数据...');
    refinedData = JSON.parse(fs.readFileSync(refinedDataPath, 'utf8'));
    console.log(`成功读取 ${refinedData.length} 个优化后的iPhone型号数据`);
    
    // 创建备份
    fs.writeFileSync(backupPath, JSON.stringify(refinedData, null, 2), 'utf8');
    console.log(`已创建备份: ${backupPath}`);
}

// 合并数据
console.log('开始合并数据...');
const mergedData = [];
const refinedDataMap = new Map();

// 创建优化数据的映射表
refinedData.forEach(item => {
    refinedDataMap.set(item.id, item);
});

// 处理原始数据，合并或添加到结果中
originalData.forEach(originalItem => {
    const id = originalItem.id;
    const refinedItem = refinedDataMap.get(id);
    
    if (refinedItem) {
        // 合并数据，优先使用refined中的字段，但保留original中有而refined中没有的字段
        const mergedItem = { ...originalItem, ...refinedItem };
        mergedData.push(mergedItem);
        console.log(`合并型号: ${id}`);
    } else {
        // 如果refined中没有，直接添加original数据
        mergedData.push(originalItem);
        console.log(`添加新型号: ${id}`);
    }
    
    // 从映射表中移除已处理的项
    refinedDataMap.delete(id);
});

// 添加在refined中有但original中没有的数据
refinedDataMap.forEach((item, id) => {
    mergedData.push(item);
    console.log(`保留额外型号: ${id}`);
});

// 保存合并后的数据
fs.writeFileSync(refinedDataPath, JSON.stringify(mergedData, null, 2), 'utf8');
console.log(`数据合并完成! 已保存 ${mergedData.length} 个iPhone型号数据到 iphone_refined.json`);

// 添加一个提示，建议用户确认数据后可以删除iphone.json
console.log('\n提示: 数据合并完成后，请验证 iphone_refined.json 中的数据是否正确。');
console.log('如果确认无误，可以安全删除 iphone.json 文件，今后只维护 iphone_refined.json 文件。');
