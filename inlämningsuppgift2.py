# Dino Kunic, TK21
# Moment02, inlämningsuppgift 2
# Denna uppgiften blev väldigt svår i slutet, dock likt den första uppgiften har vi det mesta redo med datetime importen
# , skillnaden på den första uppgiften var dock bara att det var en math input
# Det som jag ansåg som svårast var den sista deluppgift där vi skulle subtrahera 2 angedda tider med varandra(i rätt format),
#  men jag kom på att jag kunde skapa en list och sedan omvandla tiderna till sekunder med simpel matte och sedan subtrahera 
# och omvandla till lämpligt format igen

import datetime # importerar lämpligt paket för att kunna göra beräkningar med  tiden
sekunder = int(input("seconds ")) # integer input för att omvandla en tid i sekunder till HH:MM:SS
input(datetime.timedelta(seconds=sekunder)) # här görs beräkningen med hjälp av datetime.timedelta

h = int(input("timmar ")) #input timmar
m = int(input("minuter ")) #input minuter
s = int(input("sekunder")) #input sekunder
print(int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())) # datetime.timedelta tar alla sparade h,m,s värden och omvandlar till sekunder .total_seconds

a = input("Största tiden du vill subtrahera i formatet [HH:MM:SS] : ") #input en tid du vill subtrahera med
b = input("Andra tiden du vill subtrahera i formatet [HH:MM:SS] : ") # input en annan tid du vill subtrahera

a_from_str_to_list = a.split(':')  # konverterar string till list för att vi anger en string med : tecken och gör en split för lämpligt format
b_from_str_to_list = b.split(':') # exakt samma sak här fast med variablen b

a_seconds = ( int(a_from_str_to_list[0]) * 3600 ) + ( int(a_from_str_to_list[1]) * 60 ) + int(a_from_str_to_list[2]) # sätter datatypen till int så att vi inte får variabler när vi sedan subtraherar, här används listan med [0] osv för att skapa lämpligt format HH:MM:SS, vi multiplicerar sedan allting med 3600, 60 för att omvandla värdena till sekunder för att enklare subtrahera från variabeln a

b_seconds = ( int(b_from_str_to_list[0]) * 3600 ) + ( int(b_from_str_to_list[1]) * 60 ) + int(b_from_str_to_list[2]) # samma sak men med variabeln b

c_seconds = a_seconds - b_seconds # vi gör matten och subtraherar sekunderna för att få det nya värdet

t = str(datetime.timedelta(seconds = c_seconds)) # sätter tillbaka formatet till HHMMSS sätter datatypen till seconds, asså jag använder mig utav seconds från datetime vilket ger ett lämpligt format

print(t) #printar resultatet