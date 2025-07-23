#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import pandas as pd
import re
import shutil
from datetime import datetime

def load_excel_data(file_path):
    """从Excel文件加载数据"""
    try:
        excel_data = pd.read_excel(file_path)
        return excel_data
    except Exception as e:
        print(f"加载Excel文件失败: {str(e)}")
        return None

def load_json_data(file_path):
    """从JSON文件加载数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data
    except Exception as e:
        print(f"加载JSON文件失败: {str(e)}")
        return None

def save_json_data(file_path, data):
    """保存数据到JSON文件"""
    try:
        # 创建备份
        if os.path.exists(file_path):
            backup_path = f"{file_path}.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}"
            shutil.copy2(file_path, backup_path)
            print(f"已创建备份: {backup_path}")
        
        # 保存新数据
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到: {file_path}")
        return True
    except Exception as e:
        print(f"保存JSON文件失败: {str(e)}")
        return False

def update_json_data(excel_data, json_data):
    """根据Excel数据更新JSON数据"""
    # 创建一个字典，用于快速查找现有数据
    existing_data = {item['id']: item for item in json_data}
    updated_count = 0
    new_count = 0
    
    # 记录所有在Excel中存在但未在field_mapping中定义的列
    unmapped_columns = set()
    
    # 定义Excel列名到JSON字段名的映射
    field_mapping = {
        'ID': 'id',
        '机型名称': 'name',
        'releaseDate': 'releaseDate',
        'processor': 'processor',
        'processorDetails': 'processorDetails',  # 处理器详细信息
        'ram': 'ram',
        'chipPerformance': 'cpuPerformance',     # 将分离为单核和多核跑分
        'gpuPerformance': 'gpuPerformance',
        'display': 'displayTechnology',
        'displaySize': 'displaySize',           # 屏幕尺寸
        'displayResolution': 'displayResolution', # 屏幕分辨率
        'screenBrightness': 'displayBrightness',
        'displayRefreshRate': 'displayRefreshRate', # 屏幕刷新率
        'camera': 'camera',
        'faceTimeCamera': 'frontCamera',
        'battery': 'battery',
        'batteryLife': 'batteryLife',
        'batteryLifeScore': 'batteryLifeScore', # 电池续航评分
        'charging': 'charging',
        'wireless': 'wireless',
        'storage': 'storage',
        'price': 'price',
        'dimensions': 'dimensions',
        'weight': 'weight',
        'os': 'os',
        'connectivity': 'connectivity',
        'cellularFeatures': 'cellularFeatures',
        'satelliteFeatures': 'satelliteFeatures',
        'colors': 'colors',
        'materials': 'materials',
        'waterResistance': 'waterResistance',
        'security': 'security',
        'sensors': 'sensors',
        'ports': 'ports',
        'audioFeatures': 'audioFeatures',
        'modelIdentifier': 'model',
        'baseband': 'baseband',
        'techSpecs': 'technicalSpecsLink',
        'marketingSlogan': 'marketingSlogan',
        'specialFeatures': 'specialFeatures'  # 特殊功能
    }
    
    # 检查Excel中存在但未在field_mapping中定义的列
    for column in excel_data.columns:
        if column not in field_mapping and column not in ['index', 'Unnamed: 0']:
            unmapped_columns.add(column)
    
    # 如果有未映射的列，打印警告
    if unmapped_columns:
        print("警告: 以下Excel列未映射到JSON字段:")
        for column in sorted(unmapped_columns):
            print(f"  - {column}")
        print("请考虑更新field_mapping字典以包含这些列。")
    
    # 遍历Excel数据，更新或添加到JSON数据
    for _, row in excel_data.iterrows():
        product_id = str(row['ID']).strip()
        
        # 检查产品ID是否存在
        if not product_id or pd.isna(product_id):
            print("警告: 跳过没有ID的行")
            continue
        
        # 检查是更新还是新增
        if product_id in existing_data:
            product = existing_data[product_id]
            is_new = False
            updated_count += 1
        else:
            product = {'id': product_id}
            is_new = True
            new_count += 1
        
        # 更新产品数据
        for excel_column, json_field in field_mapping.items():
            if excel_column in excel_data.columns and not pd.isna(row.get(excel_column)):
                value = row[excel_column]
                
                # 根据字段类型进行特殊处理
                if excel_column == 'colors':
                    try:
                        # 尝试解析颜色数据，格式应为: 颜色名称1:#颜色代码1,颜色名称2:#颜色代码2,...
                        colors_str = str(value)
                        colors = []
                        for color_pair in colors_str.split(','):
                            if ':' in color_pair:
                                name, code = color_pair.split(':')
                                colors.append({"name": name.strip(), "code": code.strip()})
                        if colors:
                            product[json_field] = colors
                    except Exception as e:
                        print(f"处理颜色数据时出错 (ID: {product_id}): {str(e)}")
                elif excel_column == 'storage':
                    # 存储容量应为逗号分隔的列表
                    try:
                        storage_str = str(value)
                        product[json_field] = [item.strip() for item in storage_str.split(',')]
                    except Exception as e:
                        print(f"处理存储容量数据时出错 (ID: {product_id}): {str(e)}")
                elif json_field in ['cpuPerformance', 'gpuPerformance', 'price', 'batteryLifeScore']:
                    # 数值型字段
                    try:
                        # 尝试直接转换为整数
                        product[json_field] = int(value)
                    except ValueError:
                        try:
                            # 尝试直接转换为浮点数
                            product[json_field] = float(value)
                        except ValueError:
                            # 处理特殊格式的价格
                            if json_field == 'price':
                                try:
                                    # 提取价格中的数字部分
                                    import re
                                    price_match = re.search(r'(\d+(?:\.\d+)?)', str(value))
                                    if price_match:
                                        product[json_field] = int(float(price_match.group(1)))
                                    else:
                                        print(f"警告: 无法从 '{value}' 提取价格 (ID: {product_id})")
                                except Exception as e:
                                    print(f"警告: 处理价格时出错 '{value}' (ID: {product_id}): {str(e)}")
                            # 处理CPU性能跑分
                            elif json_field == 'cpuPerformance':
                                try:
                                    import re
                                    # 提取单核跑分
                                    single_score_match = re.search(r'单核跑分[：:](\s*)(\d+)', str(value))
                                    # 提取多核跑分
                                    multi_score_match = re.search(r'多核跑分[：:](\s*)(\d+)', str(value))
                                    
                                    # 创建或更新跑分对象
                                    if 'cpuPerformance' not in product or not isinstance(product['cpuPerformance'], dict):
                                        product['cpuPerformance'] = {}
                                    
                                    # 添加单核跑分
                                    if single_score_match:
                                        product['cpuPerformance']['singleCore'] = int(single_score_match.group(2))
                                    
                                    # 添加多核跑分
                                    if multi_score_match:
                                        product['cpuPerformance']['multiCore'] = int(multi_score_match.group(2))
                                    
                                    # 如果都没有匹配到且不是"无"，打印警告
                                    if not single_score_match and not multi_score_match and value != '无':
                                        print(f"警告: 无法从 '{value}' 提取CPU性能跑分 (ID: {product_id})")
                                        
                                    # 如果没有提取到任何跑分，但值不是"无"，则保留原始值
                                    if not single_score_match and not multi_score_match and value != '无':
                                        product['cpuPerformanceRaw'] = str(value)
                                except Exception as e:
                                    print(f"警告: 处理CPU性能跑分时出错 '{value}' (ID: {product_id}): {str(e)}")
                                
                                # 跳过后续处理，因为我们已经手动处理了跑分
                                continue
                            # 处理GPU性能跑分
                            elif json_field == 'gpuPerformance':
                                if value == '无':
                                    # 对于没有GPU跑分的旧设备，设置为0或不设置
                                    product[json_field] = 0
                                else:
                                    print(f"警告: 无法从 '{value}' 提取GPU跑分 (ID: {product_id})")
                            else:
                                print(f"警告: 无法将 '{value}' 转换为数值 (ID: {product_id}, 字段: {json_field})")
                else:
                    # 其他字段直接赋值
                    product[json_field] = value
        
        # 如果是新产品，添加到JSON数据中
        if is_new:
            json_data.append(product)
    
    print(f"更新了 {updated_count} 个产品，新增了 {new_count} 个产品。")
    return json_data

def check_missing_fields(json_data):
    """检查JSON数据中缺失的字段"""
    # 定义所有可能的字段
    all_fields = [
        'id', 'name', 'releaseDate', 'processor', 'processorDetails', 'ram', 'cpuPerformance',
        'gpuPerformance', 'displayTechnology', 'displaySize', 'displayResolution', 
        'displayBrightness', 'displayRefreshRate', 'camera', 'frontCamera', 'battery', 
        'batteryLife', 'batteryLifeScore', 'charging', 'wireless', 'storage', 'price', 
        'dimensions', 'weight', 'os', 'connectivity', 'cellularFeatures', 'satelliteFeatures', 
        'colors', 'materials', 'waterResistance', 'security', 'sensors', 'ports', 
        'audioFeatures', 'model', 'baseband', 'technicalSpecsLink', 'marketingSlogan',
        'specialFeatures'
    ]
    
    # 统计每个字段的缺失情况
    missing_stats = {field: 0 for field in all_fields}
    total_products = len(json_data)
    
    # 检查每个产品
    for product in json_data:
        for field in all_fields:
            # 特殊处理cpuPerformance字段，因为它现在是一个对象
            if field == 'cpuPerformance':
                if field not in product or not isinstance(product[field], dict) or \
                   ('singleCore' not in product[field] and 'multiCore' not in product[field]):
                    missing_stats[field] += 1
            elif field not in product or product[field] is None or product[field] == '':
                missing_stats[field] += 1
    
    # 打印缺失字段统计
    print("\n字段完整性检查:")
    print(f"总产品数: {total_products}")
    print("\n缺失字段统计:")
    
    # 按缺失比例排序
    sorted_stats = sorted(missing_stats.items(), key=lambda x: x[1], reverse=True)
    
    for field, count in sorted_stats:
        if count > 0:
            percentage = (count / total_products) * 100
            print(f"  {field}: 缺失 {count}/{total_products} ({percentage:.1f}%)")
    
    # 检查每个产品的完整性
    print("\n产品完整性检查:")
    for product in json_data:
        missing_fields = []
        for field in all_fields:
            # 特殊处理cpuPerformance字段
            if field == 'cpuPerformance':
                if field not in product or not isinstance(product[field], dict) or \
                   ('singleCore' not in product[field] and 'multiCore' not in product[field]):
                    missing_fields.append(field)
            elif field not in product or product[field] is None or product[field] == '':
                missing_fields.append(field)
        
        # 只打印缺失字段较多的产品
        if len(missing_fields) > 5:
            print(f"  {product.get('name', product.get('id', 'Unknown'))}: 缺失 {len(missing_fields)} 个字段")
            # 打印前5个缺失字段
            print(f"    缺失字段: {', '.join(missing_fields[:5])}...")
    
    return missing_stats

def main():
    excel_file = 'iPhone数据表.xlsx'
    json_file = 'public/data/iphone.json'
    
    # 加载数据
    excel_data = load_excel_data(excel_file)
    json_data = load_json_data(json_file)
    
    if excel_data is None or json_data is None:
        print("数据加载失败，退出程序。")
        return
    
    # 更新数据
    updated_data = update_json_data(excel_data, json_data)
    
    # 检查缺失字段
    check_missing_fields(updated_data)
    
    # 保存更新后的数据
    save_json_data(json_file, updated_data)

if __name__ == "__main__":
    main()
