# Напишите программу, которая принимает на вход координаты точки(X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка(или на какой оси она находится).


x = int (input('Enter the coordinates of the point along the axis X: '))
y = int (input('Enter the coordinates of the point along the axis Y: '))
if x !=0 and y !=0:
    if x > 0 and y > 0:
        print ('1st quater')
    elif x < 0 and y > 0:
        print ('2nd quarter')
    elif x < 0 and y < 0:
        print('3th quarter')
    elif x > 0 and y < 0: 
        print('4th quarter')
else:
    print ('The point is at the inersection of the axes')
