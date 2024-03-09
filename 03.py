
#3 a) 1, 3, 5, 7, ___  
#resposta 9
print('3a.: ', end='')
num = 1
while (num < 30):
    print(num, end=' ')
    num += 2

#3 b) 2, 4, 8, 16, 32, 64, ____
#resposta 128
print('\n3b.: ', end='')
num = 1
while (num < 5):
    print(num, end=' ')
    num += num

#3 c. 0, 1, 4, 9, 16, 25, 36, ____  
#resposta 49
print('\n3c.: ', end='')
num = 0
soma = 1
while (num < 100):
    print(num, end=' ')
    num += soma
    soma += 2
    

#3 d) 4, 16, 36, 64, ____  
#resposta 100
print('\n3d.: ', end='')
num = 1
while (num < 7):
    print((4 * num) * num, end=' ')
    num += 1

#3 e) 1, 1, 2, 3, 5, 8, ____  
#resposta 13
print('\n3e.: ', end='')
num = 0
num2 = 1
while (num2 < 30):
    temp = num2
    num2 += num
    num = temp
    print(num, end=' ')


#3 f) 2,10, 12, 16, 17, 18, 19, ____  
#resposta 
print('\n3f.: ', end='')
num = 0
i = 2
divisor = 20
for i in range(1, 10):
    
    if(i % 2 == 0):
        num  = (divisor / i) + 1
    else:
        num  = (divisor / i) + 1
    print( int( num / 2) , end=' ')

