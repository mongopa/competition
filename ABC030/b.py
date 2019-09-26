n, m = map(int, input().split())

s = 360 / 12 * (n + m / 60) % 360
l = 360 / 60 * m
diff = abs(s - l)
print(min(diff, 360 - diff))