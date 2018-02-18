import random


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i + 1, r)
    return i + 1


def partition2(A, p, r):
    x = A[r]
    i = p
    j = r - 1
    while True:
        while A[i] < x:
            if i == r:
                break
            i = i + 1
        while A[j] > x:
            if j == p:
                break
            j = j - 1
        if i >= j:
            break
        exchange(A, i, j)
    exchange(A, i, r)
    return i


def exchange(A, i, j):
    if i == j:
        return
    A[i], A[j] = A[j], A[i]


def quick_sort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def quick_sort2(A, p, r):
    if p < r:
        q = partition2(A, p, r)
        quick_sort2(A, p, q - 1)
        quick_sort2(A, q + 1, r)


def randomized_partition(A, p, r):
    i = random.randrange(p, r + 1)
    exchange(A, r, i)
    return partition(A, p, r)


if __name__ == '__main__':
    A = [13, 19, 9, 5, 12, 8, 10, 7, 4, 21, 2, 6, 11]
    quick_sort(A, 0, len(A) - 1)
    print(A)
