#### Output

print("Calculadora.py")
print("Operadores")
print("==========================================")
y = int(input("Introducir el primer numero: "))
print("==========================================")
x = int(input("Introducir el segundo numero: "))
print("==========================================")

print("Selecciona una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
print("6. Logaritmo")

resultado = x, y
instruccion = int(input("Con que operador quieres (?) "))


if instruccion >= 7:
    print("Valor no valido.")
else:
    print("Puedes Seguir usando el programa. ")





