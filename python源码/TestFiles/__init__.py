#这个__init__.py文件作用是使TextFiles文件夹下的python
#文件之间能相互调用。
def p():
    print('hello world')
p = 2
__all__ = ['p']