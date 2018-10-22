# 账单计算代码
lines = open("data.user.txt")
result = 0
for index, lin in enumerate(lines):
    list = lin.split()
    memory = int(list[6])
    instance = list[10]
    timestamp = list[11]
    if index == 0:
        before = int(timestamp)
    result = result + (int(timestamp) - before) * int(instance)*memory
    before = int(timestamp)
print(result)
print(result /1024/3600)