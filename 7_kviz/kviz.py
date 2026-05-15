# Kvíz hra v Pythonu

otazky = [
    {
        "otazka": "Jaké je hlavní město Česka?",
        "moznosti": ["a) Brno", "b) Praha", "c) Ostrava"],
        "spravne": "b"
    },
    {
        "otazka": "Kolik je 5 * 6?",
        "moznosti": ["a) 30", "b) 56", "c) 25"],
        "spravne": "a"
    },
    {
        "otazka": "Který jazyk používáme v tomto projektu?",
        "moznosti": ["a) Java", "b) C++", "c) Python"],
        "spravne": "c"
    },
    {
        "otazka": "Kolik stran má čtverec?",
        "moznosti": ["a) 3", "b) 4", "c) 5"],
        "spravne": "b"
    },
    {
        "otazka": "Jaká planeta je nejblíže Slunci?",
        "moznosti": ["a) Merkur", "b) Země", "c) Mars"],
        "spravne": "a"
    }
]

def hra():
    skore = 0

    print("Vítej v kvízové hře!")

    for cislo, otazka in enumerate(otazky, 1):
        print(f"\nOtázka {cislo}:")
        print(otazka["otazka"])

        for moznost in otazka["moznosti"]:
            print(moznost)

        odpoved = input("Tvoje odpověď: ").lower()

        if odpoved == otazka["spravne"]:
            print("Správně!")
            skore += 1
        else:
            print("Špatně!")

    print(f"\nKonec hry! Tvoje skóre je {skore}/{len(otazky)}")

hra()