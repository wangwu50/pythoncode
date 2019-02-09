# 动态规划 切割钢条问题： p代表价格，n代表总长度。求解怎么切分利润最大


def init():
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 40]


def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-Inf')
    for i in range(1, n):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    r = [float('-Inf')] * n
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-Inf')
        for i in range(1, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    r = []
    r[0] = 0
    for j in range(1, n):
        q = float('-Inf')
        for i in range(1, j):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    r = []
    s = []
    r[0] = 0
    for j in range(1, n):
        q = float['-Inf']
        for i in range(1, j):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
            r[j] = q
    return r, s


# 100个台阶，每次可以走一步或者两步，问共有多少种走法
# s[100] = s[99]+s[98]
#
# s[1] = 1
# s[2] = 2
# s[n] = s[n-1] + s[n-2]


def find_step(n):
    s = [float('-Inf')] * (n + 1)
    return find_step_aux(n, s)


def find_step_aux(n, s):
    if s[n] > 0:
        return s[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    s[n] = find_step_aux(n - 1, s) + find_step_aux(n - 2, s)
    return s[n]


def bottom_up_find_step(n):
    s = [float('-Inf')] * (n + 1)
    s[1] = 1
    s[2] = 2
    for j in range(3, n + 1):
        s[j] = s[j - 1] + s[j - 2]
    return s[n]


if __name__ == '__main__':
    i = find_step(100)
    print(i)
    j = bottom_up_find_step(100)
    print(j)
