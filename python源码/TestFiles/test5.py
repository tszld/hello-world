'''
杨辉三角
            [1]
            [1, 1]
            [1, 2, 1]
            [1, 3, 3, 1]
generator函数：
    将函数变作生成器，yield相当于return的作用，只不过有yield
    关键字则是生成器而非函数。
    generator的函数，在每次调用next()的时候执行，遇到yield
    语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
def triangles_1():
    S = [1]
    while True:
        yield S
        S = [1]+[S[i+1]+S[i] for i in range(len(S)-1)]+[1]
    
def triangles_2():
    S = [1,2,1]
    n = 2
    while True:
        n = n + 1
        if n<3:
            S = [1 for i in range(n)]
            yield S
        else:
            S =  [S[i-1]+S[i] for i in range(n) if i !=0 and i != n-1]
            S.insert(0,1)
            S.append(1)
            yield S
