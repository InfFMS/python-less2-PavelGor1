age=int(input())
if (age > 4) and (age < 21):
  print('Вам ', age, ' лет.')
else:
  i = age % 10
  if i==1:
    print(age, ' год.')
  elif i < 5:
    print(age, ' года.')
  else:
    print(age, ' лет.')