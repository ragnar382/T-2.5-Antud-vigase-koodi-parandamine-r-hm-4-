print("vali programm")
print("1 Ruutvõrrandi lahendamine")
print("2 nädala palga arvutamine")
print("3 parkimis hind")



programm=(input("vali programm (1,2,3): "))
if programm==1 :
 print ("ruutvõrrandi lahendamine")
if programm==2 :
 print ("2 nädala palga arvutamine")
if programm==3 :
 print("parkimis hind")
 

print("Ruutvõrrandi lahendamine")
a = float(input("Sisesta a => ")) #ülakoma oli vale
b = float(input("Sisesta b => "))
c = float(input("Sisesta c => ")) #peab olema float ,sest me arvutame arvudega

D = b*b - 4*a*c

if D > 0: #koolon oli puudu
    x1 = (-b + D**0.5) / (2*a)   #sulud olid puudu 2*a
    x2 = (-b - D**0.5) / (2*a)
    print("Kaks lahendit:", x1, x2)
elif D == 0: #tuleb lisada else if asemel elif ja d = 0 on puudu 1 võrdusmärk
    x = -b / (2*a)
    print("Üks lahend:", x)
else:
    print("Reaalarvulised lahendid puuduvad")
print()

print("Palga arvutamine")

tunnid = float(input("Sisesta töötunnid nädalas => "))
tunnitasu = float(input("Sisesta tunnitasu (€) => "))

if tunnid < 0 or tunnid > 168:  #and asemel kasutame or
    print("Vigane tundide arv")
elif tunnid <= 40:
    palk = tunnid * tunnitasu
    print("Nädalapalk:", palk, "€")
else:
    palk = 40*tunnitasu + (tunnid-40)*tunnitasu*1.5
    print("Nädalapalk koos ületundidega:", palk, "€")

print()

print("Parkimise hind")

tunnid = int(input("Sisesta parkimise aeg tundides => "))

if tunnid < 0: #eemaldasin =
    print("Vigane aeg")
elif tunnid >= 8:   #Parkimise tingimused olid vales järjekorras. Kõigepealt tuleb kontrollida 8 või rohkem tundi.
    print("Hind: 10 € (päevapilet)")
elif tunnid >= 3:
    print("Hind: 5 €")
else:
    print("Hind: 2 €") #sulg oli puudu