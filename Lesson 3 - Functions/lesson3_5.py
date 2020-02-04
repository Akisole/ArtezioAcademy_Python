"""Напишите функцию, которая будет принимать ввод пользовательской строки.
В строке 1 или более отрицательных/положительных чисел.
Функция должна вернуть ближайшее к нулю значение."""

# def f():
#     str = input()
#     diff = ''
#
#     space = str.find(' ')
#     while space != -1:
#         a = float(str[:space + 1])
#         if diff == '':
#             diff = a
#         elif abs(a) < abs(diff):
#             diff = a
#         s = str[space + 1:]
#         space = str.find(' ')
#     if abs(float(str)) < abs(diff):
#         diff = float(s)
#     print(diff)

def f():
 s=input();d='';p=s.find(' ')
 while p!=-1:
  a = float(s[:p+1])
  if d=='':d=a
  elif abs(a)<abs(d):d=a
  s=s[p+1:];p=s.find(' ')
 if abs(float(s))<abs(d):d=float(s);
 print(d)

f()
