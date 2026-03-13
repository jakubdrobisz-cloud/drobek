#budu delat kod pro hadani cisla
import random

def hra():
    print("Vítej ve hře hádej číslo!")
    print("Myslím si číslo mezi 1 a 100. Zkus ho uhodnout!")
    cislo = random.randint(1, 100)
    pokusy = 8
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
            print(f"Gratulace! Uhodl jsi číslo {cislo} za {9 - pokusy} pokusů!")
            return True
        pokusy -= 1
        print(f"Zbývá ti {pokusy} pokusů.")
    else:
        print(f"Prohrál jsi! Myslel jsem si číslo {cislo}.")
        return False

def main():
    while True:
        vyhra = hra()
        if vyhra:
            print("Skvělé! Chceš hrát znovu? (ano/ne)")
        else:
            print("Nevadí, zkus to znovu! Chceš hrát znovu? (ano/ne)")
        odpoved = input().lower()
        if odpoved != "ano":
            print("Díky za hru!")
            break

main()