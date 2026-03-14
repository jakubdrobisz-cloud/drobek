#budu delat kod pro hadani cisla
import random


def ask_yes_no(prompt):
    """Vrací True pro ano, False pro ne."""
    while True:
        odpoved = input(prompt).strip().lower()
        if odpoved in ("ano", "a"):
            return True
        if odpoved in ("ne", "n"):
            return False
        print("Prosím, odpověz 'ano' nebo 'ne'.")


def hra(min_cislo=1, max_cislo=100, max_pokusy=8):
    print("Vítej ve hře hádej číslo!")
    print(f"Myslím si číslo mezi {min_cislo} a {max_cislo}. Máš {max_pokusy} pokusů.")
    cislo = random.randint(min_cislo, max_cislo)
    pokusy = max_pokusy

    while pokusy > 0:
        try:
            hadani = int(input("Zadej svůj tip: "))
        except ValueError:
            print("To není platné číslo! Zkus to znovu.")
            continue

        if hadani < cislo:
            print("Moc nízké! Zkus to znovu.")
        elif hadani > cislo:
            print("Moc vysoké! Zkus to znovu.")
        else:
            pouzite = max_pokusy - pokusy + 1
            print(f"Gratulace! Uhodl jsi číslo {cislo} za {pouzite} pokusů!")
            return True

        pokusy -= 1
        if pokusy > 0:
            print(f"Zbývá ti {pokusy} pokusů.")

    print(f"Prohrál jsi! Myslel jsem si číslo {cislo}.")
    return False


def main():
    while True:
        vyhra = hra()
        if vyhra:
            print("Skvělé, vyhrál jsi!", end=" ")
        else:
            print("Nevadí, příště to vyjde!", end=" ")

        if not ask_yes_no("Chceš hrát znovu? (ano/ne): "):
            print("Díky za hru!")
            break


if __name__ == "__main__":
    main()