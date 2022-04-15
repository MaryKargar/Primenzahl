

#Um zu überprüfen, ob eine Zahl wie x an Primzahl steht,
# ist ein Divisionstest.
# Dieser Test prüft die Teilbarkeit von n über eine ganze Zahl zwischen 2 und dem Rest x.
#import ist für mathematische funktionen zuladern (sqrt)
import math
#Die Variable x nimmt eine Zahl vom Benutzer durch Eingabe,Die Variable x wird in int (stirng to integer) konvertiert, da sie standardmäßig ein String ist.
x = input ("Enter Number :")
#Wir erstellen eine if-Bedingung, vorausgesetzt, wenn x größer als eins ist,Betrachten Sie eine for-Schleife mit Zähler i,
# die im Bereich 2 liegt und x(range funktion)Das heißt, es beginnt von 2 bis eins vor x.
x = int(x)
if x > 1:
#(2,√x)+1
#√55=7+1 weil brauchen wir 7 auch zahlen
#for i in range (2 , int(math.sqrt(x))+1):Innerhalb der Schleife verwenden wir die Bedingung, wenn der Rest der Division von x durch i gleich Null ist.
#Druckt, die keine Primzahlen sind, andernfalls sind Drucke Primzahlen.
#math.sqrt ist Funktion von Hochzahl√
      for i in range (2 , int(math.sqrt(x))+1):
          if (x % i) == 0 :
              print(x , "Nummber is Not Prime" )
              break
          else:
              print(x , "Nummber is prime")
              break
