#inicio
import os
os.system("cls")

'''persona ha recorrido tres tramos de una carretera. La longitud del primer tramo está dada
en kilómetros, el segundo tramo en pies y el tercer tramo en millas. Desarrolle el programa que
determine la longitud total recorrida en metros y en yardas. Considere los siguientes factores de
conversión: 1 metro = 3.2808 pies, 1 milla = 1609 metros'''

kilometros= float (input("Escriba la cantidad de kilometros 1er tramo:" ))
pies= float (input("Escriba la cantidad en pies 2do tramo:" ))
millas= float (input("Escriba la millas en pies 3er tramo:" ))

metros=kilometros*1000.0
pies=pies/3.281
millas=millas*1609

total_de_metros=metros+pies+millas
print("total recorrida en metros",total_de_metros,"metros" ) 
yardas=total_de_metros*1094
print("total recorrida en yardas",yardas,"yardas" ) 