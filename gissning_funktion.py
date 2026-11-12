def gissa(ord,shh_ord,felgissningar):
    while True:
        if len(felgissningar) == 10:
            print("Du suger!")
            break
        gissning = input("Ange en gissning: ").upper().split()
        for char in ord:
            for pos in range(len(ord)):
                shh_ord = replace_str(shh_ord, pos, char)
                
    return shh_ord,felgissningar
print(gissa("banan", "*****", ""))

#ord=svaret
#shh_ord=strängen som fylls i av rätt gissning
#felgissningar=strängen som innehåller alla felgissningar