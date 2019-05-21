cdef extern from "c_fib.c":
    int c_fib(int n)

def fib(n):
    return c_fib(n)
