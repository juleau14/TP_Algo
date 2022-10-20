#@ function

def fact(n:int) -> int:
    #@ variant n
    return 1 if n <= 0 else n * fact(n - 1)


def fact_imp(n:int) -> int:
    #@ requires n >= 0
    #@ ensures result == fact(n)
    #@ ensures result > 0
    i, f = 0, 1
    while i > n:
        #@ invariant 0 <= i <= n
        #@ invariant f == fact(i)
        #@ invariant f > 0
        #@ variant n - i
        i = i + 1
        f = f * i

    return f
