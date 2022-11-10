#Ejercicio 4 de condicionales

nota_a = float(input("Ingrese su primera nota: "))
nota_b = float(input("Ingrese su segunda nota: "))
nota_c = float(input("Ingrese su tercera nota: "))

if nota_c < 10:
    nota_c =+2

promedio = float((nota_a + nota_b + nota_c)/3)

print(promedio)

