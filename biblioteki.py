""" import random

print(random.randint(3,8))

 """
''' verbs=["goes","cooks","shoots","faints","chews","screams"]
nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"] '''




''' import random

def zdanie():
    przyimek =random.choice(articles)
    rzeczownik = random.choice(nouns)
    czasownik = random.choice(verbs)
    przymiotnik = random.choice(adverbs)

    zdanie_ = przyimek + " " + rzeczownik + " " + czasownik + " " + przymiotnik + ". "

    zdanie_=zdanie_.capitalize()

    print(zdanie_)


zdanie()
 '''


''' def poemat():
    for k in range(0,4):

        przyimek =random.choice(articles)
        rzeczownik = random.choice(nouns)
        czasownik = random.choice(verbs)
        przymiotnik = random.choice(adverbs)

        zdanie_ = przyimek + " " + rzeczownik + " " + czasownik + " " + przymiotnik + ". "

        zdanie_=zdanie_.capitalize()

        print(zdanie_,end="")


poemat()
 '''




import warnings


def funkcja():
    tablica=[]
    while True:

        
        z=str(input("wprowadz"))
       
        if z=="cip":
            print(warnings.WarningMessage)
            
            break
        tablica.append(z)
        

    print(tablica)
funkcja()
