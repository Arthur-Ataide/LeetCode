n = int(input())

vet = map(int, input().split())
vet = list(vet)
vet = sorted(vet)
pd = [0 for i in range(n)]
vet = vet[::-1]

if n == 1:
    print(1)

else:

    for i in range(n):
        maior = 1
        for j in range(0, i):
            if vet[j] % vet[i] == 0:
                maior = max(maior, pd[j]+1)
        
        pd[i] = maior
        
    maior = max(pd)
    print(maior)
