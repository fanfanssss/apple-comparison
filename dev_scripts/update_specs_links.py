#!/usr/bin/env python3
import json
import os
import shutil
from datetime import datetime

# 创建备份
json_path = '/Users/aron/CascadeProjects/apple-comparison/public/data/watch_refined.json'
backup_path = f'/Users/aron/CascadeProjects/apple-comparison/public/data/watch_refined_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
shutil.copy(json_path, backup_path)

# 读取JSON文件
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 技术规格链接映射
specs_links = {
    "Apple Watch Series 10": "https://support.apple.com/zh-cn/121202",
    "Apple Watch Series 9": "https://support.apple.com/zh-cn/111833",
    "Apple Watch Ultra 2": "https://support.apple.com/zh-cn/111848",
    "Apple Watch Series 8": "https://support.apple.com/zh-cn/111909",
    "Apple Watch Ultra": "https://support.apple.com/zh-cn/111918",
    "Apple Watch SE(第 2 代)": "https://support.apple.com/zh-cn/118453",
    "Apple Watch Series 7": "https://support.apple.com/zh-cn/111984",
    "Apple Watch Series 6": "https://support.apple.com/zh-cn/111891",
    "Apple Watch SE(第 1 代)": "https://support.apple.com/zh-cn/112022",
    "Apple Watch Series 5": "https://support.apple.com/zh-cn/111985",
    "Apple Watch Series 4": "https://support.apple.com/zh-cn/112009",
    "Apple Watch Series 3": "https://support.apple.com/zh-cn/112009",
    "Apple Watch Series 2": "https://support.apple.com/zh-cn/112009",
    "Apple Watch Series 1": "https://support.apple.com/zh-cn/112009",
    "Apple Watch(第 1 代)": "https://support.apple.com/zh-cn/112009"
}

# 更新技术规格链接
for watch in data:
    watch_name = watch.get("name", "")
    if watch_name in specs_links:
        watch["technicalSpecsLink"] = {
            "text": "技术规格",
            "url": specs_links[watch_name]
        }

# 保存修改后的JSON文件
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已成功更新所有Apple Watch型号的技术规格链接")
