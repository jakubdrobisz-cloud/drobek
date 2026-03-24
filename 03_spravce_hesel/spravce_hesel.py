# jednoduchý správce hesel

def uloz_heslo():
    nazev = input("Název (např. Instagram): ")
    jmeno = input("Uživatelské jméno: ")
    heslo = input("Heslo: ")

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
                for radek in data:
                    print(radek.strip())
    except FileNotFoundError:
        print("Soubor zatím neexistuje.")

def main():
    while True:
        print("\n--- SPRÁVCE HESEL ---")
        print("1 - Přidat heslo")
        print("2 - Zobrazit hesla")
        print("3 - Konec")

        volba = input("Vyber: ")

        if volba == "1":
            uloz_heslo()

        elif volba == "2":
            zobraz_hesla()

        elif volba == "3":
            print("Konec programu")
            break

        else:
            print("Neplatná volba")

main()