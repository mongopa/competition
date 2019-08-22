from fractions import Fraction
N = int(input())
li = list(map(int, input().split()))
A = 0
for i in range(N):
  A += Fraction(1, li[i])
print(A.denominator / A.numerator)