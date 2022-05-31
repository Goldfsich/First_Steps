import time
import random

# Variablen
name = "Spieler"
weiter = "ja"
beenden = "nein"

# Begrüßung
print("Guten Tag.")
print("")
time.sleep(0.5)
name = input("Wie heißt du? ")
print("")
time.sleep(0.5)
print("Hallo " + str(name) + ", ich begrüße dich zu dem Spiel Strichmänchen.")
print("")
time.sleep(0.5)

#Fragt ob du die Anleitung wissen willst.
regeln = input("Soll ich dir die Regeln des Spieles erklären(Ja/Nein)? ").lower()
print("")
if regeln == "ja":
    print("Der Computer denkt sich ein Wort aus.")
    time.sleep(0.5)
    print("Du musst Buchstaben sagen.")
    time.sleep(0.5)
    print("Wenn diese Buchstaben in dem Wort vorkommen werden sie in das Wort eingezeichnet.")
    time.sleep(0.5)
    print("Wenn nicht wird das Galgenmänchen weiter Aufgebaut.")
    time.sleep(0.5)
    print("Wenn du das Wort erraten hast, bevor das Galgenmänchen fertig ist hast du Gewonnen.")
    print("")

while weiter == "ja":
    while beenden == "nein":
        spielmodi = input("Wie schwer soll das Spiel sein(leicht, mittel oder schwer)? ")
        
        if spielmodi == "schwer":
            beenden = "Ja"
            print("Deine Schwierigkeitstufe ist schwer")
            
        elif spielmodi == "mittel":
            beenden = "Ja"
            print("Deine Schwierigkeitstufe ist mittel")
            
        elif spielmodi == "leicht":
            beenden = "Ja"
            print("Deine Schwierigkeitstufe ist leicht")
            
        else:
            print("diese Schwierigkeitsstufe gibt es nicht")
    print("fertig")
    weiter = "nein"