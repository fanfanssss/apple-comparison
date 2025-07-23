import json
import datetime
import os

# 备份原始文件
backup_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
backup_file = f'public/data/iphone_refined.json.bak.{backup_timestamp}'

# 读取JSON文件
with open('public/data/iphone_refined.json', 'r', encoding='utf-8') as f:
    refined_data = json.load(f)

# 创建备份
with open(backup_file, 'w', encoding='utf-8') as f:
    json.dump(refined_data, f, ensure_ascii=False, indent=2)

# 定义iPhone发布日期的比较函数
def is_later_than(date_str, reference_date_str):
    # 提取年份
    year = int(date_str.split('年')[0])
    ref_year = int(reference_date_str.split('年')[0])
    
    if year > ref_year:
        return True
    elif year < ref_year:
        return False
    
    # 如果年份相同，比较月份
    if '月' in date_str and '月' in reference_date_str:
        month = int(date_str.split('年')[1].split('月')[0])
        ref_month = int(reference_date_str.split('年')[1].split('月')[0])
        return month >= ref_month
    
    return False

# 更新显示色域信息
iphone8_release_date = '2017年9月'

for phone in refined_data:
    model_id = phone.get('id', '').lower()
    release_date = phone.get('releaseDate', '')
    
    # iPhone 8、iPhone 8 Plus、iPhone X和比iPhone 8晚发布的所有机型
    if ('iphone-8' in model_id or 'iphone-x' in model_id or 
        (release_date and is_later_than(release_date, iphone8_release_date))):
        phone['displayColorGamut'] = 'P3广色域和原彩显示'
    
    # iPhone 7和iPhone 7 Plus
    elif 'iphone-7' in model_id:
        phone['displayColorGamut'] = 'P3广色域'
    
    # iPhone 6和6 Plus、iPhone 6s和6s Plus、iPhone SE第一代
    elif ('iphone-6' in model_id or 
          ('iphone-se' in model_id and not any(x in model_id for x in ['-2', '-3']))):
        phone['displayColorGamut'] = '全sRGB'
    
    # 其它机型
    else:
        phone['displayColorGamut'] = ''

# 保存更新后的JSON文件
with open('public/data/iphone_refined.json', 'w', encoding='utf-8') as f:
    json.dump(refined_data, f, ensure_ascii=False, indent=2)

print(f'已成功更新iphone_refined.json的显示色域信息并创建备份文件: {backup_file}')
print(f'更新了{len(refined_data)}个iPhone型号的显示色域信息')
