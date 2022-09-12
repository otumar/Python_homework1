# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('Enter the X value for the first point: '))
y1 = int(input('Enter the Y value for the first point: '))

x2 = int(input('Enter the X value for the second point: '))
y2 = int(input('Enter the Y value for the second point: '))

a = (x2 - x1) * (x2 - x1)
b = (y2 - y1) * (y2 - y1)
c = round ((a + b) ** 0.5, 3)
print (f'The distance between points is: {c}')