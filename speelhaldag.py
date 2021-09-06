ticketPrijs=7.45
vrPerMinuut = 0.37 / 5

tickets = int(input("Hoeveel tickets wilt u?\n"))
vrMinuten = int(input("Hoeveel minuten wilt u VR doen?\n"))

totalPrice = (tickets*ticketPrijs) + ((vrPerMinuut * vrMinuten) * tickets)

print("Dit geweldige dagje-uit met " + str(tickets) + " mensen in de speelhal met " + str(vrMinuten) + " minuten vr kost je maar " + str(totalPrice) + " euro")