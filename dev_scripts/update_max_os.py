#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import os
import re
from datetime import datetime

# 文件路径
json_file = 'public/data/iphone_refined.json'

# 创建备份
backup_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'{json_file}.bak.{backup_timestamp}'

# 读取JSON数据
with open(json_file, 'r', encoding='utf-8') as f:
    iphone_data = json.load(f)

# 创建备份
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)
    print(f'已创建备份文件: {backup_file}')

# 定义iPhone型号与最高支持系统版本的映射规则
def get_max_os_version(phone_id, release_date):
    # 将发布日期转换为日期对象，便于比较
    release_date_obj = None
    if release_date:
        # 尝试提取年份和月份
        match = re.search(r'(\d{4})年(\d{1,2})月', release_date)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            release_date_obj = datetime(year, month, 1)
    
    # iPhone 11及之后发布的机型
    iphone_11_date = datetime(2019, 9, 1)
    
    # 按照规则设置最高支持系统版本
    if release_date_obj and release_date_obj >= iphone_11_date:
        return "最新"
    
    # 根据型号ID判断
    if any(id_part in phone_id for id_part in ["iphone-11", "iphone-12", "iphone-13", "iphone-14", "iphone-15", "iphone-16", "iphone-se-2", "iphone-se-3"]):
        return "最新"
    elif any(id_part in phone_id for id_part in ["iphone-xs", "iphone-xs-max", "iphone-xr"]):
        return "iOS 18"
    elif any(id_part in phone_id for id_part in ["iphone-x", "iphone-8", "iphone-8-plus"]):
        return "iOS 16"
    elif any(id_part in phone_id for id_part in ["iphone-7", "iphone-7-plus", "iphone-6s", "iphone-6s-plus", "iphone-se"]):
        return "iOS 15"
    elif any(id_part in phone_id for id_part in ["iphone-6", "iphone-6-plus", "iphone-5s"]):
        return "iOS 12"
    elif any(id_part in phone_id for id_part in ["iphone-5", "iphone-5c"]):
        return "iOS 10"
    elif "iphone-4s" in phone_id:
        return "iOS 9"
    elif "iphone-4" in phone_id:
        return "iOS 7"
    elif "iphone-3gs" in phone_id:
        return "iOS 6"
    elif "iphone-3g" in phone_id:
        return "iOS 4"
    elif "iphone-2g" in phone_id or "iphone-1" in phone_id:
        return "iOS 3"
    else:
        # 默认情况，保持原值
        return None

# 更新最高支持系统版本
updated_count = 0
for phone in iphone_data:
    phone_id = phone.get('id', '')
    release_date = phone.get('releaseDate', '')
    
    max_os = get_max_os_version(phone_id, release_date)
    if max_os and ('maxSupportedOS' in phone or max_os == "最新"):
        phone['maxSupportedOS'] = max_os
        updated_count += 1

# 保存更新后的JSON数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(iphone_data, f, ensure_ascii=False, indent=2)

print(f'更新完成! 已更新 {updated_count} 个iPhone型号的最高支持系统版本')
