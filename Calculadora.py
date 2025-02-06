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

instruccion = int(input("Con que operador quieres (?) "))


if instruccion >= 7:
    print("Valor no valido.")
else:
    print("Puedes Seguir usando el programa. ")

if instruccion == 1:
    y + x
    print("El Valor es: ", x + y)

if instruccion == 2:
    y - x
    print(x - y)
if instruccion == 3:
    y * x
    print("El valor es: ", y * x)
if instruccion == 4:
    y / x
    print("El valor es: ", y / x)
if instruccion == 5:
    y ** x 
    print("El valor es: ", y ** x)
    