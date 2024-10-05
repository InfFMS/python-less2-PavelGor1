x1 = int(input())
x2 = int(input())
a1 = int(input())
a2 = int(input())
if x1<a1<x2 and x2<a2:
    print(a1,x2)
elif a1<x1 and x2>a2:
    print(x1,a2)
elif a1 == x2:
    print(a1)
elif a2 == x1:
    print(x1)
elif x2<a1 or a2<x1:
    print("Пустое множество")
