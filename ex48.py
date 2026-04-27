def maior(x, y):
    if x > y:
        return x
    else:
        return y
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
print (f"O maior numero é: {maior(numero1, numero2)} ")