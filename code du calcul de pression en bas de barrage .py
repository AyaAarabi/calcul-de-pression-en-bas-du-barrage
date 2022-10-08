mv= float(input("entrez la valeur la lasse volumique : "))
g = float(input("entrez la valeur de l'acceleration :"))
h= float(input("entrez la valeur de hauteur : "))
try :
    P= mv*g*h
    print("la valeur de la pression est :",P,"N")
except:
    print("la valeur de la masse volmique ou/ et de hauteur ou/et de acceleration n'est pas correct")

