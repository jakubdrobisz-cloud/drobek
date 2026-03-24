# Správce hesel

## Popis a cíl projektu
Program slouží k ukládání a zobrazování hesel do souboru.  
Uživatel si může ukládat přihlašovací údaje k různým službám a později je zobrazit.  
Cílem je vytvořit jednoduchou, ale funkční aplikaci pro správu hesel.

## Funkcionalita programu
- Přidání nového hesla s názvem služby, uživatelským jménem a heslem
- Uložení hesel do souboru `hesla.txt`
- Zobrazení všech uložených hesel
- Jednoduché menu pro ovládání programu

## Technická část
- Použité knihovny: pouze standardní Python (žádné externí knihovny)
- Použité datové struktury: seznamy nejsou potřeba, data se ukládají přímo do souboru
- Funkce (`def`) pro jednotlivé akce: přidání hesla, zobrazení hesel, hlavní smyčka programu
- Práce se soubory: `open`, `write`, `read`, `readlines`
- Řídící struktury: cyklus `while` pro menu, podmínky `if/elif/else` pro volby uživatele
- Ošetření výjimek: kontrola existence souboru při načítání hesel (`FileNotFoundError`)

## Uživatelská instrukce
1. Spusť program `password_manager.py` ve svém Python prostředí.
2. Vyber možnost z menu:
   - `1` – přidat nové heslo
   - `2` – zobrazit uložená hesla
   - `3` – ukončit program
3. Při přidávání hesla zadej název služby, uživatelské jméno a heslo.
4. Uložená hesla se budou nacházet v souboru `hesla.txt`.