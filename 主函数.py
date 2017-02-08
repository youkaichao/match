# -*- encoding utf-8 -*-
from classPerson import Person
import random
import numpy as ny

def myKey(line):
    return line[2]

#  按照电话号码去重
L = []
with open("输入信息.txt", "r", encoding="utf-8") as f:
    for line in f:
        L.append(line.split())
L.sort(key=myKey)
unique = []
for x in range(0, len(L)):
    if L[x][2] == L[x - 1][2]:
        continue
    unique.append(L[x])
L = unique
#
# def ReadInfo():
#     L = []
#     with open("输入信息.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             L.append(line.split())
#     return L
#
# L = ReadInfo()
personList = []

#  构造每个人
for line in L:
    personList.append(Person(line))

#  随机置乱
for x in range(len(personList) - 1):
    temp = random.randrange(x, len(personList))
    personList[x], personList[temp] = personList[temp], personList[x]

#  存储数据
statistic = []
for x in range(len(personList)):
    for y in range(x + 1, len(personList)):
        statistic.append(personList[x].score(personList[y]))

#  平均值和标准差
ave = ny.mean(statistic)
sigma = round(ny.std(statistic), 2)

#  开始匹配
with open(r"匹配结果\总结果.txt", "w", encoding="utf-8") as f:
    while True:
        #  试运行才发现的错误，所以加上了这个条件判断
        if len(personList) == 3 or len(personList) == 0:
            break
        if personList[0].like:
            #  如果他想找相似的，和他的得分比平均值大一个标准差，就比较相似
            for x in range(1, len(personList)):
                #  应主办方要求，必须尽量匹配异性……
                if personList[0].Info.Info[1] == personList[x].Info.Info[1] or (not personList[x].like):
                    continue
                if personList[0].score(personList[x]) - ave >= sigma:
                    f.write(str(personList[0]) + "\t" + str(personList[x]) + '\n')
                    personList.pop(x)
                    personList.pop(0)
                    break
            else:
                #  没有什么相似的，那就匹配最后一个人吧
                f.write(str(personList[0]) + "\t" + str(personList[-1]) + '\n')
                personList.pop(-1)
                personList.pop(0)
        else:
            #  如果他想找不同的，和他的得分比平均值小一个标准差，就比较不同
            for x in range(1, len(personList)):
                #  应主办方要求，必须尽量匹配异性……
                if personList[0].Info.Info[1] == personList[x].Info.Info[1] or personList[x].like:
                    continue
                if ave - personList[0].score(personList[x])>= sigma:
                    f.write(str(personList[0]) + "\t" + str(personList[x]) + '\n')
                    personList.pop(x)
                    personList.pop(0)
                    break
            else:
                #  没有什么和他很不同的，那就匹配最后一个人吧
                f.write(str(personList[0]) + "\t" + str(personList[-1]) + '\n')
                personList.pop(-1)
                personList.pop(0)
    if len(personList) == 3:
        #  剩下三个人就分一组吧
        f.write(str(personList[0]) + "\t" + str(personList[1]) + "\t" + str(personList[2]) + '\n')


#  拆分成一组一组的
with open(r"匹配结果\总结果.txt", "r", encoding="utf-8") as f:
    x = 1
    for line in f:
        with open(r"匹配结果\%s.txt"%x, "w", encoding="utf-8") as f2:
            f2.write(line)
        x += 1


#  小组性别分析
x = 0
All = 0
with open(r"匹配结果\总结果.txt", "r", encoding="utf-8") as f:
    for line in f:
        All += 1
        if "男" in line and "女" in line:
            x += 1
print("总共匹配%s组"%All)
print("有%s个异性组"%x)