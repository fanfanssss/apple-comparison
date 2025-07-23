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

# 所有可能的传感器字段
all_sensors = [
    "accelerometer",
    "gyroscope",
    "ambientLightSensor",
    "heartRateSensor",
    "ecgSensor",
    "barometer",
    "compass",
    "bloodOxygenSensor",
    "temperatureSensor",
    "waterTemperatureSensor",
    "depthGauge"
]

# 处理每个Apple Watch型号
for watch in data:
    # 检查每个传感器字段
    for sensor in all_sensors:
        # 如果传感器字段不存在，添加并设置为❌
        if sensor not in watch:
            watch[sensor] = "❌"

# 保存修改后的JSON文件
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("已成功更新所有Apple Watch型号的传感器数据")
