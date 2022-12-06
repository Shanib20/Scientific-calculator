print("                 SCIENTIFIC CALCULATOR              ")

import math as m

def addition (a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
def square_root(a):
    return m.sqrt(a)
def power(a,b):
    return a**b
def sin(a):
    return m.sin(a)
def cos(a):
    return m.cos(a)
def tan(a):
    return m.tan(a)
def radian_to_degree(a):
    return m.degrees(a)
def degree_to_radian(a):
    return m.radians(a)



print('''
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Modulus
6. Square_root
7. Power
8. Sin
9. Cos
10. Tan
11. Radian_to_degree
12. Degree_to_radian
''')
print("ONLY CHOOSE THE GIVEN OPERATIONS ONLY")
print()
option=eval(input('Choose the operator:  '))

   
while option <=12:
    if option==1:
        print("****addition operator****")
        n1=eval(input('Enter first number:'))
        n2=eval(input('Enter second number:'))
        result=addition(n1,n2)
        print('The addition of {} and {} is {}'.format(n1,n2,result))
    elif option==2:
        print("****substraction operator****")
        n1=eval(input('Enter first number:'))
        n2=eval(input('Enter second number:'))
        result=substraction(n1,n2)
        print('The substraction of {} and {} is {}'.format(n1,n2,result))
    elif option==3:
        print("****multiplication operator****")
        n1=eval(input('Enter first number:'))
        n2=eval(input('Enter second number:'))
        result=multiplication(n1,n2)
        print('The multiplication of {} and {} is {}'.format(n1,n2,result))
    elif option==4:
        print("****division operator****")
        n1=eval(input('Enter first number:'))
        n2=eval(input('Enter second number:'))
        result=division(n1,n2)
        print('The division of {} and {} is {}'.format(n1,n2,result))
    elif option==5:
        print("****Modulus operator****")
        n1=eval(input('Enter first number:'))
        n2=eval(input('Enter second number:'))
        result=modulus(n1,n2)
        print('The modulus of {} and {} is {}'.format(n1,n2,result))
    elif option==6:
        print("****square_root operator****")
        n1=eval(input('Enter the number:'))
        result=square_root(n1)
        print('The square_root of {} is {}'.format(n1,result))
    elif option==7:
        print("****power operator****")
        n1=eval(input('Enter first number:'))
        n2=eval(input('Enter second number:'))
        result=power(n1,n2)
        print('The power of {} and {} is {}'.format(n1,n2,result))
    elif option==8:
        print("****Sine operator****")
        n1=eval(input('Enter the number:'))
        result=sin(n1)
        print('The sine value  of {} is {}'.format(n1,result))
    elif option==9:
        print('****cosine Operator****')
        n1=eval(input('Enter the number:'))
        result=cos(n1)
        print('The cosine value  of {} is {}'.format(n1,result))
    elif option==10:
        print('****Tan Operator****')
        n1=eval(input('Enter the number:'))
        result=tan(n1)
        print('The tan value  of {} is {}'.format(n1,result))
    elif option==11:
        print('****Radian_to_degree Operator****')
        n1=eval(input('Enter the number:'))
        result=radian_to_degree(n1)
        print('The degree value  of {} is {}'.format(n1,result))
    elif option==12:
        print('****Degree_to_radian Operator****' )
        n1=eval(input('Enter the number:'))
        result=degree_to_radian(n1)
        print("The Radian value of {} is {}".format(n1,result))
    else:
        print("Invalid Entry")
    print()
    new_option=eval(input('*Press one(1) to continue       *Press zero to exit(0)'))
    if new_option==1:
        option=eval(input('choose the operator:  '))
    else:
        print("thankyou")
        break
        
    
        

    























