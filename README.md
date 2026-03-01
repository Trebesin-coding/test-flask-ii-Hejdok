# Test: Flask, JSON

## Flask

1.  zajisti, ať se vitej.html načítá jako první (defaultní) stránka webového serveru
2.  ve form.html ztuční a podbarvi nadpis Recepty pomocí CSS - použij externí .css soubor
3.  uprav formulář tak, ať se dá odeslat odpověď
4.  do app.py přidej práci s formulářem - flask přijme odeslaná data z formuláře a pošle je zpět na stránku form.html
5.  pokud uživatel zadal slovo "nvm" místo receptu flask pošle zpět zprávu "autor byl příliš líný na napsání receptu" - bonus stejnou hlášku to vypíše pro jakékoliv slovo, které má 3 a méně znaků
6.  uprav formulář tak, ať se zobrazí odeslaná odpověď na stránce
7.  do kódu vlož komentář, který vysvětluje, co dělá tento blok kódu `if __name__ == "__main__": app.run(debug=True)`

## JSON

8.  data z formuláře ulož také do JSON recepty.json ve složce data


# Hodnocení:

✅

❌

🚩chybí uzavření formuláře

🚩ve formuláři chybí name u inputů a proto flask informace nepřijímá, redirect nemá hodnotu, kam by měl redirectovat

🚩v případě krátkého slova flask printuje, místo toho aby data poslal zpět na stránku

❌

❌

🚩nikde není specifikováno co je message, která se má ukládat do jsonu

## Známka: 4

