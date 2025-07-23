#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

# 读取 JSON 文件
json_file = '/Users/aron/CascadeProjects/apple-comparison/public/data/ipad_refined.json'
with open(json_file, 'r', encoding='utf-8') as f:
    ipad_data = json.load(f)

# 查找并修改第一代 iPad 的内存信息
for ipad in ipad_data:
    if ipad.get('id') == 'ipad-ipad':
        print(f"找到第一代 iPad: {ipad['name']}")
        print(f"原内存值: {ipad.get('ram', '未设置')}")
        ipad['ram'] = ["256MB DDR"]
        print(f"修改后内存值: {ipad['ram']}")
        break

# 保存修改后的数据
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(ipad_data, f, ensure_ascii=False, indent=2)

print("修改完成!")
