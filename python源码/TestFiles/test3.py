'''
Quiz:
    要求：  
        用下面数据做出35份试卷,这35份试卷的题相同，题目的顺序随机，
        每个题目的选项随机，并且做出对应试题的答案，共35份。
'''
# 北京市 京 北京
# 上海市 沪 上海
# 天津市 津 天津
# 重庆市 渝 重庆
# 黑龙江省 黑 哈尔滨
# 吉林省 吉 长春
# 辽宁省 辽 沈阳
# 内蒙古 蒙 呼和浩特
# 河北省 冀 石家庄
# 新疆 新 乌鲁木齐
# 甘肃省 甘 兰州
# 青海省 青 西宁
# 陕西省 陕 西安
# 宁夏 宁 银川
# 河南省 豫 郑州
# 山东省 鲁 济南
# 山西省 晋 太原
# 安徽省 皖 合肥
# 湖北省 鄂 武汉
# 湖南省 湘 长沙
# 江苏省 苏 南京
# 四川省 川 成都
# 贵州省 黔 贵阳
# 云南省 滇 昆明
# 广西省 桂 南宁
# 西藏 藏 拉萨
# 浙江省 浙 杭州
# 江西省 赣 南昌
# 广东省 粤 广州
# 福建省 闽 福州
# 台湾省 台 台北
# 海南省 琼 海口
# 香港 港 香港
# 澳门 澳 澳门
#运行出错，吧上面的数据复制一下即可。

#把剪切板上的数据用正则表达式提取出来并保存到字典中。
import re,pyperclip
str1 = pyperclip.paste()
content = re.findall(r'[^\r\n]+',str1)
content
province,city = [],[]
dict1 = {}
for i in content:
    list1 = i.split(' ')
    province.append(list1[0])
    city.append(list1[2])
    dict1[list1[0]] = list1[2]
#循环35次，每次循环即创建一份试卷。
for quizNum in range(35):
        #创建测验文件和答案文件。
        quizfile = open('Text{}.txt'.format(quizNum+1),'w')
        answerfile = open('Text{}answers.txt'.format(quizNum+1),'w')
        #填写测验文件的标题，表头。
        quizfile.write('姓名:\n\nDate:\n\nPeriod:\n\n'+
                        '省会城市测验{}'.format(quizNum+1).center(80,' ')+'\n\n')
        #打乱问题的次序。
        Province = list(dict1.keys())
        import random
        random.shuffle(Province)
        for j in range(34):
                correctanswer = dict1[Province[j]]
                wronganswer = list(dict1.values())
                del wronganswer[wronganswer.index(correctanswer)]
                wronganswer = random.sample(wronganswer,3)
                #random.simple(list,Num),从列表中随机选取Num个项
                #组成新的列表,不改变原来的列表。
                #将正确答案与错误答案组成答案选项列表并打乱顺序。
                answeroptions = wronganswer+[correctanswer]
                random.shuffle(answeroptions)
                quizfile.write('\n{}.{}的省会是？'.format(j+1,Province[j])+'\n')
                for i in range(4):
                        quizfile.write('  {}.{}'.format('ABCD'[i],answeroptions[i])+'\n')
                answerfile.write('{}.{}'.format(j+1,'ABCD'[answeroptions.index(correctanswer)])+'\n')
        #一定要记得关闭文件！！！                
        answerfile.close()
        quizfile.close()
