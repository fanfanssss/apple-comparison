#!/usr/bin/env python3
import json
import os

# 读取JSON文件
json_path = os.path.join('public', 'data', 'iphone_refined.json')
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 需要检查的参数
params = ['displayHdrBrightness', 'wirelessCharging']

# 遍历所有iPhone型号
modified = False
for phone in data:
    for param in params:
        # 如果参数不存在，添加"无"
        if param not in phone:
            phone[param] = "无"
            modified = True
            print(f"为 {phone['name']} 添加了 {param}: 无")

# 保存修改后的JSON文件
if modified:
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("文件已更新")
else:
    print("没有需要更新的内容")
