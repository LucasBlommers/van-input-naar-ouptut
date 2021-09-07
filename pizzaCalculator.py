#Lucas Blommers
#Pizza Calculator

#Defineer de pizza prijzen
smallPizza = 7.49
mediumPizza = 8.99
largePizza = 11.49

#Introductie
print("Welkom bij pizzaria de Italiaan.\nWij verkopen 3 pizza margarita's: klein (7,49 p.st), middel (8,99 p.st) en groot (11,49 p.st).")

#Bestelling opnemen
print("Hoeveel kleine pizza's wilt u?")
smallPizzas = int(input())

print("Hoeveel middel pizza's wilt u?")
mediumPizzas = int(input())

print("Hoeveel groote pizza's wilt u?")
largePizzas = int(input())

#Prijs berekening
price= (smallPizza * smallPizzas) + (mediumPizza * mediumPizzas) + (largePizza * largePizzas) 
#Prijs opgave weergeven
print(str(smallPizzas) + " keer een kleine, " + str(mediumPizzas) + " keer een middel en " + str(largePizzas) + " groote pizza's. \nDat word dan " + str(price))