import sys
num = int(sys.argv[1])
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=' ')
