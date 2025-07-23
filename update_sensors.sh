#!/bin/bash

# 创建备份
cp /Users/aron/CascadeProjects/apple-comparison/public/data/watch_refined.json /Users/aron/CascadeProjects/apple-comparison/public/data/watch_refined_backup_$(date +%Y%m%d_%H%M%S).json

# 定义所有传感器字段
sensors=(
  "ecgSensor"
  "bloodOxygenSensor"
  "temperatureSensor"
  "waterTemperatureSensor"
  "depthGauge"
)

# 处理每个传感器字段
for sensor in "${sensors[@]}"; do
  # 在每个产品对象的结尾处查找是否缺少该传感器字段
  # 如果缺少，则添加该字段并设置为❌
  sed -i '' -E 's/("compass": "[^"]+",)\s*("technicalSpecsLink": "[^"]+")/\1\n    "'$sensor'": "❌",\n    \2/g' /Users/aron/CascadeProjects/apple-comparison/public/data/watch_refined.json
done

echo "完成传感器字段更新"
