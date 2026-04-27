def par_impar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("Digite um numero: "))
result = par_impar(numero)
print(f"O numero {numero} é {result}")
    