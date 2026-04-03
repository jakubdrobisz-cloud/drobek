jednoduchý správce hesel

import getpass

def uloz_heslo():
    nazev = input("Název (např. Instagram): ")
    jmeno = input("Uživatelské jméno: ")
    heslo = getpass.getpass("Heslo: ")  # tady se heslo nezobrazuje

    with open("hesla.txt", "a") as soubor:
        soubor.write(f"{nazev} | {jmeno} | {heslo}\n")

    print(" Uloženo!")

def zobraz_hesla():
    try:
        with open("hesla.txt", "r") as soubor:
            data = soubor.readlines()

            if not data:
                print("Žádná uložená hesla.")
            else:
                print("\n--- ULOŽENÁ HESLA ---")
                for i, radek in enumerate(data, 1):
                    print(f"{i}. {radek.strip()}")
                return data  # Vrátí data pro smazání
    except FileNotFoundError:
        print("Soubor zatím neexistuje.")
        return []

def smaz_heslo():
    data = zobraz_hesla()
    if not data:
        return

    try:
        cislo = int(input("Zadej číslo hesla ke smazání: "))
        if 1 <= cislo <= len(data):
            del data[cislo - 1]
            with open("hesla.txt", "w") as soubor:
                soubor.writelines(data)
            print("Heslo smazáno!")
        else:
            print("Neplatné číslo.")
    except ValueError:
        print("Zadej platné číslo.")

def main():
    while True:
        print("\n--- SPRÁVCE HESEL ---")
        print("1 - Přidat heslo")
        print("2 - Zobrazit hesla")
        print("3 - Smazat heslo")
        print("4 - Konec")

        volba = input("Vyber: ")

        if volba == "1":
            uloz_heslo()

        elif volba == "2":
            zobraz_hesla()

        elif volba == "3":
            smaz_heslo()

        elif volba == "4":
            print("Konec programu")
            break

        else:
            print("Neplatná volba")

main()
