# jednoduché šachy v terminálu

def vytvor_sachovnici():
    return [
        ["r","n","b","q","k","b","n","r"],
        ["p","p","p","p","p","p","p","p"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["P","P","P","P","P","P","P","P"],
        ["R","N","B","Q","K","B","N","R"]
    ]


def zobraz(s):
    print("\n  a b c d e f g h")
    for i, radek in enumerate(s):
        print(8 - i, " ".join(radek))
    print()


def prevod(pole):
    try:
        x = 8 - int(pole[1])
        y = ord(pole[0]) - ord('a')
        return x, y
    except:
        return None, None


def je_bily(figurka):
    return figurka.isupper()


def je_cerny(figurka):
    return figurka.islower()


def tah(s, hrac):
    while True:
        vstup = input(f"{hrac} táhne (např. e2 e4): ")

        try:
            start, konec = vstup.split()
        except:
            print("Zadej tah ve formátu: e2 e4")
            continue

        x1, y1 = prevod(start)
        x2, y2 = prevod(konec)

        if None in (x1, y1, x2, y2):
            print("Špatný formát!")
            continue

        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            print("Mimo šachovnici!")
            continue

        figurka = s[x1][y1]

        if figurka == " ":
            print("Tady není žádná figurka!")
            continue

        if hrac == "Bílý" and not je_bily(figurka):
            print("To není tvoje figurka!")
            continue

        if hrac == "Černý" and not je_cerny(figurka):
            print("To není tvoje figurka!")
            continue

        cil = s[x2][y2]

        if hrac == "Bílý" and je_bily(cil):
            print("Nemůžeš sebrat vlastní figurku!")
            continue

        if hrac == "Černý" and je_cerny(cil):
            print("Nemůžeš sebrat vlastní figurku!")
            continue

        # jednoduchý tah (bez pravidel)
        s[x2][y2] = figurka
        s[x1][y1] = " "
        break


def main():
    sachovnice = vytvor_sachovnici()
    hrac = "Bílý"

    while True:
        zobraz(sachovnice)
        tah(sachovnice, hrac)

        # střídání hráčů
        if hrac == "Bílý":
            hrac = "Černý"
        else:
            hrac = "Bílý"


main()
