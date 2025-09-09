a = int(input())

for _ in range(a):
    b, c = map(int, input().split())
    vet = list(map(int, input().split()))
    vet = sorted(vet)
    
    cont = 0
    
    
    for i in range(b-1, -1, -1):
        if (c):
            cont += vet[i] * c
            c -= 1
        
        else:
            break
        
        
    print(cont)
    
    