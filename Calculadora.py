print ("Calculadora: ")
num1 = float(input("Ingrese un numero: "))
operador = input("INgrese un operador (+, -, *, /): ")
num2 = float(input("Ingrese otro numero : "))
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: división por cero"
else:
    resultado = "Operador no válido"
print(f"{num1} {operador} {num2} = {resultado}")
