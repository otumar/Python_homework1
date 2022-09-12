# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
a = int (input ("Enter a number from 1 to 7: "))
if 1 <= a <=7:
    print(list[a-1])
    if a == 6 or a ==7:
        print ("It's a day off")
    else:
        print ("It's a working day")
else:
    print ("Your number is incorrect")