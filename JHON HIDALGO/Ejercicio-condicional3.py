#Condicionales
'''3.	Los ángulos se clasifican de la siguiente manera: nulo (0°), Agudo (0°< x < 90°), Recto (90°), 
Obtuso (90° < x <180°), Llano (180°), Cóncavo (180°< x < 360°), Completo (360°). 
Desarrolle el programa que determine la clasificación de un ángulo dado en grados.'''


med_angulo =  int(input("INGRESE EL ÁNGULO EN GRADOS: "))

if med_angulo == 0:
    print("ES ANGULO NULO!")

if med_angulo == 90:
    print("ES ANGULO RECTO!")

if med_angulo == 360:
    print("ES ANGULO COMPLETO!")

if med_angulo == 180:
    print("ES ANGULO LLANO!")

if 0 < med_angulo < 90:
    print("ES ANGULO AGUDO!")

if 90 < med_angulo < 180:
    print("ES ANGULO OBTUSO!")

if 180 < med_angulo < 360:
    print("ANGULO CÓNCAVO!")
