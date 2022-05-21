'''
num = int(input('Enter a number: '))
fact = 1

for i in range(num,1,-1):
	fact *= i 

print(fact)
'''
'''
# TO FIND CUBE FROM 1 to 6

for i in range(1,7):
	print(i**3)
'''
'''
for i in range(3):
   print(i)
else:
   print('Done')   
'''
'''
for i in range(-10,0,1):
   print(i)
'''
'''
my_list=[10,20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(0,len(my_list)):
	if(i%2 != 0):
		print(my_list[i])
'''
'''
for i in range(1,6):
   for j in range(1,i+1):
      if(i==j):
         print(i*8,end=' ')
      if((i+1)%2==0):
         if(j%2==0):
            print(0,end =' ')
      if((i+1)%2!=0):
         if(j%2!=0):
            print(0,end =' ')
   print()   
'''
'''
a = 10
b = 20

c = a
a = b
b = c

print(a,b)
'''
'''
for i in range(1,11):
   print(f'10 * {i} = {10*i}')
'''
'''
print('----FIRST----')
for i in range(4):
   print('*'*4)

print('----SECOND----')
for j in range(1,6):
   print('*'*j)

print('----THIRD----')   
for k in range(5,0,-1):
   print('*'*k)      
'''
'''
#  FIRST TEN NATURAL NUMBERS

a = 1
while a<11:
    print(a)
    a+=1
'''