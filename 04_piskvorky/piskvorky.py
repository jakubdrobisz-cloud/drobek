def tisk_pole(pole):
    for radek in pole:
        print(" | ".join(radek))
        print("-" * 9)

def kontrola_vyhry(pole, hrac):
    # Kontrola řádků a sloupců
    for i in range(3):
        if all([pole[i][j] == hrac for j in range(3)]) or \
           all([pole[j][i] == hrac for j in range(3)]):
            return True
    # Kontrola diagonál
    if all([pole[i][i] == hrac for i in range(3)]) or \
       all([pole[i][2-i] == hrac for i in range(3)]):
        return True
    return False

def piskvorky():
    pole = [[" " for _ in range(3)] for _ in range(3)]
    hraci = ["X", "O"]
    tah = 0

    print("Vítejte u piškvorek! Zadávejte řádek a sloupec (0, 1 nebo 2).")

    while tah < 9:
        tisk_pole(pole)
        aktualni_hrac = hraci[tah % 2]
        print(f"Hraje hráč {aktualni_hrac}")

        try:
            r = int(input("Zadej řádek: "))
            s = int(input("Zadej sloupec: "))

            if pole[r][s] == " ":
                pole[r][s] = aktualni_hrac
                if kontrola_vyhry(pole, aktualni_hrac):
                    tisk_pole(pole)
                    print(f"Gratuluji! Vyhrál hráč {aktualni_hrac}!")
                    return
                tah += 1
            else:
                print("Toto pole už je obsazené, zkus to znovu.")
        except (ValueError, IndexError):
            print("Neplatný vstup! Zadej čísla od 0 do 2.")

    tisk_pole(pole)
    print("Remíza!")

if __name__ == "__main__":
    piskvorky()
