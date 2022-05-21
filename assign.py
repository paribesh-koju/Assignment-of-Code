'''
a = 5
b = 4
if a == b:
    print('1')
elif a>b:
    print('2')
else:
    print('3')
'''

'''
a = 'pari'
b = 'besh'
c = 'koju'
d = 'koju'
if a == b and c == d:
    print('Hello')
else:
    print("invalid entry")
'''

'''
a = 'mobile'
b = 'laptop'
c = 'earpod'
d = 'earpod'
if a == b or c == d:
    print('Hello')
else:
    print('Does not exist')
'''

'''
x = 23
if x > 0:
    print('True')
elif x < 0:
    print('False')
else:
    print('Zero')
'''

'''
x = int(input('Enter the number:\n'))
if x % 2 == 0:
    print('It is even number')
else:
    print('It is odd number')
'''
'''
print('Enter the marks of four Subject:\n')
Maths = float(input('Enter the marks of Maths:\n'))
Science = float(input('Enter the marks of science:\n'))
Social = float(input('Enter the marks of social:\n'))
English = float(input('Enter the marks of english:\n'))


WAP = Maths + Science + Social + English

Percentage = ( WAP / 400 ) * 100

if Percentage >= 70:
    print('\tDistinction')
    Grade = 'A'
elif Percentage >= 60:
    print('\tfirst division')
    Grade = 'B'
elif Percentage >= 40:
    print('\tPass')
    Grade = 'C'
else:
    print('\tFail')
    Grade = 'E'

print('\nThe WAP Marks is:\t', WAP)
print('\nThe Percentage is:\t', Percentage)
print('\nThe Grade is:\t', Grade)
'''

'''
# What is the output of 'APPLE' > 'apple'??
print('APPLE'>'apple')
#False
'''
'''
print("\t\t\tPersonal details")
name = 'Paribesh koju'
age = 19
address = 'suryabinayak,bhaktapur'
print(name)
print(age)
print(address)
'''
 
'''
PI = 22/7
r = float(input('Enter the radius of the circle:(in m)\n '))
Area = PI * (r**r)
#print(f'The area of circle is {Area} m²')
print('The area of circle: \n %.2f' %Area, 'm²'
'''

'''
a = int(input('Enter the no of students in class a:\n'))
b = int(input('Enter the no of students in class b:\n'))
c = int(input('Enter the no of students in class c:\n'))
print('The possible no of desk that can be purchase is:')
print(a//2 + b//2 + c//2 + a%2 + b%2 + c%2)                 #snakify theorem
# '//' means floor division helps to find out the no of desk
# '%' means modulus helps to find out the reminder
# the final result of this code is find out the exact no of desk
'''

'''
x = int(input('Enter the number:\n'))
y = int(input('Enter the number:\n'))
z = int(input('Enter the number:\n'))
if x >= y <= z:
    print(y)
elif y >= x <= z:
    print(x) 
else:
    print(z) 
'''  

'''
m = int(input('Enter the number:\n'))
n = int(input('Enter the number:\n'))
o = int(input('Enter the number:\n'))
print(m + n + o)
'''

'''
x = int(input('Enter the hight of right angled tringle:\n'))
y = int(input('Enter the lenght of base:\n'))
print(x * y /2)
'''
'''
N = int(input('Number of students:\n'))
K = int(input('Number of Apples:\n'))
print(K // N)
# print(K // N) represent the no of apples got by the single students
print(K % N)
# print(K % N) represent the no of apples remain in the basket
'''

