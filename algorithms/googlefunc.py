# coding=utf-8
# 问题：有一个由字符组成的等式。WWWDOT-GOOGLE=DOTCOM，每个字符代表一个0~9之间的数字，
# WWWDOT、GOOGLE和DOTCOM都是合法的数字，不能以0开头。
# 请找出一组字符和数字的对应关系，使它们互相替换，并且替换后的数字能够满足等式。
# 解答：
# 777589-188103=589486
# 777589-188106=589483
import time

USE_MY_ISVALUE = 1

# 字符，数字，是否是数字的最高位
char_item = [
    ['W', -1, True], ['D', -1, True], ['O', -1, True],
    ['T', -1, True], ['G', -1, True], ['L', -1, True],
    ['E', -1, True], ['C', -1, True], ['M', -1, True]
]

char_value = [
    [0, False], [1, False], [2, False], [3, False], [4, False],
    [5, False], [6, False], [7, False], [8, False], [9, False]
]


def IsValueVaild(ciItem, cvItem):
    if cvItem[0] == 0:
        if USE_MY_ISVALUE:
            if ciItem[0] == 'W' or ciItem[0] == 'D' or ciItem[0] == 'G':
                return False
        else:
            return not ciItem[2]
    return not cvItem[1]


def MakeIntegerValue(ci, string):
    strLen = len(string)
    res = 0
    for i in range(0, strLen, 1):
        for item in ci:
            if string[i] == item[0]:
                res *= 10
                res += item[1]
    return res


def OnCharListReady(ci):
    minuend = 'WWWDOT'
    subtrahead = 'GOOGLE'
    diff = 'DOTCOM'
    m = MakeIntegerValue(ci, minuend)
    s = MakeIntegerValue(ci, subtrahead)
    d = MakeIntegerValue(ci, diff)
    if (m - s) == d:
        print(str(m) + "-" + str(s) + "=" + str(d))


def SearchResult(ci, cv, index, callback):
    max_char_count = len(ci)
    max_number_count = len(cv)
    if index == max_char_count:
        callback(ci)
        return
    for i in range(0, max_number_count, 1):
        if IsValueVaild(ci[index], cv[i]):
            cv[i][1] = True  # 设置使用标志
            ci[index][1] = cv[i][0]
            SearchResult(ci, cv, index + 1, callback)
            cv[i][1] = False  # 清除使用标志


if __name__ == '__main__':
    print("有一个由字符组成的等式。WWWDOT-GOOGLE=DOTCOM，每个字符代表一个0~9之间的数字，"
          "WWWDOT、GOOGLE和DOTCOM都是合法的数字，不能以0开头。"
          "请找出一组字符和数字的对应关系，使它们互相替换，并且替换后的数字能够满足等式。")
    print("解答：")
    start = time.clock()
    SearchResult(char_item, char_value, 0, OnCharListReady)
    end = time.clock()
    print("使用了: %f s" % (end - start))
