# @Time : 2022/1/23 21:32 
# @Author : Jface 
# @desc :

"""
需求：1.用户注册 2.用户登录
用户1：{"name": "rose", "pwd": "123"}
用户2:{"name": "mike", "pwd": "456"}

用户管理是列表：
user_list = [{"name": "rose", "pwd": "123"}, {"name": "mike", "pwd": "456"}]
"""

"""
# 1. 注册功能，新增加一个用户
# 1.1 用户信息
# 1.2 创建一个字典
# 1.3 追加字典到列表中
"""


"""
# 2. 判断某个用户，是否在列表中
# 2.1 需要找的用户
# 2.2 通过for遍历列表，取出的每个元素是字典
    # 2.3 字典['name']和reg_name比较是否相等
        # 2.4 如果相等，打印提示名字在列表中
        # 2.5 跳出循环
# 2.6 for循环的else，循环里面没有执行到break，则会执行else
    # 2.7 打印，名字不在列表中
"""

# 3. 登陆功能：和上面流程差不多，同时判断用户名和密码是否相等
