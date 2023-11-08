import random
import math

#véletlen számok generálása

def veletlen():
    #[10,30] közötti vélatlen számokat
    i:int=0
    while i<110:
        szam:int= math.floor(random.random()*21 + 10)
        print(szam, end=" ")
        i+=1



'''
1.generál 5 véletlen lottószámot
[1,90]

2. generélj 1 véletlen számot
    dönts el róla, hogy páros, vagy páratlan?

3. generálj 15 db egész számot [0,1] között.
hány 1-es generáltál?

4. generálj egy véletlen 2 és 10 között!
szorozd ,eg 3-mal!
vonj ki belölle 05-öt
oszd el 6-tal
szorozd be 2-vel
vonj ki belölle az eredeti számot!
a program írja ki, hogy az eredmény egyenlő-e 5-tel?

5. írj ki metódust, mely a paraméterban kapott szövegnek
kiírja a hosszát!
az 5. karakterét nagybetűvel.
'''

#1.feladat:
def feladat1():
    i:int=0
    while i<5:
        szam:int= math.floor(random.random()*89 + 1)
        print(szam, end=" ")
        i+=1

#2.feladat:
def feladat2():
    i:int=0
    while i<1:
        szam:int= math.floor(random.random()*90 + 10)
        if szam % 2 == 0:
            print("Páros!!")
        else:
            print("Páratlan!!")
        print(szam, end=" ")
        i+=1

#3.feladat:
def feladat3():
    i:int=0
    while i<15:
        szam:int=random.random()*1 + 0
        print(szam, end=" ")
        i+=1

#4.feladat:
def feladat4():
    i:int=0
    while i<1:
        szam:int=math.floor(random.random()*9 + 1)
        eredmeny: szam * 3
        kivonas: eredmeny - 15
        osztas: kivonas / 6
        szorzas: osztas * 2
        kivonas2: szorzas - szam
        if kivonas2 % 5 == 0:
            print(szam, end=" ")
        else:
            print("nem osztható 5-el!!")
        i+=1
