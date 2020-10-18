# Wir haben bisher gelernt wie man Variablen für Texte und Zahlen definiert, wie man Text auf dem Bildschirm ausgibt
# und wie man Eingaben vom Benutzer einliest. Mit diesem Wissen allein können wir leider noch kein vernünftiges Programm
# kreieren. Um den Ablauf eines Programms zu steuern gibt es sogenannte Kontrollstrukturen. Eine davon ist die If-Anweisung.

# betrachten wir als erstes eine einfache If-Anweisung. Diese setzt sich wie folgt zusammen: in der ersten Zeile kommt if
# gefolgt von der Bedingung mit einem : am Ende der Zeile. In der nächsten Zeile/Zeilen folgen dann die Anweisungen/Befehle,
# welche nur ausgeführt werden, wenn die Bedingung erfüllt wird. Beachte, alle zeilen von diesem Anweisungsblock müssen
# etwas nach rechts (und ebenfalls gleich) eingerückt sein.

# In diesem Beispiel haben wir eine If-Anweisung mit der Bedingung, bei der der Anweisungsblock nur ausgeführt wird, wenn
# der Wert der Variable alter größer oder gleich 6 ist.
alter = 9
if alter >= 6:
    print("Hallo Schüler, ")
    print("du darfst bei unserem coolen Spiel mitmachen.")
    print("Viel Spass!")


# Oft will man im Programm  zusätzlich auch etwas anderes machen, falls eine Bedingung nicht erfüllt wird. Dazu verwendet
# man das Kommando else (in Deutsch: sonst)
temperatur_tee = 55 # Temperatur des Wassers in der Teetasse
if temperatur_tee >= 65:
    print("Tee ist noch zu heiß.")
else:
    print("Tee kann getrunken werden.")


# Ebenfalls oft will man mehrere Fälle (statt einer mehrere Bedinungen testen) unterscheiden und im Programm ganz verschieden behandeln.
# hier ist ein Beispiel, bei dem die Farbe überprüft wird. Dabei wird für jede Farbe eine eigene Ausgabe auf dem Bildschirm gemacht.
farbe = input("Nenne mir eine Farbe ... ")
if farbe == "gelb":
    print("Ich mag diese Farbe am liebsten! BVB!!!")
elif farbe == "grün":
    print("Diese Farbe ist nicht schlecht.")
elif farbe == "blau":
    print("Diese Farbe ist SCHLAKE :-P")
else:
    print("Diese Farbe kenne ich nicht ...")


# Hier sind noch ein Paar Beispiele für Vergleichsoperatoren, die man in den Bedingungen benutzen kann:
variable = "Paul"
if variable == "Johannes": # ist der Wert der Variable gleich "Johannes"
    pass # pass steht für leeren Anweisungsblock, und muss verwendet werden, falls man für best. Bedingung nichts machen möchte.
if variable != "Johannes": # ist der Wert der Variable ungleich "Johannes"
    pass

variable = 99
if variable < 100: # ist der Wert der Variable kleiner 100
    pass
if variable <= 99: # ist der Wert der Variable kleiner oder gleich 99
    pass
if variable > 50: # ist der Wert der Variable größer 50
    pass
if variable >= 200: # ist der Wert der Variable größer oder gleich 200
    pass



# Als Zusammenfassung von bisher Gelerntem: ein kleines Programm, welches den Namen und das Alter eines Teilnehmers
# einliest und abhängig davon wie alt der Teilnehmer ist verschiedene Nachrichten auf dem Bildschirm ausgibt.
print("Hier kannst du dich für unseren neuen Programmierkus anmelden.")
name = input("Wenn du teilnehmen willst, musst du jetzt deinen Namen eingeben. ... ")

alter = int(input("Hallo %s, Ich bin C3P0. Wie alt bist du, %s? ... " % (name, name))) # das eingegebene Alter in eine Zahl (int) umwandeln

if alter < 4:
    print("Entschuldige %s. Du bist leider noch zu jung. Komm wieder, wenn du 4 Jahre alt bist." % name)
elif alter < 6:
    print("Wow bist noch so jung, %s! Es wartet viel Spaß aus uns!" % name)
elif alter < 12:
    print("%s, du bist im besten Alter! Lass es krachen!" % name)
elif alter < 68:
    print("%s, warum hat es so lange gedauert!" % name)
else:
    print("Was hast du in den vergangenen %i Jahren getrieben, %s. Lass uns keine Zeit mehr verlieren!" % (alter - 4, name))
