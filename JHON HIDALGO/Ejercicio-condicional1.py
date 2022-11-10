# CONDICIONALES

'''Una tienda vende un producto a precios unitarios que dependen de la cantidad de unidades adquiridas. 
Adicionalmente, si el cliente adquiere más de 50 unidades la tienda le descuenta el 15% del importe de la compra; 
en caso contrario, sólo le descuenta el 5%. Desarrolle el programa que determine el importe de la compra, 
el descuento y el total a pagar por la compra de cierta cantidad de unidades del producto. 
1 a 25 unidades (S/. 27), 26 a 50 unidades (S/. 25), 51 en adelante unidades (S/. 23)'''


unidades = int(input("ingrese la cantidad de unidades: "))

#Calculo del importe de la compra

if (unidades>=1 and unidades <=25):
    precio = 27 * unidades
if (unidades>=26 and unidades <=50):
    precio = 25 * unidades 
if (unidades>=51):
    precio = 23 * unidades
    
#Calcular el importe de descuento
if (unidades > 50):
    descuento = 0.15 * precio
if (unidades <= 50):
    descuento = 0.05 * precio

#Calcular el importe a pagar
pagar = precio - descuento  

#Salida de Resultados

print("Importe de la Compra:",precio)
print("Importe de Descuento:",descuento)
print("Importe a Pagar:",pagar)
    
