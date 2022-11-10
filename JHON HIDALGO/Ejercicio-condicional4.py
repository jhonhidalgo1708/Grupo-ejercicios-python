#Condicionales

'''4.	El promedio final de un curso se obtiene en base al promedio simple de tres prácticas calificadas. 
Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota de la tercera 
práctica calificada, si es que esta no es menor que 10. Desarrolle el programa que determine el promedio final de un
alumno conociendo sus tres notas. '''


NOTA_1 = float(input("COLOQUE EL VALOR DE SU 1RA NOTA: "))
NOTA_2 = float(input("COLOQUE EL VALOR DE SU 2DA NOTA: "))
NOTA_3 = float(input("COLOQUE EL VALOR DE SU 3RA NOTA: "))

if NOTA_3 >10:
    NOTA_3 +=2

promedio = float((NOTA_1 + NOTA_2 + NOTA_3)/3)

print(promedio)
