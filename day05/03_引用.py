# @Time : 2022/1/26 22:53 
# @Author : Jface 
# @desc :
"""
1. 引用：是一个变量或值的另一个名字，又称别名
2. id(变量名或值)：查看变量或值的引用地址
3. 引用地址相等，说明指向同一个内存空间
"""

a = 10  # a 是 10 的别名，引用
print(id(a), id(10))
b = a  # b 是 a 的别名，引用
print(id(a), id(b), id(10))
