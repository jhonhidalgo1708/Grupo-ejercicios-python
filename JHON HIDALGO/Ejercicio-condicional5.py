#CONDICIONALES

'''5.	Desarrolle el programa que dado un número de 4 cifras, forme el mayor número posible de dos cifras 
usando la mayor y menor cifra del número ingresado'''

#Ejercicio 5 de condicionales

numero = input("COLOQUE NUMERO DE 4 CIFRAS: ")

if len(numero) !=4:
    print("ERROR!!!!!, EL NUMERO DEBE SER DE 4 CIFRAS")

else:
    cifra_MENOR = 10
    cifra_MAYOR = 0

    for cifra in numero:
        if (int(cifra) < cifra_MENOR):
            cifra_MENOR = int(cifra);

        elif (int(cifra) > cifra_MAYOR):
            cifra_MAYOR = int(cifra);
    
    print(f"MAYOR NUMERO POSIBLE ES: {str(cifra_MAYOR)}{str(cifra_MENOR)}");
    
        