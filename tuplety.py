



from os import write



def Informacja(imie,wiek,zawod):
    
    while True:
        imie=input(str("podaj imie"))
        wiek= input(str("wiek?"))
        zawod=input(str("jaki jest twoj zawod"))
        infilename = open('wejscie.txt','w')
        z =str("Mam na imie: "+imie+"Mam; "+wiek+"Lat a to Moj zawod : "+zawod+"\n")
        infilename.write(z)
        start = input("wprowadz 1 aby pisac dalej,wprowadz 0 aby zakonczyc")
        if start == "0":
            break
    
          




Informacja(imie=str,wiek=str,zawod=str)


        





