#Condicionales
'''3.	Los ángulos se clasifican de la siguiente manera: nulo (0°), Agudo (0°< x < 90°), Recto (90°), 
Obtuso (90° < x <180°), Llano (180°), Cóncavo (180°< x < 360°), Completo (360°). 
Desarrolle el programa que determine la clasificación de un ángulo dado en grados.'''


angulo =  int(input("INGRESE EL ÁNGULO: "))

if angulo == 0:
    print("ANGULO NULO!")

if angulo == 90:
    print("ANGULO RECTO!")

if angulo == 360:
    print("ANGULO COMPLETO!")

if angulo == 180:
    print("ANGULO LLANO!")

if 0 < angulo < 90:
    print("ANGULO AGUDO!")

if 90 < angulo < 180:
    print("ANGULO OBTUSO!")

if 180 < angulo < 360:
    print("ANGULO CÓNCAVO")
