#!/usr/bin/env python3
import json
import re

# 读取JSON文件
with open('public/data/iphone_refined.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理计数器
updated_count = 0
fields_updated = {
    "name": 0,
    "batteryLife": 0,
    "audioFeatures": 0,
    "materials": 0,
    "displayTechnology": 0
}

# 英文翻译映射
translations = {
    # 常见电池寿命描述的翻译
    "batteryLife": {
        "视频播放：最长([0-9]+)小时，音频播放：最长([0-9]+)小时": 
            lambda m: f"Video playback: Up to {m.group(1)} hours, Audio playback: Up to {m.group(2)} hours",
        "视频播放：([0-9]+)小时，音频播放：([0-9]+)小时": 
            lambda m: f"Video playback: {m.group(1)} hours, Audio playback: {m.group(2)} hours",
        "视频播放：最长([0-9]+)小时": 
            lambda m: f"Video playback: Up to {m.group(1)} hours"
    },
    # 音频特性翻译
    "audioFeatures": {
        "立体声扬声器": "Stereo speakers",
        "立体声扬声器，杜比全景声支持": "Stereo speakers with Dolby Atmos support",
        "立体声扬声器，支持空间音频": "Stereo speakers with spatial audio support",
        "单声道扬声器": "Mono speaker"
    },
    # 材质翻译
    "materials": {
        "钛合金中框": "Titanium frame",
        "铝合金中框": "Aluminum frame",
        "不锈钢中框": "Stainless steel frame",
        "强化玻璃": "Hardened glass",
        "超瓷晶面板": "Ceramic Shield front",
        "超瓷晶面板二代": "Ceramic Shield front (2nd generation)",
        "玻璃背板": "Glass back",
        "强化玻璃背板": "Hardened glass back",
        "塑料背板": "Plastic back"
    }
}

# 辅助函数：应用正则表达式翻译
def apply_regex_translation(text, field_translations):
    for pattern, translator in field_translations.items():
        match = re.search(pattern, text)
        if match:
            return translator(match)
    return None

# 辅助函数：翻译电池寿命文本
def translate_battery_life(text):
    # 尝试使用正则表达式匹配
    translation = apply_regex_translation(text, translations["batteryLife"])
    if translation:
        return translation
        
    # 如果没有匹配成功，尝试一些常见情况
    if "视频播放" in text and "音频播放" in text:
        # 尝试提取数字并构建翻译
        video_hours = re.search(r'视频播放：[最长约]*([0-9]+)[小时h]', text)
        audio_hours = re.search(r'音频播放：[最长约]*([0-9]+)[小时h]', text)
        
        if video_hours and audio_hours:
            return f"Video playback: Up to {video_hours.group(1)} hours, Audio playback: Up to {audio_hours.group(1)} hours"
    
    # 返回通用翻译
    return "Battery life varies by use and configuration"

# 辅助函数：翻译音频特性
def translate_audio_features(text):
    # 检查是否完全匹配
    if text in translations["audioFeatures"]:
        return translations["audioFeatures"][text]
        
    # 部分匹配
    for key, value in translations["audioFeatures"].items():
        if key in text:
            return value
            
    # 默认返回
    return "Built-in audio"

# 辅助函数：翻译材质
def translate_materials(text):
    result = []
    
    # 对常见材质术语进行翻译
    for zh_term, en_term in translations["materials"].items():
        if zh_term in text:
            # 替换中文术语为英文
            text = text.replace(zh_term, en_term)
            
    # 如果翻译后仍有中文，则返回通用描述
    if re.search('[\u4e00-\u9fff]', text):
        return "Premium materials including glass and metal"
    
    return text

# 遍历所有iPhone数据
for iphone in data:
    # 记录此iPhone是否有更新
    phone_updated = False
    
    # 1. 更新名称字段 (name)
    if isinstance(iphone.get('name'), str):
        zh_name = iphone['name']
        
        # 对于iPhone SE系列的特殊处理
        if "SE" in zh_name:
            gen_match = re.search(r'第([一二三四五六七八九十\d]+)代', zh_name)
            if gen_match:
                gen_text = gen_match.group(1)
                gen_num = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5"}.get(gen_text, gen_text)
                en_name = f"iPhone SE ({gen_num}rd generation)" if gen_num == "3" else f"iPhone SE ({gen_num}th generation)" if gen_num == "4" else f"iPhone SE ({gen_num}nd generation)" if gen_num == "2" else f"iPhone SE ({gen_num}st generation)"
            else:
                en_name = "iPhone SE"
                
        # iPhone第一代特殊处理
        elif "第1代" in zh_name or "第一代" in zh_name:
            en_name = "iPhone (1st generation)"
            
        # 普通iPhone型号
        else:
            en_name = zh_name.replace("iPhone(", "iPhone (").replace("（", "(").replace("）", ")")
            en_name = re.sub(r'第\s*(\d+)\s*代', r'\1', en_name)  # 去掉"第X代"
            
        iphone['name'] = {
            'zh-CN': zh_name,
            'en-US': en_name
        }
        fields_updated["name"] += 1
        phone_updated = True
            
    # 2. 更新电池续航 (batteryLife)
    if isinstance(iphone.get('batteryLife'), str) and iphone.get('batteryLife'):
        battery_life_zh = iphone['batteryLife']
        battery_life_en = translate_battery_life(battery_life_zh)
        
        iphone['batteryLife'] = {
            'zh-CN': battery_life_zh,
            'en-US': battery_life_en
        }
        fields_updated["batteryLife"] += 1
        phone_updated = True
            
    # 3. 更新音频功能 (audioFeatures)
    if isinstance(iphone.get('audioFeatures'), str) and iphone.get('audioFeatures'):
        audio_features_zh = iphone['audioFeatures']
        audio_features_en = translate_audio_features(audio_features_zh)
        
        iphone['audioFeatures'] = {
            'zh-CN': audio_features_zh,
            'en-US': audio_features_en
        }
        fields_updated["audioFeatures"] += 1
        phone_updated = True
            
    # 4. 更新材质 (materials)
    if isinstance(iphone.get('materials'), str) and iphone.get('materials'):
        materials_zh = iphone['materials']
        materials_en = translate_materials(materials_zh)
        
        iphone['materials'] = {
            'zh-CN': materials_zh,
            'en-US': materials_en
        }
        fields_updated["materials"] += 1
        phone_updated = True
            
    # 5. 更新显示技术 (displayTechnology)
    if isinstance(iphone.get('displayTechnology'), str) and iphone.get('displayTechnology'):
        display_tech_zh = iphone['displayTechnology']
        # 简单替换常见术语
        display_tech_en = display_tech_zh.replace('英寸', '\"')
        
        # 替换中文术语为英文术语
        display_tech_en = display_tech_en.replace('超视网膜', 'Super Retina')
        display_tech_en = display_tech_en.replace('视网膜', 'Retina')
        display_tech_en = display_tech_en.replace('分辨率', 'resolution')
        
        # 如果翻译后仍然包含中文，则使用通用描述
        if re.search('[\u4e00-\u9fff]', display_tech_en):
            size_match = re.search(r'([\d\.]+)(?:英寸|\")', display_tech_zh)
            resolution_match = re.search(r'(\d+)×(\d+)', display_tech_zh)
            
            if size_match and resolution_match:
                display_tech_en = f"{size_match.group(1)}\" display with {resolution_match.group(1)}×{resolution_match.group(2)} resolution"
            elif size_match:
                display_tech_en = f"{size_match.group(1)}\" display"
            else:
                display_tech_en = "High-quality display"
        
        iphone['displayTechnology'] = {
            'zh-CN': display_tech_zh,
            'en-US': display_tech_en
        }
        fields_updated["displayTechnology"] += 1
        phone_updated = True
    
    # 计数更新的设备
    if phone_updated:
        updated_count += 1

print(f"总共更新了 {updated_count} 个 iPhone 型号")
print("字段更新统计:")
for field, count in fields_updated.items():
    print(f"- {field}: {count}个")

# 写回JSON文件
with open('public/data/iphone_refined.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    
print("数据已保存到 public/data/iphone_refined.json")
