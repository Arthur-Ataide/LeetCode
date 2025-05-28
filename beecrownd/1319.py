while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        exit()
        
    menor, maior = map(int, input().split())
    dic = {}

    dic[menor] = []
    dic[menor].append(maior)

    for i in range(n-1):
        a, b =map(int, input().split())
        menor = min(menor, a)
        maior = max(maior, b)
        
        if a not in dic:
            dic[a] = []
        dic[a].append(b)

    if menor == 0 and maior == m:
        cont = 1
        
        for i in range(m+1):
            if i not in dic:
                continue
                
            cont+= len(dic[i])-1
            valorMax = max(dic[i])
            
            if i > 0:
                if valorMax <= maior:
                    cont+=1
                else:
                    maior = valorMax
            
            else:    
                maior = valorMax

        print(cont)
    else:
        print(0)
