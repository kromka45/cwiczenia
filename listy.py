"""
newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
'''
def wyciagam(dane):
    print("Populacja                stan")
    for k in dane:
        print(k[1],"                ",k[0])

wyciagam(newEngland)
"""


"""
def raport(dane):  
    print(" ludność                    stan")
    for k in range(0,len(dane)):
        print(dane[k][1],"                  ",dane[k][0])

raport(newEngland)

"""

"""
def sumsa(dane):
    sumka = 0
    stany =len(dane)

    for k in range(0,stany):
        jeden=dane[k]
        populacja = jeden[1]
        sumka = sumka+populacja
# jako 2 argument funkcji range przy tablicy wykorzystuje funkcje len           
    print("ogólna populacja ludzi to :",sumka)
    print("Wśród ",stany,"Stanów")



sumsa(newEngland)
"""

numlis = [65, 44, 3, 56, 48, 74, 7, 97, 95, 42]  # test on this list
numlis2 = [4,6,8,12,2,7,19]     # test on a second list to be sur


def srednia(dane):
    dlugosc=len(dane)
    wynik =0
    
    for k in range(0,dlugosc):
        wynik = wynik+dane[k]
        print(dane[k],end=" ")
    print()
    
    sred=float(wynik/dlugosc)

    print("średnia to",sred)


srednia(numlis2)