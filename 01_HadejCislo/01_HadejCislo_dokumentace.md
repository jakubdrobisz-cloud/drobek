# Hádej číslo

## Co program dělá
Tahle hra je o hádání čísla mezi 1 a 100.  
Program si náhodně vybere číslo a hráč se ho snaží uhodnout.

## Jak hra funguje
- Program si vygeneruje náhodné číslo
- Hráč má 8 pokusů
- Program hlásí, jestli je tip vyšší nebo nižší
- Když hráč uhodne číslo, vyhraje
- Když se pokusy vyčerpají, program ukáže správné číslo

## Jak je program napsaný
- Použita knihovna `random` pro náhodná čísla
- Hlavní funkce: `hra()`
- Smyčka `while` kontroluje počet pokusů a porovnává tip s číslem