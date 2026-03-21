# seznam pro ukládání úkolů (úkol + stav splnění)
def zobraz_ukoly(ukoly):
    if not ukoly:
        print("Žádné úkoly")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            stav = "✔ splněno" if ukol["hotovo"] else "❌ nesplněno"
            print(f"{i}. {ukol['text']} [{stav}]")


def main():
    ukoly = []

    while True:
        print("\n--- MENU ---")
        print("1 - Přidat úkol")
        print("2 - Zobrazit úkoly")
        print("3 - Smazat úkol")
        print("4 - Označit jako splněné")
        print("5 - Konec")

        volba = input("Vyber: ")

        if volba == "1":
            text = input("Zadej úkol: ")
            ukoly.append({"text": text, "hotovo": False})
            print("Úkol přidán")

        elif volba == "2":
            zobraz_ukoly(ukoly)

        elif volba == "3":
            zobraz_ukoly(ukoly)
            try:
                cislo = int(input("Který úkol chceš smazat? "))
                ukoly.pop(cislo - 1)
                print("Úkol smazán")
            except:
                print("Špatné číslo")

        elif volba == "4":
            zobraz_ukoly(ukoly)
            try:
                cislo = int(input("Který úkol je splněný? "))
                ukoly[cislo - 1]["hotovo"] = True
                print("Úkol označen jako splněný")
            except:
                print("Špatné číslo")

        elif volba == "5":
            print("Konec programu 👋")
            break

        else:
            print("Neplatná volba")


main()
