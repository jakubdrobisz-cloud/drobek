# Projekt: Šachy v Pythonu

## Popis projektu
Tento projekt představuje jednoduchou hru šachy vytvořenou v programovacím jazyce Python. Hra funguje v terminálu a umožňuje dvěma hráčům hrát proti sobě.

## Funkce programu
- zobrazení šachovnice (8x8)
- zadávání tahů ve formátu např. "e2 e4"
- střídání hráčů (bílý a černý)
- kontrola základních chyb (špatný formát, mimo šachovnici, vlastní figurky)

## Jak program funguje
Šachovnice je uložena jako dvourozměrné pole (list v Pythonu).  
Každá figurka je reprezentována písmenem:
- velká písmena = bílý hráč
- malá písmena = černý hráč

Program neustále běží ve smyčce, kde:
1. zobrazí šachovnici
2. hráč zadá tah
3. tah se provede
4. hráči se střídají

## Omezení programu
- nejsou implementována kompletní pravidla šachu
- není kontrola šachu ani šach matu
- není implementována umělá inteligence

## Použité technologie
- Python 3
- základní datové struktury (listy, funkce)

## Spuštění programu
Program se spustí v terminálu příkazem:
