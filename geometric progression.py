import math


def print_series(a, n, r):
    for i in range(0, n):
        curr_term = a * pow(r, i)
        print(curr_term, end=" ")


a = int(input("Please Enter the starting of an G.P Series: : "))
n = int(input("Please Enter the no of terms in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio of G.P Series : "))
total = (a * (1 - math.pow(r, n))) / (1 - r)
print("\nThe Sum of Geometric Progression Series = ", total)
print_series(a, n, r)

