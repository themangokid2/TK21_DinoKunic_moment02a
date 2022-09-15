# Dino Kunic, TK21
# Moment02, inlämningsuppgift 1
# Denna uppgiften var inte svår med tanke på att math importen ger oss allt vi behöver, ganska simpelt med input output
# det 'svåraste' var dock i slutet när jag skulle printa en if statement 
# som ska ge oss ett int värde om vi anger ett int värde, och printa float värde om vi anger ett float värde
# , dock fick jag reda på att jag kunde använda .is_integer för att fixa detta problemet.

import math # importerar matte så att vi kan använda den inbyggda variablen pi

enhet = "cm\u00b2" #ger en lämplig enhet

radie = float(input('vad e radien på din cirkel')) #du anger radien på din cirkel i cm

intRadie = int(radie), enhet # integer värde av din radie sparas

area = math.pi*radie**2 # gör matten för area

intArea = int(math.pi*radie**2), enhet # sparar int värde av area

omkrets = float(2*math.pi*radie) # räknar ut omkrets och omvandlar till float med angedd radie

intOmkrets = int(omkrets) # sparar int värde av din omkrets

roundedRadie = round(radie, 2), enhet #avrundar radie till 2 decimaltal

roundedOmkrets = round(omkrets, 2), enhet # avrundar

roundedArea = round(area, 2), enhet # avrundar

if float(radie).is_integer(): # en if statement, om radie är en integer så printas ut 3 värden som är strikt integer
        print('radie är{0} area är{1}omkrets är {2}'.format(intRadie, intArea, intOmkrets))
else:
        print('radie är{0} area är{1}omkrets är {2}'.format(roundedRadie, roundedArea, roundedOmkrets)) # om inte printas endast float värden













