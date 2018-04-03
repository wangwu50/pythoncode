def counting_sort(A, B, k):
    C = [0] * k
    for j in range(0, len(A) - 1):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1


if __name__ == '__main__':
    counting_sort([], [], 2)
