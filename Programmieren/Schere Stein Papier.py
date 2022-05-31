import random
import time

#Variablen
wiederholung = "Ja"
punkte = 0
cpunkte = 0
# Fragt nach dem Namen.
name = input("Hallo was ist dein Name? ")
time.sleep(1)
print("Hallo " + str(name) + ",herzlich willkommen zu Schere Stein Papier")
time.sleep(1)
# Fragt ob er die Spielanleitung erklären soll
frage = input("Möchtest du die Spielanleitung wissen(Ja oder Nein)? ")
if frage == "Ja":
    print("Der Computer wählt entweder Schere, Stein oder Papier.") 
    print("Du musst dann  auch etwas wählen ohne das du das Ergebnis von Computer kennst.") 
    print("Der Gewinner wird ganz einfach entschieden : Stein schlägt Schere, Schere schlägt Papier und Papier schlägt Stein.")
    time.sleep(5)
if frage == "cheat":
    cheat = True
    print("cheat on")
    time.sleep(1)

while wiederholung == "Ja":
    # Computer wählt
    computer = random.choice(["Schere", "Stein", "Papier"])
    if cheat == True:
        print("Das Symbol vom Computer ist " + str(computer))

    # Fragt Spieler
    spieler = input("Welchen, Gegenstand möchtest du Einsetzen(Schere, Stein oder Papier)? ").strip().title()


    # Auswertung

    if spieler != "Schere" and spieler != "Stein" and spieler != "Papier":
        print("Diesen Gegenstand gibt es nicht.")

    if computer == spieler:
        print("Computer hat " + str(computer) + " gewählt: Unentschieden. ")
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")
    
    if computer == "Stein" and spieler == "Papier":
        print("Computer wählt Stein: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")
    if computer == "Stein" and spieler == "Schere":
        print("Computer wählt Stein: Verloren")
        cpunkte = cpunkte +1
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")

    if computer == "Papier" and  spieler == "Schere":
        print("Computer wählt Papier: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")
    if computer == "Papier" and spieler == "Stein":
        print("Computer wählt Papier: Verloren")
        cpunkte = cpunkte +1
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")

    if computer == "Schere" and  spieler == "Stein":
        print("Computer wählt Schere: Gewonnen")
        punkte = punkte + 1
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")

    if computer == "Schere" and spieler == "Papier":
        print("Computer wählt Schere: Verloren")
        cpunkte = cpunkte +1
        print("Du hast " + str(punkte) + " Punkte.")
        wiederholung = input("Möchtest du nochmal Spielen(Ja oder Nein)? ")

        if cpunkte == 10:
            wiederholung = "Nein"
            print("Der Computer hat Gewonnen. Viel Glück das nächste mal, " + str(name))