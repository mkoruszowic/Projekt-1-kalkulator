# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:48:51 2019

@author: student
"""

import numpy as np
import time



#~~~~~~~~~~~~~~~~~~~~~~~~~~~***WYZNACZNIK MACIERZY***~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Obliczanie wyznacznika z definicji"""

def det(x):
    length=len(x)
    d={}    #tworzy biblioteke
    sum=0
    if length>1:
        k=1
        for t in range(length):
            t2=0
            for i in range (1,length):
                d[t2]=[]  #dla klucza t2 przypisuje wartosć którą jest pusta lista
                for j in range(length):
                    if t!=j:
                        d[t2].append(x[i][j]) #dołącza do listy w bibliotece poszczegolne elementy z macierzy
                t2=i
            x2=[d[x] for x in d] #tworzenie listy z biblioteki
            sum=sum+k*(x[0][t])*(det(x2)) # sumowanie
            k=k*(-1)
            t=+1
        return sum
    else:
        return (x[0][0])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~***MACIERZ TRANSPONOWANA***~~~~~~~~~~~~~~~~~~~~~~~~

"""Funkcja tworzy nowa liste zamieniajac wspolrzedne kazdego elementu
ze starej list z i,j na j,i"""

def T(x):
    c=list()
    for i in range(len(x)):
        b=list()
        for j in range(len(x)):
            b.append(x[j][i])
        c.append(b)
    return(c)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~***MACIERZ DOPEŁNIEŃ***~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Funkcja tworząca liste będąca macierzą odwrotną"""
"""Te samo działanie co w funkcji det rozszerzone o przejscie po kazdej wspolrzednej
macierzy oraz brak zmiennej sum która pozwalała na liczenie wyznacznika"""

def dop(x):
    pomoc=[]
    dop=[]
    licznik=1
    length=len(x)
    d={}
    if length>1:
        k=1
        for i2 in range(0,length):
            for j2 in range(0,length):
                key=0
                for i in range (0,length):
                        if i2!=i:
                            d[key]=[]
                            for j in range(length):
                                if j2!=j:
                                        d[key].append(x[i][j])
                            key+=1
                matrix2=[d[x] for x in d]

                k=(-1)**(i2+j2) #wspolczynnik którego wartosć jest uzalezniona od wpsolrzendych i oraz j
                a=k*det(matrix2)
                pomoc.append(a)
                if licznik==length:
                    dop.append(pomoc)
                    pomoc=[]
                    licznik=0
                    k=-k
                licznik+=1

        return dop
    else:
        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~***MACIERZ ODWROTNA***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Odw(x):
    if det(m)==0: #odrzucanie przypadku gdy wyznacznik jest rowny 0
        return "Macierz odwrotna nie istnieje"
    elif len(m)==1:
        return "Nie można wykonać tego typu obliczeń dla podanej macierzy"
    else:
        c=list()
        for i in range(len(x)):
            b=list() #tworzenie nowej list b w której będą zapisywane obliczone elementu macierzy odwrotnej
            for j in range(len(x[0])):
                b.append(round(float(dop(T(x))[i][j]*(1/det(m))),2)) #zaokraglanie liczby i dołaczenie jej do listy
            c.append(b) #dołaczenie do listy c listy b składającej sie z wiersza macierzy odwrotnej
        return(c)

#~~~~~~~~~~~~~~~~~~~~~~~~~***TWORZENIE NOWEJ MACIERZY***~~~~~~~~~~~~~~~~~~~~~~~

def matrix(n):
    y=[]
    z=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            while 1:
                try:
                    x=int(input("Podaj liczbe o wspolrzednych (%s,%s): " %(str(i),str(j))))
                    break
                except:
                    print("\nProsze podać liczbę!")
            y.append(x)
            if j==n:
                z.append(y)
                y=[]
    print("\nTwoja macierz:\n")
    printing(z)
    return(z)

#~~~~~~~~~~~~~~~~~~***MIERNIK CZASU OBLICZANIA WYZNACZNIKA***~~~~~~~~~~~~~~~~~~

"""Funkcja licząca czas wykonania dla wbudowanej funkcji linalg.det oraz funkcji det"""

def timer():
    start = time.clock() #zmienna ktorej przypisuje sie czas w momencie wywołania funkcji
    g = np.linalg.det(m)
    end = time.clock() #zmienna ktorej przypisuje sie czas w momencie zakonczenia działania funkcji
    time1 = end - start #liczenie roznocy miedzy poczatkiem i końcem wywołania funkcji

#analogicznie jak powyżej
    start = time.clock()
    h = det(m)
    end = time.clock()
    time2 = end - start #liczenie roznocy miedzy poczatkiem i końcem wywołania funkcji
    print("Funkcja linalg.det():")
    print("WYNIK: %i    CZAS OBLICZEŃ: %f [s] \n" %(g,time1))
    print("Funkcja kalkulatora: ")
    print("WYNIK: %i    CZAS OBLICZEŃ: %f [s] \n" %(h,time2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~***NOWA MACIERZ***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Funkcja tworzy macierz według wskazań użytkownika"""
