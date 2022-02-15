#result = 0
#for n in range(5):
#    result = n + 4
#    if (result % 2) != 0:
#        print('-', end=' ')
#        continue
#    print(result, end=' ')
#print('done')


#a = int(input())
#b = int(input())
#c = int(input())
#result = 0
#while a < b:
#    result = a * 2
#    print(result)
#    if result > c:
#        break
#    a += 3


#stop = int(input())
#result = 0
#for a in range (4):
#    for b in range (5):
#        result += a + b
#    print(result)
#    if result > stop:
#        break


stop = int(input())
result = 0
for a in range (3):
    print(a, end=': ')
    for b in range (4):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()



