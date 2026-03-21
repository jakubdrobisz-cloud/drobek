#seznam pro ukládání úkolů 
def zobraz_ukoly(ukoly):
    if not ukoly:
        print(" Žádné úkoly")
    else:
        print("\n Seznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol}")

def main():
    ukoly = []

    while True:
        print("\n--- MENU ---")
        print("1 - Přidat úkol")
        print("2 - Zobrazit úkoly")
        print("3 - Smazat úkol")
        print("4 - Konec")

        volba = input("Vyber: ")

        if volba == "1":
            ukol = input("Zadej úkol: ")
            ukoly.append(ukol)
            print(" Úkol přidán")

        elif volba == "2":
            zobraz_ukoly(ukoly)

        elif volba == "3":
            zobraz_ukoly(ukoly)
            try:
                cislo = int(input("Který úkol chceš smazat? "))
                ukoly.pop(cislo - 1)
                print(" Úkol smazán")
            except:
                print(" Špatné číslo")

        elif volba == "4":
            print("👋 Konec programu")
            break

        else:
            print(" Neplatná volba")

main()