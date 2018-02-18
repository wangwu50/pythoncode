class Heap(list):
    def __init__(self, *nums):
        self.append(None)
        for n in nums:
            self.append(n)
        self.heap_size = len(self) - 1

    def __str__(self):
        return self[1:].__str__()


def max_imum(A):
    return A[1]


def extract_max(A):
    if A.heap_size < 1:
        print('heap underflow')
        return
    max_num = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    max_heapify(A, 1)
    return max_num


def increase_key(A, i, key):
    if key < A[i]:
        print("new key is smaller than current key")
        return
    A[i] = key
    while i > 1 and A[parent(i) < A[i]]:
        exchange(A, i, parent(i))
        i = parent(i)


def insert(A: Heap, key):
    A.heap_size = A.heap_size + 1
    A.append(float('-inf'))
    increase_key(A, A.heap_size, key)


def parent(i):
    return int(i / 2)


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def exchange(A, i, j):
    A[i], A[j] = A[j], A[i]


def min_heapify(A: Heap, i: int):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        exchange(A, i, smallest)
        min_heapify(A, smallest)


def max_heapify(A: Heap, i: int):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange(A, i, largest)
        max_heapify(A, largest)


def build_min_heap(A: Heap):
    A.length = A.heap_size
    for i in range(int(A.length / 2), 0, -1):
        min_heapify(A, i)


def build_max_heap(A: Heap):
    A.length = A.heap_size
    for i in range(int(A.length / 2), 0, -1):
        max_heapify(A, i)


def heap_sort(A: Heap):
    build_max_heap(A)
    A.length = A.heap_size
    for i in range(A.length, 1, -1):
        exchange(A, 1, i)
        A.heap_size = A.heap_size - 1
        max_heapify(A, 1)


def heap_sort2(A: Heap):
    build_min_heap(A)
    A.length = A.heap_size
    for i in range(A.length, 1, -1):
        exchange(A, 1, i)
        A.heap_size = A.heap_size - 1
        min_heapify(A, 1)


if __name__ == '__main__':
    a = Heap(2, 5, 6, 0, -3, 4, 3, 1)
    print(a)
    heap_sort2(a)
    print(a)
