# 1. feladat:
def feladat1():
    szam: int = int(input("Kérem a számot [200, 920] intervallumban: "))

    if 200 <= szam <= 920:
        elso_szamjegy: int = int(str(szam)[0])
        print("Az első számjegy:", elso_szamjegy)
    else:
        print("Hiba: A megadott szám nincs az [200, 920] intervallumban.")


# 4. feladat:
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




