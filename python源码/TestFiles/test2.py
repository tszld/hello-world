'''
CensusPopData:

将test2.xlsx中的人口普查数据做成一个字典并写入模块中，使得运行该模块
并给州县之类的参数，即可获得该县的人口数即普查区数目。
'''
import openpyxl,pprint
wb = openpyxl.load_workbook('''D:\\TheThirdFiles\\censuspopdata.xlsx''')
sheet = wb['Population by Census Tract']
countydata = {}
for i in range(2,sheet.max_row+1):
    state = sheet['B'+str(i)].value
    county = sheet['C'+str(i)].value
    pop = sheet['D'+str(i)].value
    countydata.setdefault(state,{})
    countydata[state].setdefault(county,{'pop':0,'tracts':0})
    countydata[state][county]['pop'] += int(pop)
    countydata[state][county]['tracts'] += 1
resultfile = open('census2010.py','w')
resultfile.write('alldata =' + pprint.pformat(countydata))
resultfile.close()