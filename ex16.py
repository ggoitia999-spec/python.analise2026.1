A = int (input("Valor 1 => "))
B = int (input("Valor 2 => "))
C = int (input("Valor 3 => "))
if A > B and A > C:
   print(f"{A} é maior que {B} e {C}")
elif B > A and B > C: 
    print (f"{B} é maior que {A} e {C}")
else:
    print(f"{C} é maior que {B} e {A}") 