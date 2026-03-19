# To-Do List Projekt

## Popis a cíl projektu
Program je jednoduchý úkolníček v Pythonu.  
Uživatel si může zapisovat své úkoly, prohlížet je a mazat.  
Cílem projektu je naučit se pracovat s funkcemi, seznamy a cykly v Pythonu, a zároveň vytvořit interaktivní program vhodný pro každodenní použití.

## Funkcionalita programu
- Přidání nového úkolu do seznamu
- Zobrazení aktuálních úkolů
- Smazání vybraného úkolu
- Menu pro snadnou navigaci
- Ošetření chybového zadání (např. špatné číslo při mazání)

## Technická část
- Použité knihovny: pouze standardní Python (`input`, `print`, `list`)
- Algoritmy: jednoduchá iterace přes seznamy, výběr podle indexu
- Struktura programu:
    - Funkce `zobraz_ukoly(ukoly)` – vypíše seznam úkolů
    - Funkce `main()` – hlavní smyčka programu s menu
- Program běží v konzoli (žádné GUI)

## Uživatelský návod
1. Spusť soubor `todo.py` v Pythonu 3.x  
2. Zobrazí se menu s možnostmi: přidat úkol, zobrazit úkoly, smazat úkol, konec  
3. Postupně zadávej volby podle potřeby  
4. Program se ukončí po výběru “Konec”