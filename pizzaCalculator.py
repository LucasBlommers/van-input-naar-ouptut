#Lucas Blommers
#Pizza Calculator

#Defineer de pizza prijzen
smallPizza = 7.49
mediumPizza = 8.99
largePizza = 11.49

#Introductie
introduction = """
---- Pizzaria De Itialiaan ----
                                     ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   \\
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i'
    :
"""
print(introduction + "\nWij verkopen 3 pizza margarita's: klein (" + smallPizza + " p.st), middel (" + mediumPizza + " p.st) en groot (" + largePizza + " p.st).")

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