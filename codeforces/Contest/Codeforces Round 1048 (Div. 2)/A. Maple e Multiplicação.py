a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    
    if c == b:
        print(0)
    
    elif c % b == 0 or b % c == 0:
        print(1)
    
    else:
        print(2)