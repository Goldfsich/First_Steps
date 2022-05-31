
import random
import time 

# Variblen
spielmodi = "nicht" 
beenden = "nein"
weiter = "Ja"
cheat = "of"
punkt = 0

# Fragt nach dem Namen und ob es die Regeln des Spieles erklären soll.
name = input("Hallo was ist dein Name? ")

regeln = input("Guten Tag " + str(name) + ". Soll ich dir die Regeln des Spiels erklären(Ja oder Nein)? ")

if regeln == "Ja":
    print("Die Regeln sind Einfach: Du musst eine Zahl erraten. Wenn du es unter 10 Versuchen geschaft hast, kriegst du einen Punkt. Es gibt drei Spielschwierigkeiten.")
    time.sleep(3)
if regeln == "ja":
    print("Die Regeln sind Einfach: Du musst eine Zahl erraten. Wenn du es unter 10 Versuchen geschaft hast, kriegst du einen Punkt. Es gibt drei Spielschwierigkeiten.")
    time.sleep(3)
if regeln == "cheat":
    print("cheat on") 
    cheat = "on"

#Fragt nach der Schwierigkeit des Spiels
while beenden != "Ja":
    spielmodi = input("Wie schwer soll das Spiel sein(leicht, mittel oder schwer)? ")
    
    if spielmodi == "schwer":
        beenden = "Ja"
        print("Du hast Zahlen von 1 bis 1000")
        break
    if spielmodi == "mittel":
        beenden = "Ja"
        print("Du hast Zahlen von 1 bis 100")
        break
    if spielmodi == "leicht":
        beenden = "Ja"
        print("Du hast Zahlen von 1 bis 10")
        break
    else:
        print("diese Schwierigkeitsstufe gibt es nicht")

# Das Eigentliche Spiel
while weiter == "Ja":
    
    versuche = 0
    punkt2 = ("keinen")

    if spielmodi == "schwer":
        zahl = random.randint(1, 1000)
    if spielmodi == "mittel":
        zahl = random.randint(1, 100)
    if spielmodi == "leicht":
        zahl = random.randint(1, 10)

    if cheat == "on":
        print(zahl)

    schätzung = int(input("Was ist deine Zahl? "))

    while True:
        
        if schätzung == zahl:
            versuche = versuche + 1
            if versuche < 11:
                punkt = punkt + 1
                punkt2 = ("einen")
            weiter = input("Sehr Gut " + str(name) + ". Du hast " + str(versuche) +  " Versuche gebraucht und " + str(punkt2) + " weiteren Punkt bekommen. Möchtest du nochmal(Ja oder Nein) ?" )
            break
        elif zahl < schätzung:
            print("Zu groß")
            versuche = versuche + 1
            schätzung = int(input("Nächster Versuch "))
        elif zahl > schätzung:
            print ("zu klein")
            versuche = versuche + 1
            schätzung = int(input("Nächster Versuch "))

print("Du hast " + str(punkt) + " Punkte gekriegt")