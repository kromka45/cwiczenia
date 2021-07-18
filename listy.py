
newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
'''
def wyciagam(dane):
    print("Populacja                stan")
    for k in dane:
        print(k[1],"                ",k[0])

wyciagam(newEngland)
'''


"""
def raport(dane):  
    print(" ludność                    stan")
    for k in range(0,len(dane)):
        print(dane[k][1],"                  ",dane[k][0])

raport(newEngland)

"""


def suma(dane):
    sumka = 0
    stany =len(dane)

    for k in range(0,stany):
        jeden=dane[k]
        populacja = jeden[1]
        sumka = sumka+populacja
        




        
    print("ogólna populacja ludzi to :",sumka)
    print("Wśród ",stany,"Stanów")
    


suma(newEngland)

