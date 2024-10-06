num = 22
try:
    if num % 2 == 0:
        raise Exception("Erro lançado")
    print("numero é impar", num)

except:
    print("numero é par", num)