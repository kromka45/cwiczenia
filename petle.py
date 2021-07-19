''' def dodajnik():
    sumka = 0
    while True:
        numer= int(input("Podaj liczbe albo wcisnij 0 by zobaczyc wynik i wyjsc:   "))
        if numer==0:
            break
        sumka=sumka+numer
    print("suma to: ", sumka)

dodajnik()
 '''




''' def licz():
    tablica=[]
    while True:
        nastepny=int(input("Podaj liczbę lub 0 by wyjść"))
        if nastepny==0:
            break
        tablica.append(nastepny)
    
    print(tablica)
licz() '''




def zamowienie():
    lista= []
    print("dzien dobry Będe od państwa zbierać zamówienie, jesli to wszystko napisz :koniec ")
    while True:
        order = str(input("Wprowadz zamowienie:"))
        if order =="koniec":
            break
        lista.append(order)
    print("panstwa zamowienie to:")

    for k in range(0,len(lista)):
        print(lista[k],end=" ")
    

zamowienie()

