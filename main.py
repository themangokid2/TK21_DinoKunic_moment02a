# jag har skrivit den första linjen på ett lätt sätt endast med en print
# den andra linjen har jag kunnat använda mig utav dubbelcitat genom att använda seperat citat i print('')
# den tredje linjen har jag kunnat bryta linjen med \n för att skriva 3 rader text med en enda print()

print('Jag heter Dino och jag går på amerikanska gymnasiet')

print('Jag tycker att det är "kul" med programmering')

print('Dessa tre rader \nhar jag skrivit \nmed en enda print()')

#uppgift m02u01 ovanför

import math
a = 9
b = 2
f = 4.0
name = "dino"

print(type(a*b), a*b) #visar vilken datatyp som framstår, samma för alla nedre
print(type(a*f), a*f) 
print(type(a/b), a/b) #för att 9/2 ger 4.5 alltså ett värde med en decimal vilket gör det till float
print(type(name), name)
print(type(a//b), a//b) # eftersom att heltalsdivision ger endast ett heltal och därför blir int
print(type(a%b), a%b) # eftersom att det inte kan bli decimaler i rest och rest är hur mycket är över alltså int
print(type(math.sqrt(a)), math.sqrt(a)) # för att math.sqrt() alltid ger ut float() 
print(type(b**2), b**2) # för att 2^2 ger ett tal utan decimaler
print(type(f**2), f**2) # detta ger float eftersom att vi har deklarerat f som en float
print(b+a)

#uppgift m02u02 ovanför

penna = 4
apple = 0.019
resultapple = 200*apple
resultpenna = 3*penna
valuta = "kr"
round(resultapple, 2)


print('Jag köpte 3 pennor för', penna*3, str(valuta), 'och 1 äpple för', round(resultapple, 2), str(valuta), 'vilket totalt blev', resultpenna+resultapple, str(valuta) ) 
# denna blev lite lång men alla värden är variabler förutom valutan vilket inte är ett värde utan en string för att teckna valutan SEK

print(f"Jag köpte 3 pennor för {resultpenna} och 1 äpple för {round(resultapple, 2)} vilket totalt blev {resultpenna+resultapple}", str(valuta))
#lite kortare eftersom att jag använder annan slags formatering

choosepenna = int(input("hur många pennor vill du köpa"))
totaltpenna = choosepenna * penna
print("det kommer att kosta", totaltpenna, "kr för", choosepenna, "pennor")
chooseapple = int(input("hur många kg äpplen vill du köpa i GRAM"))
totaltapple = apple * chooseapple
print (int(totaltapple))

print()
print("penna", totaltpenna, valuta)
print("äpple", int(totaltapple), valuta)
print("----------------------------")
print("summa", int(totaltpenna+totaltapple), valuta)

# Skriv en kommentar för varje fel du identifierar och löser.
# Beskriv vad som var fel och hur du har löst det.
exchange_rate = 8.82
print('Detta är ett program där vi kan växla mellan SEK & dollar') #lägger citationstecken
sek = float (input("Hur många SEK vill du växla till dollar: ")) #stänger parantesen
dollar = sek / exchange_rate #gör den till exchange_rate ist
print("Du ville växla {0} SEK vilket blir {1} dollar.".format(sek, dollar)) # stänger parantes









