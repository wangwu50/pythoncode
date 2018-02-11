class Heap(list):
    def __init__(self, *nums):
        for n in nums:
            self.append(n)

    def heap_size(self):
        return len(self)


def parent(i):
    return i / 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def exchange(A, i, j):
    A[i], A[j] = A[j], A[i]


def max_heapify(A: Heap, i: int):
    l = left(i)
    r = right(i)
    if l <= A.heap_size() and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size() and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange(A, i, largest)
        max_heapify(A, largest)


def build_max_heap(A: Heap):
    A.length = A.heap_size()
    for i in range(A.length / 2, 0, -1):
        max_heapify(A, i)


a = Heap(1, 2, 3, 4, 5)
print(a.heap_size())
exchange(a, 1, 2)
print(a)
