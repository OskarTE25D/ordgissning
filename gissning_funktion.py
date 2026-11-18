def gissa(ord, shh_ord, felgissningar):
    while True: 
        if len(felgissningar) == 10: #kollar om man har gått förbi 10 felgissningar
            print("Du suger!")
            break
        while True:
            gissning = input("Ange en gissning: ").upper() #upper gör bokstäverna stora för att göra inmatning enklare
            if gissning.isalpha() == False or len(gissning) > 1: #om man matar in något som inte är en bokstav eller en sträng längre än 1 bokstav
                print("Gissningen ska vara en bokstav!")
                continue
            else:
                break
        hittad = False 
        for char in ord: 
            for pos in range(len(ord)): #går igenom varje bokstav i ordet
                if ord[pos].upper() == gissning: #kollar om bokstaven pos är på är samma som vår gissning 
                    shh_ord = shh_ord[:pos] + gissning + shh_ord[pos+1:] #byter ut den hemliga bokstaven mot den man har hittat i rätt position
                    hittad = True
        if not hittad:
            if gissning in felgissningar: #kollar om gissningen är i felgissningar och låter inte användaren mata in samma bokstav flera gånger
                print("Denna bokstav finns redan!")
                continue
            else:
                felgissningar += gissning #annars lägger till bokstaven till felgissningar
        return shh_ord, felgissningar #returnerar det hemliga ordet i asterisker och hur många felgissningar spelaren har (10 från början)

#ord=svaret
#shh_ord=strängen som fylls i av rätt gissning
#felgissningar=strängen som innehåller alla felgissningar