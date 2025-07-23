#!/usr/bin/env python3
import json
import re
import os

print("开始更新iPhone数据字段为双语格式...")

# 备份原始文件
source_file = 'public/data/iphone_refined.json'
backup_file = 'public/data/iphone_refined_backup.json'

# 如果备份文件不存在，创建一个
if not os.path.exists(backup_file):
    print(f"创建备份文件: {backup_file}")
    with open(source_file, 'r', encoding='utf-8') as f:
        original_data = f.read()
        
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(original_data)

# 读取JSON文件
print("读取iPhone数据文件...")
with open(source_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理计数器
updated_count = 0
fields_updated = {}

# 需要忽略的字段（不需要双语处理的字段）
ignore_fields = [
    "id", "model", "cpuPerformance", "benchmarks", "storage", "dimensions", "weight",
    "displayPpi", "cpuSingleCore", "cpuMultiCore", "gpuPerformance", "batteryCapacityMah",
    "batteryCapacityWh", "displayRefreshRate", "displayStandardBrightness", "displayHdrBrightness"
]

# 已经是双语格式的字段不需要重复处理
bilingual_fields = ["name", "speakers"]

# 英文翻译映射
translations = {
    # 基本信息
    "releaseDate": {
        r"(\d{4})年(\d{1,2})月": lambda m: f"{m.group(1)}-{m.group(2).zfill(2)}",
    },
    "colors": {
        "白色": "White", 
        "黑色": "Black", 
        "红色": "Red", 
        "黄色": "Yellow", 
        "蓝色": "Blue", 
        "紫色": "Purple",
        "绿色": "Green",
        "粉色": "Pink",
        "银色": "Silver",
        "金色": "Gold",
        "深空灰色": "Space Gray",
        "天蓝色": "Sky Blue",
        "石墨色": "Graphite",
        "暗夜绿色": "Midnight Green",
        "太平洋蓝": "Pacific Blue",
        "午夜色": "Midnight",
        "星光色": "Starlight",
        "海蓝色": "Sierra Blue",
        "远峰蓝": "Alpine Blue",
        "深紫色": "Deep Purple",
        "钛蓝色": "Blue Titanium",
        "钛金色": "Gold Titanium",
        "钛原色": "Natural Titanium",
        "钛黑色": "Black Titanium",
    },
    "frontPanel": {
        "超瓷晶面板": "Ceramic Shield front", 
        "超瓷晶面板二代": "Ceramic Shield front (2nd generation)",
        "钢化玻璃": "Hardened glass front", 
        "普通玻璃": "Glass front",
    },
    "frameMaterial": {
        "钛合金": "Titanium frame",
        "铝合金": "Aluminum frame",
        "不锈钢": "Stainless steel frame",
        "塑料": "Plastic frame",
    },
    "backPanelMaterial": {
        "钛合金": "Titanium back",
        "玻璃": "Glass back",
        "钢化玻璃": "Hardened glass back",
        "塑料": "Plastic back",
    },
    "waterResistance": {
        "IP68": "IP68 water and dust resistance",
        "IP67": "IP67 water and dust resistance",
        "无官方防水等级": "No official water resistance rating",
    },
    
    # 屏幕参数
    "displaySize": {
        r"(\d+\.?\d*)英寸": lambda m: f"{m.group(1)} inches",
    },
    "displayResolution": {
        r"(\d+) × (\d+)像素": lambda m: f"{m.group(1)} × {m.group(2)} pixels",
        r"(\d+)×(\d+)像素": lambda m: f"{m.group(1)} × {m.group(2)} pixels",
    },
    "displayPanelType": {
        "OLED": "OLED",
        "LCD": "LCD",
        "Super Retina XDR": "Super Retina XDR",
        "Liquid Retina": "Liquid Retina",
        "Liquid Retina XDR": "Liquid Retina XDR",
        "Retina HD": "Retina HD",
    },
    "displaySpecialTech": {
        "ProMotion": "ProMotion technology",
        "True Tone": "True Tone technology",
        "原彩显示": "True Tone display",
        "广色域": "Wide color display (P3)",
        "LTPO": "LTPO technology",
    },
    "touchTechnology": {
        "触控屏": "Touch screen",
        "Force Touch": "Force Touch",
        "3D Touch": "3D Touch",
        "触觉触控": "Haptic Touch",
        "多点触控": "Multi-touch display",
    },
    "displayColorGamut": {
        "P3色域": "P3 wide color gamut",
        "广色域": "Wide color gamut",
        "sRGB": "sRGB",
    },
    
    # 处理器和性能
    "processor": {
        r"A(\d+)": lambda m: f"Apple A{m.group(1)}",
        r"A(\d+) Bionic": lambda m: f"Apple A{m.group(1)} Bionic",
        r"A(\d+) Pro": lambda m: f"Apple A{m.group(1)} Pro",
    },
    "processTechnology": {
        r"(\d+)nm": lambda m: f"{m.group(1)}nm process",
        r"(\d+)纳米": lambda m: f"{m.group(1)}nm process",
    },
    "ram": {
        r"(\d+)GB": lambda m: f"{m.group(1)}GB",
        r"(\d+) GB": lambda m: f"{m.group(1)}GB",
    },
    
    # 相机
    "mainCamera": {
        r"(\d+)MP": lambda m: f"{m.group(1)}MP",
        "单摄像头": "Single camera",
        "双摄像头": "Dual camera",
        "三摄像头": "Triple camera",
        "四摄像头": "Quad camera",
    },
    "ultraWideCamera": {
        r"(\d+)MP": lambda m: f"{m.group(1)}MP",
        "超广角": "Ultra Wide",
    },
    "telephotoCamera": {
        r"(\d+)MP": lambda m: f"{m.group(1)}MP",
        "长焦": "Telephoto",
    },
    "opticalZoom": {
        r"(\d+)x": lambda m: f"{m.group(1)}x",
        "光学变焦": "Optical zoom",
    },
    "frontCamera": {
        r"(\d+)MP": lambda m: f"{m.group(1)}MP",
        "原深感": "TrueDepth",
        "FaceTime": "FaceTime",
    },
    
    # 电池和充电
    "videoPlaybackTime": {
        r"最长(\d+)小时": lambda m: f"Up to {m.group(1)} hours",
        r"(\d+)小时": lambda m: f"{m.group(1)} hours",
    },
    "audioPlaybackTime": {
        r"最长(\d+)小时": lambda m: f"Up to {m.group(1)} hours",
        r"(\d+)小时": lambda m: f"{m.group(1)} hours",
    },
    "wiredChargingSpeed": {
        r"(\d+)W": lambda m: f"{m.group(1)}W",
        "快充": "Fast charging",
    },
    "wirelessChargingSpeed": {
        r"(\d+)W": lambda m: f"{m.group(1)}W",
        "MagSafe": "MagSafe",
        "Qi": "Qi wireless charging",
    },
    
    # 连接和接口
    "wifiStandard": {
        "Wi-Fi 6": "Wi-Fi 6",
        "Wi-Fi 6E": "Wi-Fi 6E",
        "Wi-Fi 7": "Wi-Fi 7",
        "802.11": "802.11",
    },
    "bluetoothVersion": {
        r"蓝牙(\d+\.\d+)": lambda m: f"Bluetooth {m.group(1)}",
        r"Bluetooth (\d+\.\d+)": lambda m: f"Bluetooth {m.group(1)}",
        r"(\d+\.\d+)": lambda m: f"Bluetooth {m.group(1)}",
    },
    "ports": {
        "Lightning": "Lightning",
        "USB-C": "USB-C",
        "30针": "30-pin",
    },
    "simCardSupport": {
        "双物理SIM": "Dual SIM (nano-SIM and nano-SIM)",
        "单物理SIM": "Single SIM (nano-SIM)",
        "eSIM": "eSIM",
        "双卡(物理+eSIM)": "Dual SIM (nano-SIM and eSIM)",
    },
    "cellularData": {
        "5G": "5G",
        "4G": "4G LTE",
        "3G": "3G",
        "2G": "2G",
    },
    "baseband": {
        "高通": "Qualcomm",
        "英特尔": "Intel",
    },
    "satelliteFeatures": {
        "卫星连接": "Satellite connectivity",
        "紧急SOS": "Emergency SOS via satellite",
    },
    
    # 音频
    "speakers": {
        "立体声扬声器": "Stereo speakers",
        "立体声扬声器，杜比全景声支持": "Stereo speakers with Dolby Atmos",
        "立体声扬声器，支持空间音频": "Stereo speakers with spatial audio",
        "单声道扬声器": "Mono speaker",
        "2个扬声器": "Built-in stereo speakers",
    },
    "microphoneCount": {
        r"(\d+)个麦克风": lambda m: f"{m.group(1)} microphones",
        r"(\d+)麦克风": lambda m: f"{m.group(1)} microphones",
    },
    
    # 系统
    "initialOS": {
        r"iOS (\d+)": lambda m: f"iOS {m.group(1)}",
    },
    "maxSupportedOS": {
        r"iOS (\d+)": lambda m: f"iOS {m.group(1)}",
        "最新": "Latest",
    },
    "specialSoftwareFeatures": {
        "Apple Intelligence": "Apple Intelligence",
        "ProRes视频": "ProRes video",
        "实况照片": "Live Photos",
        "动态岛": "Dynamic Island",
    },
}

# 通用翻译函数
def translate_field(field_name, text):
    if not text or not isinstance(text, str):
        return None
        
    # 检查字段是否有专用翻译映射
    if field_name in translations:
        field_translations = translations[field_name]
        
        # 1. 首先尝试直接匹配
        if text in field_translations:
            return field_translations[text]
            
        # 2. 尝试正则表达式匹配
        for pattern, translator in field_translations.items():
            if callable(translator):  # 这是一个正则表达式处理函数
                match = re.search(pattern, text)
                if match:
                    return translator(match)
        
        # 3. 尝试部分匹配和组合翻译
        translated_parts = []
        original_text = text
        
        for zh_term, en_term in sorted(
            [(k, v) for k, v in field_translations.items() if not callable(v)],
            key=lambda x: len(x[0]), 
            reverse=True
        ):
            if zh_term in text:
                text = text.replace(zh_term, f"__MARK__{en_term}__MARK__")
                
        # 处理标记
        parts = text.split("__MARK__")
        result = ""
        for part in parts:
            result += part
        
        # 如果没有任何匹配，则返回原文
        if result == original_text:
            # 如果文本包含中文，返回一个通用的英文描述
            if re.search('[\u4e00-\u9fff]', text):
                return f"{field_name.capitalize()} information"
            return text
            
        return result
            
    # 如果没有专门的翻译逻辑，检查文本是否包含中文
    if re.search('[\u4e00-\u9fff]', text):
        return f"{field_name.capitalize()} information"
        
    # 如果是纯英文/数字，直接返回
    return text

# 遍历所有iPhone数据
print(f"开始处理 {len(data)} 个iPhone产品数据...")
for iphone in data:
    # 记录此iPhone是否有更新
    phone_updated = False
    
    # 遍历所有字段
    for field, value in list(iphone.items()):
        # 跳过不需要处理的字段
        if field in ignore_fields:
            continue
            
        # 如果字段已经是双语对象格式，跳过
        if isinstance(value, dict) and ('zh-CN' in value or 'en-US' in value):
            continue
            
        # 记录字段更新
        if field not in fields_updated:
            fields_updated[field] = 0
            
        # 处理字段值
        if isinstance(value, str) and value:
            # 获取英文翻译
            en_value = translate_field(field, value)
            
            if en_value is not None and en_value != value:
                # 更新为双语格式
                iphone[field] = {
                    'zh-CN': value,
                    'en-US': en_value
                }
                fields_updated[field] += 1
                phone_updated = True
                updated_count += 1
                
        # 处理列表类型的字段（如colors）
        elif isinstance(value, list):
            # 仅对包含字符串的列表进行处理
            if all(isinstance(item, str) for item in value):
                continue  # 列表类型的数据在前端可以用formatter处理，这里先跳过
                
            # 复杂的列表对象（如color对象列表）暂不处理
                
    if phone_updated:
        print(f"已更新产品: {iphone.get('id', '未知ID')}")

# 统计更新情况
print("\n更新统计:")
print(f"总计更新字段: {updated_count}")
print("各字段更新数量:")
for field, count in sorted(fields_updated.items(), key=lambda x: x[1], reverse=True):
    if count > 0:
        print(f"- {field}: {count}")

# 写入更新后的数据
with open(source_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    
print(f"\n更新完成! 数据已保存至 {source_file}")
print(f"原始数据备份在 {backup_file}")
