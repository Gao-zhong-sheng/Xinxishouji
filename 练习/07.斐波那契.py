n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print("1"    "1")
else:
    s = 0
    for i in range(3, n + 1):
        a = (i - 1) + (i - 2)
        s+=1
        print(f"1    1    {a}\t")


