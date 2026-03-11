#budu delat kod pro hadani cisla
import random
def hra():
    print("Vítej ve hře hádej číslo!")
    print("Myslím si číslo mezi 1 a 100. Zkus ho uhodnout!")
    cislo = random.randint(1, 100)
    pokusy = 8
    while pokusy > 0:
        hadani = int(input("Zadej svůj tip: "))
        if hadani < cislo:
            print("Moc nízké! Zkus to znovu.")
        elif hadani > cislo:
            print("Moc vysoké! Zkus to znovu.")
        else:
            print(f"Gratulace! Uhodl jsi číslo {cislo}!")
            break
        pokusy -= 1
    else:
        print(f"Prohrál jsi! Myslel jsem si číslo {cislo}.")

hra()