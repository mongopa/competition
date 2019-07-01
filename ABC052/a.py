a, b, c, d = map(int, input().split())
ab = a * b
cd = c * d
print(ab if ab > cd else cd)