def wielkosc():
    while 1:
        try:
            n=int(input("\nPodaj wielkosć macierzy kwadratowej: ")) #wczytanie wielkosci macierzy
            while n<=0: #pętla wychwytująca podanie macierzy ujemnej
                n=int(input("Liczba musi być dodatnia.\nPodaj wielkosć macierzy kwadratowej: "))
            break
        except: #zabezpieczneie przed podaniem stringa
            print("\nProsze podać liczbę!")
    return n

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~***WYSWIETLANIE***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Funkcja wypisująca liste tak żeby wygladała jak macierz"""
def printing(x):
    if x==0:
        print(x)
    elif type(x)==str:
        print(x)
    else:
        for i in range(len(x)):
            print(x[i]) #wypisywanie i-tej podlisty

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~***SEKCJA GŁÓWNA***~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while 1:
    try:
        n=int(input("WITAJ W KALKULATORZE MACIERZY!\nPodaj wielkosć macierzy kwadratowej: "))
        while n<=0:
            n=int(input("Liczba musi być dodatnia.\nPodaj wielkosć macierzy kwadratowej: "))
        break
    except:
        print("\nProszę podać liczbę!")


m=matrix(n) #wywołanie funckji tworzącej macierz


while 1:
    print(2*"\n")
    print("Dostępne operacje: \n")
    print("(1) Obliczanie wyznacznika macierzy")
    print("(2) Obliczanie macierzy odwrotnej")
    print("(3) Obliczanie macierzy transponowanej")
    print("(4) Obliczanie macierzy dopełnień")
    print("(5) Obliczanie macierzy dołączonej")
    while 1: #zabezpieczneie w przypadku podania stringa
        try:
            n=int(input("Wybierz działanie: "))
            break
        except:
            print("\nProsze podać liczbę!")
    print("\n")

    while n>=6: #zabezpieczenie w przypadku podania liczby spoza zakresu
        while 1:
            try:
                n=int(input("Liczba spoza zakresu. Wybierz działanie: "))
                break
            except:
                print("\nProsze podać liczbę!")

    """Wykonywanie wybranego wczesniej działania"""

    if n==1:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        timer()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif n==2:
        print("MACIERZ ODWROTNA")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        printing(Odw(m))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif n==3:
        print("MACIERZ TRANSPONOWANA")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        printing(T(m))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif n==4:
        print("MACIERZ DOPEŁNIEŃ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        printing(dop(m))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif n==5:
        if len(m)!=1:

            print("MACIERZ DOŁĄCZONA")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            printing(T(dop(m)))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("MACIERZ DOŁĄCZONA")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Nie można wykonać tego typu obliczeń dla podanej macierzy")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




    print("\nCzy chcesz działać dalej?")
    print("(1) Tak, na bieżacej macierzy")
    print("(2) Tak, na nowej macierzy")
    print("(3) Nie")
    while 1:  #zabezpieczenie w przypadku podania liczby spoza zakresu
        try:
            n=int(input("Odp.: "))
            while n!=1 and n!=2 and n!=3:
                n=int(input("Proszę podać liczbę 1, 2 albo 3. Odp.: "))
            break
        except:  #zabezpieczneie w przypadku podania stringa
            print("\nProsze podać liczbę!")
    if n==1:
        pass
    elif n==2:
        m=matrix(wielkosc())
    elif n==3:
        break
