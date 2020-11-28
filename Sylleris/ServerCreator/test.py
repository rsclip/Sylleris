a = [i for i in range(1, 50)]

s = True
for num in a:
    s = not s
    if s:
        print(num)
