V = float (input("Digite o valor => "))
if V >= 500:
    D = 0.20
elif V <= 100:
    D = 0.10
else:
    D = 0.15
VD = V-(V*D)
print (f"O valor com desconto é => {VD}")
