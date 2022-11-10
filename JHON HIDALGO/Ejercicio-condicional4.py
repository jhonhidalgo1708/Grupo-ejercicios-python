#Condicionales

'''4.	El promedio final de un curso se obtiene en base al promedio simple de tres prácticas calificadas. 
Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos puntos la nota de la tercera 
práctica calificada, si es que esta no es menor que 10. Desarrolle el programa que determine el promedio final de un
alumno conociendo sus tres notas. '''


nota_a = float(input("COLOQUE EL VALOR DE SU 1RA NOTA: "))
nota_b = float(input("COLOQUE EL VALOR DE SU 2DA NOTA: "))
nota_c = float(input("COLOQUE EL VALOR DE SU 3RA NOTA: "))

if nota_c >10:
    nota_c +=2

promedio = float((nota_a + nota_b + nota_c)/3)

print(promedio)
