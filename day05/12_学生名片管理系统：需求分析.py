# @Time : 2022/1/27 22:52 
# @Author : Jface 
# @desc :
"""
【应用】学生名片管理系统：存用户的基本信息（姓名、年龄、电话）
1. 如何存一个用户的信息：
    user_dict = {"name": "rose", "age": 18, "tel": "123"}
2. 如果管理存储多个用户：
    user_list = [{}, {}]
3. 增加学生：
    1 用户输入
        1.2 判断用户是否存在, 如果存在就不添加
    2 创建字典
    3 追加到列表中
4. 查找显示所有的用户信息：
    1. 使用enumerate遍历列表获取每一个学生的字典和序号

5. 查找某个用户
    1. 输入需要查询的用户姓名
    2. 遍历列表获取每一个学生的字典
    3. 使用user_dict['name']判断是否找到
    4. 显示学生信息

6. 修改用户
    1. 输入需要修改的用户姓名
    2. 遍历列表获取每一个学生的字典
    3. 使用user_dict['name']判断是否找到
    4. 输入修改后的学生信息
    5. 修改列表中的字典

7. 删除用户
    7.0 输入需要删除的用户姓名
    7.1 遍历列表找到需要删除用户所在位置的 num
    7.2 删除元素
        del user_list[num]
"""