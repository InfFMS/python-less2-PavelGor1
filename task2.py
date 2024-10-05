a = int(input())
if 3<=a<=5:
    print('Весна')
elif 5<a<=8:
    print('Лето')
elif 8<a<=11:
    print('Осень')
elif a<0 or a>12:
    print('Неверный номер месяца')
else:
    print('Зима')