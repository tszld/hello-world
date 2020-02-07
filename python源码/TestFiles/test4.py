'''
三阶行列式计算器
'''
import random
a = []
for i in range(1,10):
        a.append(random.randint(0,15))
        if i in [4,7]:
                print(' ')
                print('{} '.format(a[i-1]),end = '')
        else:
                print('{} '.format(a[i-1]),end = '')
b = [0,4,8,1,5,6,2,3,7,6,4,2,7,5,0,8,3,1]
result = a[0]*a[4]*a[8]+a[1]*a[5]*a[6]+a[2]*a[3]*a[7]-a[6]*a[4]*a[2]-a[7]*a[5]*a[0]-a[8]*a[3]*a[1]
print(result)