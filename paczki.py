l_elementow = 0
liczba_paczek = 0
waga_elementu = list
#waga_paczki = 0

l_elementow = int(input("Podal ilość elementów: "))
for k in range (l_elementow):
    print(f"Podaj wagę {k+1} elementu")
    waga_elementu.insert(k,input()) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #waga_elementu.append(int(input())) #= input("Podaj wagę elementów separując je przecinkiem: ")
print(f"Ilość elementów do wysłania: {l_elementow}")
#print(f"Waga elementów: {waga_elementu.split(',')}")
print(waga_elementu)
#waga_paczki = 0
#while waga_paczki <= 20:
 #   liczba_paczek = 1
  #  waga_paczki =