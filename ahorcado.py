from lista import lista_de_palabras
from funciones import guiones, letras
import random
print("Bienvenido a ahorcado")
print("por favor ingresar una letra a la vez")
p= random.randrange(0,999)
palabra=(lista_de_palabras(p))
guion=guiones(palabra)
print(guion)
win=False
while win==False:
		letra=input("ingrese una letra: ")
		print(guion)
