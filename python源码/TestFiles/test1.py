''' 
CityData：
        将str1中的数据写进A1到F6这个区域内，
        并以xlsx后缀保存。
'''

str1 = '''
北京市 京 北京
上海市 沪 上海
天津市 津 天津
重庆市 渝 重庆
黑龙江省 黑 哈尔滨
吉林省 吉 长春
辽宁省 辽 沈阳
内蒙古 蒙 呼和浩特
河北省 冀 石家庄
新疆 新 乌鲁木齐
甘肃省 甘 兰州
青海省 青 西宁
陕西省 陕 西安
宁夏 宁 银川
河南省 豫 郑州
山东省 鲁 济南
山西省 晋 太原
安徽省 皖 合肥
湖北省 鄂 武汉
湖南省 湘 长沙
江苏省 苏 南京
四川省 川 成都
贵州省 黔 贵阳
云南省 滇 昆明
广西省 桂 南宁
西藏 藏 拉萨
浙江省 浙 杭州
江西省 赣 南昌
广东省 粤 广州
福建省 闽 福州
台湾省 台 台北
海南省 琼 海口
香港 港 香港
澳门 澳 澳门'''

#把str1中的数据用正则表达式提取出来并保存到字典中。
import re,pyperclip,random
content = re.findall(r'[^\r\n]+',str1)
content
province,city = [],[]
dict1 = {}
for i in content:
    list1 = i.split(' ')
    province.append(list1[0])
    city.append(list1[2])
    dict1[list1[0]] = list1[2]
dict1.setdefault('秦','咸阳')
dict1.setdefault('唐','长安')
dict1
keys = list(dict1.keys())

from openpyxl import Workbook
wb = Workbook()
ws1 = wb.create_sheet('MySheet')
area = ws1['A1':'F6']
j = 0
for cell in area:
    for m in range(6):
        cell[m].value = dict1[keys[j]]
        j = j + 1
wb.save('the_test_file.xlsx')
