croisantPrijs = .39
stokbroodPrijs = 2.78
kortingsbonKorting = 0.5


croisants = int(input("Hoeveel croisants wilt u?\n"))
stokbroden = int(input("Hoeveel stokbroden wilt u?\n"))
kortingsbonnen = int(input("En hoeveel kortingsbonnen heeft u?\n"))

totalPrice = (croisantPrijs * croisants) + (stokbroodPrijs * stokbroden) - (kortingsbonKorting * kortingsbonnen)
print("De feestlunch kost je bij de bakker " + str(totalPrice) + " voor de " + str(croisants) + " croissantjes en de " + str(stokbroden) + " stokbroden als de " + str(kortingsbonnen) + " kortingsbonnen nog geldig zijn!")