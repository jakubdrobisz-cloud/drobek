import random

def vytvor_pole():
    hodnoty = ["A","A","B","B","C","C","D","D"]
    random.shuffle(hodnoty)
    return [hodnoty[:4], hodnoty[4:]]  # 2x4 pole


def zobraz(pole, odkryte):
    print("\n  0 1 2 3")
    for i in range(2):
        print(i, end=" ")
        for j in range(4):
            if odkryte[i][j]:
                print(pole[i][j], end=" ")
            else:
                print("*", end=" ")
        print()


def main():
    pole = vytvor_pole()
    odkryte = [[False]*4 for _ in range(2)]

    nalezeno = 0
    pokusy = 0

    while nalezeno < 4:
        zobraz(pole, odkryte)

        try:
            r1, s1 = map(int, input("První karta (řádek sloupec): ").split())
            r2, s2 = map(int, input("Druhá karta (řádek sloupec): ").split())
        except:
            print("Špatný vstup!")
            continue

        if (r1, s1) == (r2, s2):
            print("Nemůžeš vybrat stejnou kartu!")
            continue

        if not (0 <= r1 < 2 and 0 <= s1 < 4 and 0 <= r2 < 2 and 0 <= s2 < 4):
            print("Mimo pole!")
            continue

        odkryte[r1][s1] = True
        odkryte[r2][s2] = True
        zobraz(pole, odkryte)

        pokusy += 1

        if pole[r1][s1] == pole[r2][s2]:
            print("✔ Našel jsi dvojici!")
            nalezeno += 1
        else:
            print("❌ Nesedí")
            odkryte[r1][s1] = False
            odkryte[r2][s2] = False

    print(f"\n🎉 Vyhrál jsi za {pokusy} pokusů!")


main()
