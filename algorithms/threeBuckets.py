# 有三个容积分别为3升、5升、8升的水桶,其中容积为8升的水桶中装满了水,
# 容积为3升和容积为5升的水桶都是空的。三个水桶都没有刻度,
# 现在需要将大水桶中的8升水等分成两份,每份都是4升水,
# 附加条件是只能这三个水桶,不能借助其他辅助容器。

initial_bucket_state = [0, 0, 8]
# 水桶的初始状态
bucket_volume = [3, 5, 8]
# 每个水桶的对应的容积
from collections import deque

record = deque()
record.append(initial_bucket_state)


# 利用python的deque队列记录状态转移情况,初始化时加入水桶初始状态。deque是可以从头尾插入和删除的队列,在不指定大小时,为一个无边界的队列


def nextStateLawful(current_state, bucket_volume):
    next_action = [
        (from_, to_)
        for from_ in range(3) for to_ in range(3)
        if from_ != to_
           and current_state[from_] > 0
           and current_state[to_] < bucket_volume[to_]
    ]
    # 通过列表推导式获得下一动作的二元组构成的列表,由（倒出水的容器编号,倒入水的容器编号）组成。
    # 二重循环得到下一步的所有可能动作,然后通过
    ##1.倒入倒出不能为同一个2.倒出的捅中必须有水3.倒入的桶中不能为满 的条件判断是否合法
    for from_, to_ in next_action:
        # next_state = current_state #浅复制造成错误
        next_state = list(current_state)
        if current_state[from_] + current_state[to_] > bucket_volume[to_]:
            next_state[from_] -= (bucket_volume[to_] - current_state[to_])
            next_state[to_] = bucket_volume[to_]
        else:
            next_state[from_] = 0
            next_state[to_] = current_state[to_] + current_state[from_]
        yield next_state
        # 再由所有可能的合法动作得出所有的下一个状态,通过yield产生供其它函数调用。


num = 0
record_list = []


# 记录调试的变量：num表示总共实现方法数,record_list记录所有实现路径

def searchResult(record, bucket_volume=[3, 5, 8], final_bucket_state=[0, 4, 4]):
    global num,record_list
    current_state = record[-1]
    # 由record的末尾元素得到当前水桶状态
    next_state = nextStateLawful(current_state, bucket_volume)
    # 得到关于当前状态的下一状态的可迭代生成器,供下一步循环使用
    for state in next_state:
        # 遍历所有可能的下一状态
        if state not in record:
            # 保证当前状态没在以前出现过。如果状态已经出现还进行搜索就会形成状态环路,陷入死循环。
            record.append(state)
            # 添加新的状态到列表中
            if state == final_bucket_state:
                print(record)
                # 打印出可行方案
                # record_list.append(record)这样使用错误,导致加入列表的是record的引用,应该使用下面的式子来进行深复制,得到一个新的队列再加入列表。
                record_list.append(deque(record))
                num += 1
            else:
                searchResult(record, bucket_volume, final_bucket_state)
                # 不是最终状态则递归搜索
            record.pop()
            # 去除当前循环中添加的状态,进入下一个循环,关键步 d,第一次实现的时候遗漏了


if __name__ == '__main__':
    searchResult(record)
    # 开始
    print(num)
    # 打印所有方案的数量
    print(min([len(i) for i in record_list]))
    # 打印最短路径方案中的状态总数
