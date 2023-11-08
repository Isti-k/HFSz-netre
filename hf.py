import math

# 1. feladat:
# 1.	Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az 
# intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!    
def feladat1():
    szam: int = int(input("Kérem a számot [200, 920] intervallumban: "))

    if 200 <= szam <= 920:
        elso_szamjegy: int = int(str(szam)[0])
        print("Az első számjegy:", elso_szamjegy)
    else:
        print("Hiba: A megadott szám nincs az [200, 920] intervallumban.")


# 4. feladat:
#4.	Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani.
# A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, így némiképp javul a hatékonyságuk (70%), a 8-9.
# órában azonban már újra lecsökken (50%).
#Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát, ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”)
def feladat2(a:int):
    if a == 1:
       print("Kiválóan vagyunk (90%)")
    elif a == 2 or a ==3:
        print("Éhség nagy úr (60%)")
    elif a == 4 or a == 5 or a == 6 or a == 7:
        print("Kezdek jól lenni (70%)")
    elif a == 8 or a == 9:
        print("Nem túl jó (50%)")
    elif a == 0:
        print("Be se jövök!")
    else:
        print("Túl lő a célon!")


#8. feladat:
#8.	Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj 
# hozzá formázott kiiratást!
def feladat3():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            result = i * j
            print(f"{i:2} x {j:2} = {result:2}", end="   ")
            j += 1
    print()
    i += 1


# 6. feladat:
#6.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon
#  hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
def feladat4():
    szam: float(input("Adjon meg egy valós számot: "))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(f"A(z) {szam} négyzetgyöke: {gyok}")
    else:
        print("Hiba: Negatív számból nem lehet gyököt vonni.")


#7.feladat:
#7.	A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor 
# legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét,
#  területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!
def feladat5():
    szam1 = float(input("Kérem adjon meg az első pozitív számot: "))
    szam2 = float(input("Kérem adjon meg a második pozitív számot: "))
    if szam1 > 0 and szam2 > 0:
        kerulet = 2 * (szam1 + szam2)
        terulet = szam1 * szam2
        print(f"Téglalap kerülete: {kerulet:.2f}")
        print(f"Téglalap területe: {terulet:.2f}")
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")


#feladatok:
#2. feladat.

def szam_szamjegye(szam:int):
    print("szam: ",szam)
#hogy kapjuk meg az utlsó számjegyet?
    while (szam>9):
        print("következő számjegy", szam%10)
        szam = szam // 10
        print("Az aktuális szám ", szam)
    
    print("Az utolsó számjegy ", szam)


def szam_szamjegye2(szam:int):
    szoveg_szam:str=str(szam)
    i=0
    while i<len(szoveg_szam):
        print(szoveg_szam [i])
        i+1

#10.feladat:
def ermedobas():
    i:int= 0
    fhossz:int=0
    f_szama:int=0
    max_hossz=0
    elozo_string_f=False
    while i<10:
        jel:str = input("F/I: ")
        while not ((jel=='F') or (jel=='f') or (jel=="I") or (jel=="i")):
            jel:str = input("nem jó, F/I-t adj meg! ")

        if (jel == 'f' or jel == 'F'):
            f_szama+=1
            fhossz+=1
            elozo_string_f=True
        else:
            print("aktuális hpssz: ", fhossz)
            elozo_string_f=False
            fhossz=0
            #itt összehasonlítjuk az eddigi maxhosszt
            #az aktuális hosszal
            if (max_hossz<fhossz):
                max_hossz=fhossz
            fhossz=0

        i+=1

    print("F-ek száma:", f_szama)
    if (max_hossz<fhossz):
        max_hossz=fhossz
    fhossz=0