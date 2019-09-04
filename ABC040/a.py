n, x = map(int, input().split())
dif_start = x - 1
dif_end = n - x
print(dif_start if dif_start <= dif_end else dif_end)