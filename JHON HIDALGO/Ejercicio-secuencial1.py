#inicio
import os

os.system("cls")

'''Desarrolle el programa que determine el porcentaje de varones y de mujeres que hay en un salón de clases'''

mujeres=int(input("mujeres:"))
varones=int(input("varones:"))

total=varones+mujeres
porcentaje_varones=int((varones*100)/total)
porcentaje_mujeres=int((mujeres*100)/total)

print("el porcentaje de varones es",porcentaje_varones,"%")
print("el porcentaje de mujeres es",porcentaje_mujeres,"%")



