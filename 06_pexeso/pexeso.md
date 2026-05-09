# Projekt: Pexeso (Memory)

## Popis projektu
Tento projekt je jednoduchá hra pexeso vytvořená v jazyce Python. 
Hráč hledá dvojice stejných symbolů na hrací ploše.

## Funkce programu
- náhodné rozmístění karet
- odkrytí dvou karet
- kontrola, zda se karty shodují
- počítání pokusů
- oznámení výhry

## Jak program funguje
Program vytvoří hrací pole 2x4 se skrytými kartami. 
Hráč zadává souřadnice dvou karet ve formátu:
0 1

Pokud se symboly shodují, zůstanou odkryté. 
Pokud ne, znovu se skryjí.

Hra končí po nalezení všech dvojic.

## Použité technologie
- Python 3
- knihovna random

## Spuštění programu
Program se spustí příkazem:

```bash
python pexeso.py