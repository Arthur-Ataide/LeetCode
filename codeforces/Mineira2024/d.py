n, l = map(int, input().split())

vet = map(int, input().split())
vet = list(vet)

vet = sorted(vet)

cont = 0
for leite in vet[::-1]:
    quant = (100-leite)
    if l >= quant:
        l-=quant
        cont+=1
    else:
        break

print(cont)