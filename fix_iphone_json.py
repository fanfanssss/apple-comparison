#!/usr/bin/env python3
import json
import re

print("开始修复iPhone JSON数据...")

# 读取JSON文件
source_file = 'public/data/iphone_refined.json'
backup_file = 'public/data/iphone_refined_before_fix.json'

# 创建备份
with open(source_file, 'r', encoding='utf-8') as f:
    data = json.load(f)
    with open(backup_file, 'w', encoding='utf-8') as bf:
        json.dump(data, bf, ensure_ascii=False, indent=2)

print(f"已创建备份: {backup_file}")

# 修复计数
fields_fixed = {}
generic_texts_fixed = 0
mark_texts_fixed = 0

# 查找并修复问题
for iphone in data:
    # 遍历所有字段
    for field, value in list(iphone.items()):
        # 修复双语对象
        if isinstance(value, dict) and ('zh-CN' in value or 'en-US' in value):
            # 记录字段
            if field not in fields_fixed:
                fields_fixed[field] = 0
            
            # 检查是否包含通用替换文本 (如 "xxx information")
            en_value = value.get('en-US', '')
            zh_value = value.get('zh-CN', '')
            
            if isinstance(en_value, str) and " information" in en_value:
                # 如果是通用替换文本，使用中文值
                value['en-US'] = zh_value
                generic_texts_fixed += 1
                fields_fixed[field] += 1
            
            # 修复包含__MARK__标记的文本
            if isinstance(en_value, str) and "__MARK__" in en_value:
                # 清理标记
                clean_text = en_value.replace("__MARK__", "")
                value['en-US'] = clean_text
                mark_texts_fixed += 1
                fields_fixed[field] += 1
                
            # 修复重复字段，如"4G LTE LTE"
            if isinstance(en_value, str) and re.search(r'(\w+)\s+\1', en_value):
                clean_text = re.sub(r'(\w+)\s+\1', r'\1', en_value)
                value['en-US'] = clean_text
                fields_fixed[field] += 1

# 写回文件
with open(source_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n修复完成! 共修复 {generic_texts_fixed} 个通用替换文本和 {mark_texts_fixed} 个标记文本问题")
print("按字段统计修复:")
for field, count in sorted(fields_fixed.items(), key=lambda x: x[1], reverse=True):
    if count > 0:
        print(f"- {field}: {count}")

print(f"\n修复后的数据已保存至 {source_file}")
