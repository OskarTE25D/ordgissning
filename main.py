from gissning_funktion import gissa 
from ordlista import ord_slump #import random ord från vår ordlista

#hej och välkommen type shit
print("Välkommen till ordgissnings-spelet!")
spela_igen = "j"

while spela_igen == "j": #loop som kollar ifall man vill köra igen/startar spelet
    ord = ord_slump() 
    n = len(ord) 
    
    print(f"Du ska gissa ett ord, bokstav för bokstav, på {n} bokstäver") #introduktion

    shh_ord = "*" * len(ord) #gör ordet till bara asterisker
    felgissningar = ""

    while shh_ord != ord.upper() and len(felgissningar) < 10: #loop som kollar ifall man inte har vunnit/förlorat
        #använder gissa funktionen för att låta användaren gissa och kollar ifall man gissat rätt/fel, ändrar variablerna för resultatet
        shh_ord, felgissningar = gissa(ord.upper(), shh_ord, felgissningar) 

        print("Ord:", shh_ord)
        print(f"Du har {10 - len(felgissningar)} felgissningar kvar!")
        print("Felgissningar:", felgissningar)

    
    if shh_ord == ord.upper(): #kollar ifall man vunnit efter tidigare while-loopen säger att man har vunnit eller förlorat
        print("Du vann!")
    else:
        print("Du förlorade!")

    spela_igen = input("Vill du spela igen? (j/n): ").lower() #frågar användaren ifall de vill spela igen

print("buuu")