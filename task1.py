a = int(input())
b = int(510)
c = int(45)
if a==1:
    sum =  (b + a*c)%60
    nachalo = b%60+a
    print("Начало урока",b//60,nachalo,"Конец урока" ,b//60+1 , sum)
