def gissa(ord, shh_ord, felgissningar):
    while True:
        if len(felgissningar) == 10:
            print("Du suger!")
            break
        while True:
            gissning = input("Ange en gissning: ").upper()
            if gissning.isalpha() == False or len(gissning) > 1:
                print("Gissningen ska vara en bokstav!")
                continue
            else:
                break
        hittad = False
        for char in ord:
            for pos in range(len(ord)):
                if ord[pos].upper() == gissning:
                    shh_ord = shh_ord[:pos] + gissning + shh_ord[pos+1:]
                    hittad = True
        if not hittad:
            felgissningar += gissning
        return shh_ord, felgissningar

#ord=svaret
#shh_ord=strängen som fylls i av rätt gissning
#felgissningar=strängen som innehåller alla felgissningar