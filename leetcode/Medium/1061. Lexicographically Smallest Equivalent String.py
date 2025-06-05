s1 = "abcde"
s2 = "bcdef"
baseStr = "parser"
vet = []
dic = {}

tam = len(s1)

for i in range(tam):
    letra1 = s1[i]
    letra2 = s2[i]

    if letra1 != letra2:
        if letra1 not in dic:
            dic[letra1] = set()
        if letra2 not in dic:
            dic[letra2] = set()
        
        dic[letra1].add(letra2)
        dic[letra2].add(letra1)
        
        for letra in dic:
            if letra1 in dic[letra] or letra2 in dic[letra]:
                 dic[letra] |= dic[letra1]
                 dic[letra] |= dic[letra2]
                 dic[letra1] |= dic[letra]
                 dic[letra2] |= dic[letra]

for i in dic:
    print(i, min(dic[i]))
    

print(baseStr)