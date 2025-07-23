#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
iPhone数据补充脚本
用于补充iPhone数据中缺失的参数，并更新到网站的JSON文件中
"""

import os
import json
import sys
from datetime import datetime
import re

# 定义文件路径
JSON_FILE = 'public/data/iphone.json'
BACKUP_DIR = 'data_backups'

def create_backup(json_file):
    """创建JSON文件的备份"""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUP_DIR, f'iphone_data_supplement_backup_{timestamp}.json')
    
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = f.read()
        
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(data)
        
        print(f'已创建备份: {backup_file}')
    else:
        print(f'警告: {json_file} 不存在，无法创建备份')

def load_json_data(json_file):
    """加载现有的JSON数据"""
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f'读取JSON文件失败: {str(e)}')
            sys.exit(1)
    else:
        print(f'错误: {json_file} 不存在')
        sys.exit(1)

def save_json_data(json_data, json_file):
    """保存JSON数据到文件"""
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print(f'数据已保存到 {json_file}')
    except Exception as e:
        print(f'保存JSON文件失败: {str(e)}')
        sys.exit(1)

def supplement_display_data(product):
    """补充显示相关参数"""
    # 从displayTechnology中提取displaySize
    if 'displayTechnology' in product and not product.get('displaySize'):
        display_tech = product['displayTechnology']
        size_match = re.search(r'(\d+\.?\d?)英寸', display_tech)
        if size_match:
            product['displaySize'] = f"{size_match.group(1)}英寸"
    
    # 从displayTechnology中提取displayResolution
    if 'displayTechnology' in product and not product.get('displayResolution'):
        display_tech = product['displayTechnology']
        res_match = re.search(r'(\d+×\d+|\d+\s*[xX]\s*\d+)(?:\s*像素)?', display_tech)
        if res_match:
            product['displayResolution'] = res_match.group(1).replace('x', '×').replace('X', '×') + ' 像素'
    
    # 从displayTechnology中提取displayRefreshRate
    if 'displayTechnology' in product and not product.get('displayRefreshRate'):
        display_tech = product['displayTechnology']
        if 'ProMotion' in display_tech or '120Hz' in display_tech:
            product['displayRefreshRate'] = '1-120Hz 自适应刷新率'
        elif '60Hz' in display_tech:
            product['displayRefreshRate'] = '60Hz'
        else:
            product['displayRefreshRate'] = '60Hz'

def supplement_processor_details(product):
    """补充处理器详情"""
    if 'processor' in product and not product.get('processorDetails'):
        processor = product['processor']
        
        # 根据处理器型号推断详情
        if 'A18 Pro' in processor:
            product['processorDetails'] = '台积电第二代3纳米工艺，6核CPU (2性能核心+4能效核心)，6核GPU，16核神经网络引擎'
        elif 'A17 Pro' in processor:
            product['processorDetails'] = '台积电3纳米工艺，6核CPU (2性能核心+4能效核心)，6核GPU，16核神经网络引擎'
        elif 'A16' in processor:
            product['processorDetails'] = '台积电4纳米工艺，6核CPU (2性能核心+4能效核心)，5核GPU，16核神经网络引擎'
        elif 'A15' in processor:
            if '5GPU' in processor:
                product['processorDetails'] = '台积电5纳米工艺，6核CPU (2性能核心+4能效核心)，5核GPU，16核神经网络引擎'
            else:
                product['processorDetails'] = '台积电5纳米工艺，6核CPU (2性能核心+4能效核心)，4核GPU，16核神经网络引擎'
        elif 'A14' in processor:
            product['processorDetails'] = '台积电5纳米工艺，6核CPU (2性能核心+4能效核心)，4核GPU，16核神经网络引擎'
        elif 'A13' in processor:
            product['processorDetails'] = '台积电7纳米+工艺，6核CPU (2性能核心+4能效核心)，4核GPU，8核神经网络引擎'
        elif 'A12' in processor:
            product['processorDetails'] = '台积电7纳米工艺，6核CPU (2性能核心+4能效核心)，4核GPU，8核神经网络引擎'
        elif 'A11' in processor:
            product['processorDetails'] = '台积电10纳米工艺，6核CPU (2性能核心+4能效核心)，3核GPU，神经网络引擎'
        elif 'A10' in processor:
            product['processorDetails'] = '台积电16纳米工艺，4核CPU (2性能核心+2能效核心)，6核GPU'
        elif 'A9' in processor:
            product['processorDetails'] = '台积电/三星14/16纳米工艺，2核CPU，6核GPU'
        elif 'A8' in processor:
            product['processorDetails'] = '台积电20纳米工艺，2核CPU，4核GPU'
        elif 'A7' in processor:
            product['processorDetails'] = '三星28纳米工艺，2核CPU，4核GPU'
        elif 'A6' in processor:
            product['processorDetails'] = '三星32纳米工艺，2核CPU，3核GPU'
        elif 'A5' in processor:
            product['processorDetails'] = '三星45纳米工艺，2核CPU，2核GPU'
        elif 'A4' in processor:
            product['processorDetails'] = '三星45纳米工艺，1核CPU，1核GPU'
        else:
            product['processorDetails'] = '处理器详情未知'

def supplement_battery_score(product):
    """补充电池续航评分"""
    if 'batteryLife' in product and not product.get('batteryLifeScore'):
        battery_life = product['batteryLife']
        
        # 根据电池续航时间推断评分
        if '视频播放' in battery_life:
            hours_match = re.search(r'(\d+)小时', battery_life)
            if hours_match:
                hours = int(hours_match.group(1))
                if hours >= 30:
                    product['batteryLifeScore'] = 95
                elif hours >= 25:
                    product['batteryLifeScore'] = 90
                elif hours >= 20:
                    product['batteryLifeScore'] = 85
                elif hours >= 15:
                    product['batteryLifeScore'] = 80
                elif hours >= 10:
                    product['batteryLifeScore'] = 75
                else:
                    product['batteryLifeScore'] = 70
        else:
            # 默认评分
            product['batteryLifeScore'] = 75

def supplement_special_features(product):
    """补充特殊功能"""
    if not product.get('specialFeatures'):
        special_features = []
        
        # 根据发布日期和其他参数推断特殊功能
        if 'releaseDate' in product:
            release_date = product['releaseDate']
            release_year = 0
            year_match = re.search(r'(\d{4})年', release_date)
            if year_match:
                release_year = int(year_match.group(1))
            
            # 根据年份添加特殊功能
            if release_year >= 2022:
                special_features.append('紧急SOS')
                special_features.append('碰撞检测')
                
            if release_year >= 2023:
                special_features.append('卫星通信')
                
            if release_year >= 2024:
                special_features.append('Apple Intelligence')
        
        # 根据处理器添加特殊功能
        if 'processor' in product:
            processor = product['processor']
            if 'A16' in processor or 'A17' in processor or 'A18' in processor:
                if '紧急SOS' not in special_features:
                    special_features.append('紧急SOS')
                if '碰撞检测' not in special_features:
                    special_features.append('碰撞检测')
        
        # 根据型号添加特殊功能
        if 'name' in product:
            name = product['name']
            if 'Pro' in name and ('14' in name or '15' in name or '16' in name):
                special_features.append('动态岛')
                
            if 'Pro' in name and ('15' in name or '16' in name):
                special_features.append('钛金属机身')
                
            if '16' in name:
                special_features.append('拍照按钮')
        
        if special_features:
            product['specialFeatures'] = '，'.join(special_features)
        else:
            product['specialFeatures'] = '无'

def supplement_colors(product):
    """补充颜色信息"""
    if not product.get('colors') or (isinstance(product.get('colors'), list) and len(product.get('colors')) == 0):
        # 根据型号和发布年份添加默认颜色
        if 'name' in product and 'releaseDate' in product:
            name = product['name']
            release_date = product['releaseDate']
            
            colors = []
            
            # iPhone 16 Pro 系列颜色
            if '16 Pro' in name:
                colors = [
                    {"name": "自然钛金属", "code": "#E3D0BA"},
                    {"name": "白色钛金属", "code": "#F5F5F0"},
                    {"name": "黑色钛金属", "code": "#505050"},
                    {"name": "沙金色钛金属", "code": "#D9C5AD"}
                ]
            # iPhone 16 系列颜色
            elif '16' in name:
                colors = [
                    {"name": "黑色", "code": "#1F2120"},
                    {"name": "白色", "code": "#F5F5F0"},
                    {"name": "粉色", "code": "#F8D9DF"},
                    {"name": "蓝色", "code": "#B0C4DE"},
                    {"name": "绿色", "code": "#A9C9A9"}
                ]
            # iPhone 15 Pro 系列颜色
            elif '15 Pro' in name:
                colors = [
                    {"name": "自然钛金属", "code": "#E3D0BA"},
                    {"name": "白色钛金属", "code": "#F5F5F0"},
                    {"name": "黑色钛金属", "code": "#505050"},
                    {"name": "蓝色钛金属", "code": "#6A7F92"}
                ]
            # iPhone 15 系列颜色
            elif '15' in name:
                colors = [
                    {"name": "黑色", "code": "#1F2120"},
                    {"name": "白色", "code": "#F5F5F0"},
                    {"name": "粉色", "code": "#F8D9DF"},
                    {"name": "黄色", "code": "#FFDB58"},
                    {"name": "蓝色", "code": "#B0C4DE"}
                ]
            # 其他iPhone默认颜色
            else:
                colors = [
                    {"name": "黑色", "code": "#1F2120"},
                    {"name": "白色", "code": "#F5F5F0"}
                ]
            
            if colors:
                product['colors'] = colors

def check_missing_fields(json_data):
    """检查JSON数据中缺失的字段"""
    # 网站中显示的参数列表
    website_params = [
        'releaseDate', 'price', 'model', 'colors', 'dimensions', 'weight', 'materials',
        'waterResistance', 'displaySize', 'displayResolution', 'displayTechnology',
        'displayBrightness', 'displayRefreshRate', 'processor', 'processorDetails',
        'ram', 'storage', 'cpuPerformance', 'gpuPerformance', 'camera', 'frontCamera',
        'battery', 'batteryLife', 'batteryLifeScore', 'charging', 'wireless', 'os',
        'connectivity', 'ports', 'security', 'cellularFeatures', 'satelliteFeatures',
        'sensors', 'audioFeatures', 'baseband', 'specialFeatures', 'technicalSpecsLink',
        'marketingSlogan'
    ]
    
    missing_fields_count = {}
    
    # 检查每个产品的缺失字段
    for product in json_data:
        product_id = product.get('id', 'unknown')
        product_name = product.get('name', 'unknown')
        
        for param in website_params:
            if param not in product or product[param] is None or product[param] == '':
                if param not in missing_fields_count:
                    missing_fields_count[param] = []
                missing_fields_count[param].append(f"{product_name} ({product_id})")
    
    # 打印缺失字段统计
    if missing_fields_count:
        print("\n数据完整性检查结果:")
        print("以下参数在某些产品中缺失:")
        for param, products in missing_fields_count.items():
            if len(products) > 5:
                print(f"  {param}: 缺失于 {len(products)} 个产品，包括 {', '.join(products[:3])} 等")
            else:
                print(f"  {param}: 缺失于 {', '.join(products)}")
    else:
        print("\n数据完整性检查结果: 所有产品的所有参数都已填写")

def main():
    """主函数"""
    print('开始补充iPhone数据...')
    
    # 创建备份
    create_backup(JSON_FILE)
    
    # 加载数据
    json_data = load_json_data(JSON_FILE)
    
    # 补充前检查缺失字段
    print('补充前数据完整性检查:')
    check_missing_fields(json_data)
    
    # 补充数据
    updated_count = 0
    for product in json_data:
        product_id = product.get('id', 'unknown')
        product_name = product.get('name', 'unknown')
        
        # 记录原始缺失字段数量
        missing_before = sum(1 for param in ['displaySize', 'displayResolution', 'displayRefreshRate', 
                                           'processorDetails', 'batteryLifeScore', 'specialFeatures', 'colors'] 
                           if param not in product or not product[param])
        
        # 补充各类参数
        supplement_display_data(product)
        supplement_processor_details(product)
        supplement_battery_score(product)
        supplement_special_features(product)
        supplement_colors(product)
        
        # 计算补充后缺失字段数量
        missing_after = sum(1 for param in ['displaySize', 'displayResolution', 'displayRefreshRate', 
                                          'processorDetails', 'batteryLifeScore', 'specialFeatures', 'colors'] 
                          if param not in product or not product[param])
        
        # 如果有字段被补充，增加计数
        if missing_before > missing_after:
            updated_count += 1
            print(f"已补充 {product_name} ({product_id}) 的参数数据")
    
    print(f"\n共补充了 {updated_count} 个产品的数据")
    
    # 补充后检查缺失字段
    print('\n补充后数据完整性检查:')
    check_missing_fields(json_data)
    
    # 保存数据
    save_json_data(json_data, JSON_FILE)
    
    print('iPhone数据补充完成！')

if __name__ == '__main__':
    main()
