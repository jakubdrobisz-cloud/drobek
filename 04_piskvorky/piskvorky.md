1. Funkcionalita
Hrací pole: Matice 3 \times 3 (seznam v seznamu).
Hráči: Střídání "X" a "O" pomocí operace modulo (tah % 2).
Ovládání: Vstup přes souřadnice 0, 1, 2 (řádek a sloupec).
2. Struktura kódu
tisk_pole(): Vykreslí mřížku do konzole.
kontrola_vyhry(): Kontroluje 3 v řadě (horizontálně, vertikálně, diagonálně).
piskvorky(): Hlavní smyčka hry, ošetření chyb (neplatný vstup, obsazené pole).
3. Pravidla vítězství
Hra končí výhrou jednoho hráče nebo zaplněním všech 9 polí (remíza).
4. Spuštění
Vyžaduje Python 3. Spustitelný přímo v terminálu.