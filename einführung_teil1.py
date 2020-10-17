# Hallo Lion, hier möchte ich dir ein Paar wichtige Punkte erläutern, die dir den Start in Python erleichtern sollen.

# Zunächst beginnen wir mit den Variablen. Diese können in Python z.B. Textwerte, Zahlenwerte und einiges mehr
# enthalten. Textwerte werden als Zeichenkette (string in Englisch) bezeichen, da sie aus den Zeichen (das können z.B.
# Buchstaben, Zahlen und bestimmte Sonderzeichen sein) bestehen. Zeichenketten werden zwischen doppelten Anführungszeichen
# gesetzt; einfache Anführungszeichen sind aber auch möglich.
name = "Janis, Wladimir und Lion"
nachricht = 'Wir spielen am Wochenende Fußball.' # hier werden einfache Anführungszeichen benutzt.
titel_des_buchs = "König der Löwen"

# Außer den Zeichenketten können auch Zahlen in Variablen gespeichert werden.
alter = 12
punkte = 140

# es gibt noch viele andere Werte die man in Variablen speichern kann. Auf diese gehen wir zu einem späteren Zeitpunkt ein.



# Eine Ausgabe auf Console in Python wird mit print()-Befehl gemacht.
print("Programmieren kann Spaß machen!")



# Willst du Benutzer deines Programms auffordern, etwas einzugeben, kannst du den Befehl input() verwenden.
# hier gibt es zwei Möglichkeiten.

# Möglichkeit 1: man gibt die Aufforderung/Frage mit dem Befehl print() aus und liest die Angabe dann mit input() ein:
print("Gebe bitte deinen Namen ein: ")
name_des_benutzers = input()

# Möglichkeit 2: man gibt die Aufforderung/Frage gleich mit dem input()-Befehlt aus:
name_des_benutzers = input("Gebe bitte deinen Namen ein: ")


# Will man eine Zahl einlesen, um damit zu rechnen oder mit anderen Zahlen zu vergleichen, so muss das Ergebnis des
# Befehls input() noch zu einer Zahl umgewandelt werden, da alles was mit input() eingelesen wird als Textwert
# im Computer ankommt. Das erreichen wir, indem wir um input(...) herum den Befehl int(...) benutzen. Will man z.B.
# das Alter des Benutzers erfahren so kann der Code wie folgt geschrieben werden:
alter_des_benutzers = int( input("Wie alt bist du?") )



# Oft möchte man Werte, die in Variablen im Programm gespeichert sind, bei der Ausgabe berücksichtigen. Möchte man den
# Namen des Benutzern, den man vorher eingelesen hat oder bei einem Spiel den Namen des Spielers und seine Punkte
# am Ende ausgeben so kann man Platzhalter im Text platzieren; für Zeichenketten verwendet man %s, bei ganzzahligen Werten
# wird %i benutzt.
# Will man Platzhalter im Text mit tatsächlichen Werten ersetzen, schreibt man hinter dem Text % gefolgt vom Wert oder
# dem Variablennamen. Hier muss man beachten, dass bei mehreren Platzhaltern bei der Ersetzung die tatsächlichen Werte
# oder Variablennamen in Klammern durch Komma getrennt angegeben werden:


print("Hallo %s, ich bin C3PO. Wie kann ich dir helfen?" % "Paul") # hier wird ein Wert direkt angegeben.
print("Willkommen in unserem Team, %s." % name_des_benutzers) # hier stammt der Wert aus einer variable

spieler_name = "Super Mario"
spieler_punkte = 371
# hier werden Werte von zwei Variablen eingesetzt - beachte hier die Klammern
print("Spieler %s hat %i Punkte erreicht." % (spieler_name, spieler_punkte))

# Ersetzung kann auch an einem Text vorgenommen werden, der dann in einer neuen Variable gespeichert wird
nachricht = "Spieler %s hat %i Punkte erreicht." % (spieler_name, spieler_punkte)
print(nachricht) # wir können die nachricht natürlich auch ausgeben lassen.




