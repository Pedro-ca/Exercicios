peso = float(input('me dê a massa do peixe '))

limite = 50
multa_por_kg = 4.00

if peso > limite: 
    execesso = peso - limite
    multa = execesso * multa_por_kg
else:
    multa = 0
    execesso = 0

print(f"Peso total: {peso:.2f} kg")
print(f"Excesso: {execesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")
