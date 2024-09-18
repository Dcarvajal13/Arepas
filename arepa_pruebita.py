#Se declaran los ingredientes
agua = int(input("cuantas tazas de agua?"))
print("el agua es", agua)
harina= int(input("cuantas tazas de harina?"))
print("la harina es", harina)
sal = int(input("cuantas cdas de sal?")) #La sal se convierte de cdtas a tazas, hay 3 cdtas por cda y 16 cdas por taza
print("la sal es", sal)
aceite = int(input("cuantas cdas de aceite?")) #El aceite se convierte de cdas a tazas

#Comienza la preparación de la arepa
bol = agua + harina + sal
budare = bol + aceite

#Se imprime el resultado
print("La arepa final es", budare)

input("presione enter para continuar")
