s = float (input("Insira o salário ==> "))
if s > 8000:
    ir = s * 0.27
elif s > 5000:
    ir = s * 0.075
else:
    ir = 0
sf = s - ir
print((f"Salário: R$ {s}; Imposto: R$ {ir}; Salário final: R$ {sf}"))



