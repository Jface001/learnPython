# @Time : 2022/1/23 16:01 
# @Author : Jface 
# @desc : 跑步10圈，跑5圈后，不再跑了

# 1. 定义一个条件变量，一般赋值为0
i = 0
# 2. while 判断条件：
while i < 10:
    # 3. 满足条件的循环代码块
    print("跑了%d圈" % (i + 1))
    # 4. if 满足条件：
    if i == 4:
        # 4.1 打印提示信息：累了，结束战斗
        print("累了，结束战斗")
        # 4.2 break跳出循环
        break
    # 5. 条件变量的改变【非常重要】
    i += 1
print("循环外面")
