#Requirements:-
# 1) Dividing bigger problem into smaller problems.
# 2) Base condition with simple answer
# 3) Return or roll back answer for base condition to solve all sub problems.

# eg Summation of natural nos upto N.

def find_sum(n):
    if n == 1:
        return 1

    return n + find_sum(n-1)

# eg 2 : fibonacci sequence
def fibbonaci(n):
    if n ==1:
        return 0
    if n == 2:
        return 1

    return fibbonaci(n-1) + fibbonaci(n-2)
