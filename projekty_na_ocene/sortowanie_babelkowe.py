import random
lista=[]
wybor = input("Chcesz podac czy wylosowac liste? (podac/wylosowac): ")
while wybor!="podac" and wybor!="wylosowac":
        wybor = input("Nie obsluguje takiej komendy. \nWybierz jeszcze raz: ")

if wybor=="podac":
    dlugosc=int(input("Podaj jak dluga bedzie twoja lista: "))
    dlugosc=dlugosc-1
    while dlugosc>=0:
        dodane=int(input("Podaj element: "))
        lista.append(dodane)
        dlugosc=dlugosc-1
    print(lista)
else:
     dlugosc=random.randint(1, 21)
     dlugosc=dlugosc-1
     while dlugosc>=0:
        dodane=random.randint(1, 1001)
        lista.append(dodane)
        dlugosc=dlugosc-1
     print(lista)

wybor = input("Chcesz znalezc najmniejsza czy najwieksza wartosc? (min/maks): ")
while wybor!="min" and wybor!="maks":
        wybor = input("Nie obsluguje takiej komendy. \nWybierz jeszcze raz: ")

if wybor=="min":
     for i,j in lista:
        if lista[i] > lista[j]:
            lista.remove[i]
        else:
            lista.remove[j]
     print("Minimalna wartoscia na liscie jest ", lista[1])
else:
     for i,j in lista:
          if lista[i] > lista[j]:
               lista.remove[j]
          else:
               lista.remove[i]
     print("Maksymalna wartoscia na liscie jest ", lista[1])

#NIE DZIALAJA ELEMENTY, NAPRAW