/**
 * iPhone数据维护脚本
 * 直接维护和更新iPhone的所有参数数据
 */

const fs = require('fs');
const path = require('path');

// 读取当前数据
let iphones = [];
const dataPath = path.join(__dirname, '../public/data/iphone_refined.json');

// 如果文件存在，读取现有数据，否则创建新数组
if (fs.existsSync(dataPath)) {
    const rawData = fs.readFileSync(dataPath, 'utf8');
    iphones = JSON.parse(rawData);
    console.log(`读取到${iphones.length}个iPhone型号数据`);
}

// 处理每个iPhone对象，拆分复合参数
const refinedIphones = iphones.map(iphone => {
    // 创建新的iPhone对象，保留原有的所有属性
    const refinedIphone = { ...iphone };
    
    // 1. 屏幕参数细分
    
    // 提取像素密度(PPI)
    if (iphone.displayResolution) {
        const ppiMatch = iphone.displayResolution.match(/(\d+)\s*ppi/i);
        if (ppiMatch) {
            refinedIphone.displayPpi = parseInt(ppiMatch[1]);
        }
    }
    
    // 提取面板类型
    if (iphone.displayTechnology) {
        if (iphone.displayTechnology.toLowerCase().includes('oled')) {
            refinedIphone.displayPanelType = 'OLED';
        } else if (iphone.displayTechnology.toLowerCase().includes('lcd')) {
            refinedIphone.displayPanelType = 'LCD';
        } else if (iphone.displayTechnology.toLowerCase().includes('retina')) {
            refinedIphone.displayPanelType = 'Retina LCD';
        }
    }
    
    // 提取特殊显示技术
    if (iphone.displayTechnology) {
        const specialTech = [];
        if (iphone.displayTechnology.includes('Super Retina XDR')) {
            specialTech.push('Super Retina XDR');
        } else if (iphone.displayTechnology.includes('Super Retina')) {
            specialTech.push('Super Retina');
        } else if (iphone.displayTechnology.includes('Retina')) {
            specialTech.push('Retina');
        }
        
        if (iphone.displayTechnology.includes('ProMotion')) {
            specialTech.push('ProMotion');
        }
        
        if (specialTech.length > 0) {
            refinedIphone.displaySpecialTech = specialTech.join(', ');
        }
    }
    
    // 提取屏幕亮度细分
    if (iphone.displayBrightness) {
        // 标准亮度
        const standardMatch = iphone.displayBrightness.match(/(\d+)\s*尼特/);
        if (standardMatch) {
            refinedIphone.displayStandardBrightness = `${standardMatch[1]}尼特`;
        }
        
        // HDR亮度
        const hdrMatch = iphone.displayBrightness.match(/HDR.*?(\d+)\s*尼特/);
        if (hdrMatch) {
            refinedIphone.displayHdrBrightness = `${hdrMatch[1]}尼特`;
        }
        
        // 户外亮度
        const outdoorMatch = iphone.displayBrightness.match(/峰值.*?(\d+)\s*尼特/);
        if (outdoorMatch) {
            refinedIphone.displayOutdoorBrightness = `${outdoorMatch[1]}尼特`;
        }
    }
    
    // 触控技术
    if (iphone.displayTechnology) {
        if (iphone.displayTechnology.includes('3D Touch')) {
            refinedIphone.touchTechnology = '3D Touch';
        } else if (iphone.model && parseInt(iphone.model.match(/iPhone(\d+)/)?.[1] || 0) >= 11) {
            refinedIphone.touchTechnology = 'Haptic Touch';
        }
    }
    
    // 显示色域
    if (iphone.displayTechnology && iphone.displayTechnology.includes('P3')) {
        refinedIphone.displayColorGamut = 'P3广色域';
    }
    
    // 2. 摄像头系统细分
    
    // 主摄像头
    if (iphone.camera) {
        const mainCameraMatch = iphone.camera.match(/(\d+)(?:\.\d+)?\s*万像素主摄.*?f\/(\d+\.\d+)/);
        if (mainCameraMatch) {
            refinedIphone.mainCamera = `${mainCameraMatch[1]}万像素，f/${mainCameraMatch[2]}光圈`;
        }
        
        // 超广角摄像头
        const ultraWideMatch = iphone.camera.match(/(\d+)(?:\.\d+)?\s*万像素超广角.*?f\/(\d+\.\d+)/);
        if (ultraWideMatch) {
            refinedIphone.ultraWideCamera = `${ultraWideMatch[1]}万像素，f/${ultraWideMatch[2]}光圈`;
        }
        
        // 长焦摄像头
        const telephotoMatch = iphone.camera.match(/(\d+)(?:\.\d+)?\s*万像素长焦.*?f\/(\d+\.\d+)/);
        if (telephotoMatch) {
            refinedIphone.telephotoCamera = `${telephotoMatch[1]}万像素，f/${telephotoMatch[2]}光圈`;
            
            // 光学变焦
            const zoomMatch = iphone.camera.match(/(\d+(?:\.\d+)?)倍光学变焦/);
            if (zoomMatch) {
                refinedIphone.opticalZoom = `${zoomMatch[1]}倍`;
            }
        }
        
        // 摄像头特殊功能
        const specialFeatures = [];
        if (iphone.camera.includes('夜间模式')) specialFeatures.push('夜间模式');
        if (iphone.camera.includes('电影模式')) specialFeatures.push('电影模式');
        if (iphone.camera.includes('微距')) specialFeatures.push('微距摄影');
        if (iphone.camera.includes('ProRAW')) specialFeatures.push('ProRAW');
        if (iphone.camera.includes('光学防抖')) specialFeatures.push('光学防抖');
        
        if (specialFeatures.length > 0) {
            refinedIphone.cameraSpecialFeatures = specialFeatures.join(', ');
        }
    }
    
    // 3. 处理器和性能细分
    
    // CPU架构
    if (iphone.processor) {
        const cpuMatch = iphone.processor.match(/\((\d+P\+\d+E)/);
        if (cpuMatch) {
            refinedIphone.cpuArchitecture = cpuMatch[1].replace('P', '性能核心+').replace('E', '能效核心');
        }
    }
    
    // 制程工艺
    if (iphone.processorDetails) {
        const processMatch = iphone.processorDetails?.match(/(台积电.*?纳米)/);
        if (processMatch) {
            refinedIphone.processTechnology = processMatch[1];
        }
    }
    
    // 神经网络引擎
    if (iphone.processorDetails) {
        const neuralMatch = iphone.processorDetails?.match(/(\d+)\s*核.*?神经网络/);
        if (neuralMatch) {
            refinedIphone.neuralEngine = `${neuralMatch[1]}核神经网络引擎`;
        }
    }
    
    // 4. 电池和充电细分
    
    // 电池容量(mAh)
    if (iphone.battery) {
        const mAhMatch = iphone.battery.match(/(\d+)mAh/);
        if (mAhMatch) {
            refinedIphone.batteryCapacityMah = `${mAhMatch[1]}mAh`;
        }
        
        // 电池容量(Wh)
        const whMatch = iphone.battery.match(/(\d+\.\d+)Wh/);
        if (whMatch) {
            refinedIphone.batteryCapacityWh = `${whMatch[1]}Wh`;
        }
    }
    
    // 电池续航时间细分
    if (iphone.batteryLife) {
        // 视频播放时间
        const videoMatch = iphone.batteryLife.match(/视频.*?(\d+)(?:\.\d+)?\s*小时/);
        if (videoMatch) {
            refinedIphone.videoPlaybackTime = `最长${videoMatch[1]}小时`;
        }
        
        // 音频播放时间
        const audioMatch = iphone.batteryLife.match(/音频.*?(\d+)(?:\.\d+)?\s*小时/);
        if (audioMatch) {
            refinedIphone.audioPlaybackTime = `最长${audioMatch[1]}小时`;
        }
        
        // 通话时间
        const talkMatch = iphone.batteryLife.match(/通话.*?(\d+)(?:\.\d+)?\s*小时/);
        if (talkMatch) {
            refinedIphone.talkTime = `最长${talkMatch[1]}小时`;
        }
    }
    
    // 充电技术细分
    if (iphone.charging) {
        // 有线充电速度
        const wiredMatch = iphone.charging.match(/(\d+W|快充)/);
        if (wiredMatch) {
            refinedIphone.wiredChargingSpeed = wiredMatch[0];
        }
        
        // 无线充电速度
        const wirelessMatch = iphone.charging.match(/(MagSafe|Qi|无线充电)/);
        if (wirelessMatch) {
            refinedIphone.wirelessChargingSpeed = wirelessMatch[0];
        }
    }
    
    // 5. 连接和接口细分
    
    // Wi-Fi标准
    if (iphone.wireless) {
        const wifiMatch = iphone.wireless?.match(/(Wi-Fi\s*\d+|802\.11[a-z]+)/);
        if (wifiMatch) {
            refinedIphone.wifiStandard = wifiMatch[1];
        }
        
        // 蓝牙版本
        const bluetoothMatch = iphone.wireless?.match(/(蓝牙\s*\d+\.\d+)/);
        if (bluetoothMatch) {
            refinedIphone.bluetoothVersion = bluetoothMatch[1];
        }
    }
    
    // 蜂窝网络细分
    if (iphone.cellularFeatures) {
        // SIM卡
        if (iphone.cellularFeatures.includes('双卡') && iphone.cellularFeatures.includes('eSIM')) {
            refinedIphone.simCardSupport = '物理SIM+eSIM';
        } else if (iphone.cellularFeatures.includes('双卡')) {
            refinedIphone.simCardSupport = '双物理SIM';
        } else if (iphone.cellularFeatures.includes('eSIM')) {
            refinedIphone.simCardSupport = 'eSIM';
        } else {
            refinedIphone.simCardSupport = '单物理SIM';
        }
        
        // 蜂窝数据
        const cellularTypes = [];
        if (iphone.cellularFeatures.includes('5G')) cellularTypes.push('5G');
        if (iphone.cellularFeatures.includes('4G') || iphone.cellularFeatures.includes('LTE')) cellularTypes.push('4G LTE');
        if (cellularTypes.length > 0) {
            refinedIphone.cellularData = cellularTypes.join(', ');
        }
    }
    
    // 6. 音频系统
    
    // 扬声器数量
    if (iphone.wireless && iphone.wireless.includes('立体声扬声器')) {
        refinedIphone.speakers = '立体声扬声器';
    } else {
        refinedIphone.speakers = '单扬声器';
    }
    
    // 麦克风数量
    if (iphone.wireless && iphone.wireless.includes('麦克风')) {
        const micMatch = iphone.wireless.match(/(\d+)\s*个麦克风/);
        if (micMatch) {
            refinedIphone.microphones = `${micMatch[1]}个麦克风`;
        } else {
            refinedIphone.microphones = '多个麦克风';
        }
    }
    
    // 7. 软件和系统
    
    // 初始系统版本
    refinedIphone.initialOS = iphone.os || '';
    
    // 最高支持系统版本
    // 这个需要额外数据，暂时留空或根据发布日期推测
    const releaseYear = parseInt(iphone.releaseDate?.match(/(\d{4})年/)?.[1] || '0');
    if (releaseYear > 0) {
        const currentYear = new Date().getFullYear();
        const supportYears = Math.min(currentYear - releaseYear + 3, 7); // 假设支持5-7年
        refinedIphone.maxSupportedOS = `iOS ${Math.min(18, 12 + (currentYear - releaseYear))}+`;
    }
    
    // 特色软件功能
    const specialSoftwareFeatures = [];
    if (releaseYear >= 2023) specialSoftwareFeatures.push('Apple Intelligence');
    if (iphone.name.includes('Pro') && releaseYear >= 2021) specialSoftwareFeatures.push('ProRes视频');
    if (releaseYear >= 2020) specialSoftwareFeatures.push('实况照片');
    if (releaseYear >= 2022) specialSoftwareFeatures.push('紧急SOS');
    
    if (specialSoftwareFeatures.length > 0) {
        refinedIphone.specialSoftwareFeatures = specialSoftwareFeatures.join(', ');
    }
    
    return refinedIphone;
});

// 写入更新后的数据
fs.writeFileSync(
    dataPath, 
    JSON.stringify(refinedIphones, null, 2),
    'utf8'
);

console.log('数据更新完成！已保存到 public/data/iphone_refined.json');
