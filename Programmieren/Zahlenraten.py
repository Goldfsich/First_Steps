import random

# Spieler begrüßen
print("hallo Spieler")
wiederholung = True
# Spieler nach der Anleitung fragen
erklärung = input("Möchtest du die Spielanleitung wissen (Ja oder Nein)")
if erklärung == "Ja":
    print("Du musst einen Buchstaben erraten. Wenn du richtig bist hast du gewonnen")
if erklärung == "cheat":
    print("cheats on")
spielmodi = input("welche Schwierigskeitsstufe(leicht,mittel oder schwer)")
if spielmodi == "leicht":
    gn = 1, 10
if spielmodi == "mittel":
    gn = 1, 100
if spielmodi == "schwer":
    gn = 1, 1000


while wiederholung == True:
    # Damit mann mehrmals fragen kann 
    gefunden = True
    runde = 0

    # Einen zufällige Zahl generieren
    zahl = random.randint(gn)

    if erklärung == "cheat":
        print(zahl)

    while gefunden == True:
        # Spieler nach seiner Eingabe Fragen
        eingabe = int(input("welche Zahl möchtest du eingeben"))

        # Auswertung

        if zahl == eingabe:
            runde = runde + 1
            print("glückwunsch, gefunden")
            gefunden = False
            print("du hast" + str( runde ) +  "versuche gebraucht")
            wiederholung2 = input("Willst du nochmal Spiele(Ja oder Nein)?")
            if wiederholung2 == "Ja":
                wiederholung = True
        if zahl != eingabe:
            print("Leider daneben")
            if zahl > eingabe:
                print("zu klein")
            if zahl < eingabe:
                print("zu groß")
                runde + runde + 1