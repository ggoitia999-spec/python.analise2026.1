N1=float (input(f"Insira a primeira nota =>"))
N2=float (input(f"Insira a segunda nota => "))
N3=float (input(f"Insira a terceira nota => "))
M= (N1+N2+N3)/3
print(f"A média entre as notas é de => {M}")
if M >= 6:
    print("APROVADO")
else:
    print("RECUPERAÇÃO")
