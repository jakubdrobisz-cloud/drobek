import random

# možné hodnoty karet
karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# spočítá skóre
def spocitej_skore(ruka):
    skore = sum(ruka)

    # pokud je eso (11) a skóre je moc vysoké, změní se na 1
    while skore > 21 and 11 in ruka:
        ruka[ruka.index(11)] = 1
        skore = sum(ruka)

    return skore


# náhodná karta
def vytahni_kartu():
    return random.choice(karty)


# zobrazí karty
def zobraz_karty(hrac, pocitac):
    print("\nTvoje karty:", hrac)
    print("Tvoje skóre:", spocitej_skore(hrac))

    print("Karta počítače:", pocitac[0])
    print("Druhá karta počítače: ?")


# hlavní hra
def hra():
    hrac = [vytahni_kartu(), vytahni_kartu()]
    pocitac = [vytahni_kartu(), vytahni_kartu()]

    while True:
        zobraz_karty(hrac, pocitac)

        if spocitej_skore(hrac) > 21:
            print("\nPřesáhl jsi 21.")
            print("Prohrál jsi.")
            return

        volba