from gissning_funktion import gissa 
from ordlista import ord_slump #import random ord från vår ordlista

#1 hej och välkommen type shit
print("Välkommen till ordgissnings-spelet!")
spela_igen = "j"

while spela_igen == "j":
    ord = ord_slump()
    n = len(ord)
    print(f"Du ska gissa ett ord, bokstav för bokstav, på {n} bokstäver")

    #3 en loop som anropar gissa()-funktionen i gissning_funktion.py, sedan uppdatera variabler
    shh_ord = "*" * len(ord)
    felgissningar = ""

    while shh_ord != ord.upper() and len(felgissningar) < 10:
        shh_ord, felgissningar = gissa(ord.upper(), shh_ord, felgissningar)

        print("Ord:", shh_ord)
        print(f"Du har {10 - len(felgissningar)} felgissningar kvar!")
        print("Felgissningar:", felgissningar)

    #4 användaren vann/förlora och spela igen prompt

    if shh_ord == ord.upper():
        print("Du vann!")
    else:
        print("Du förlorade!")

    spela_igen = input("Vill du spela igen? (j/n): ").lower()

print("buuu")