# @Time : 2022/1/23 16:04 
# @Author : Jface 
# @desc : 跑步10圈，到第5圈休息一下，第6圈继续

# 1. 定义一个条件变量，一般赋值为0
i = 0
# 2. while 判断条件：
while i < 10:
    # 3. if 满足条件：
    if i == 4:
        # 3.1 打印：累了，休息1圈
        print("累了，休息1圈")
        # 3.2 条件变量的改变【非常重要】，如果没有，导致死循环
        i += 1
        # 3.3 continue跳过本次循环
        continue
    # 4. 打印跑步第几圈
    print("打印跑步第%d圈" % (i + 1))
    # 5. 条件变量的改变【非常重要】
    i += 1
print("循环外面")
