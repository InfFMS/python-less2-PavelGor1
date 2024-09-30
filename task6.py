for n in range(100,999):
    one = n // 100
    two = (n // 10) % 10
    three = n % 10
    ans = one ** 3 + two ** 3 + three ** 3
    if ans==n:
        print(n)