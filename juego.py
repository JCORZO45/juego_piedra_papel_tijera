# Juego piedra_papel_tijera 

#input 
P=1
R=2
T=3

print("escoja una opcion: \n")
print("1.Piedra \n")
print("2.Papel \n")
print("3.Tijera \n")
opcion= int(input("\n Digite la opcion: "))


#process 
import random 
n=random.randint(1,3)

if (n==1):
    j=("piedra") 
if (n==2):
    j=("papel")
if (n==3):
    j=("tijera")

if(opcion==1):
    k=("piedra")
if(opcion==2):
    k=("papel")
if(opcion==3):
    k=("tijera")

print("escogiste:" + str(k))
print("la computadora escogio:" +str(j))
if(opcion== n):
    print("Empate")
elif(opcion== 1 and n==2):
    print("perdiste")
elif(opcion==1 and n==3):
    print("Ganaste")
elif(opcion== 2 and n==1):
    print("ganaste")
elif(opcion==3 and n==1):
    print("perdiste")
elif(opcion==3 and n==2):
    print("ganaste")
elif(opcion==2 and n==3):
    print("perdiste")

#fin