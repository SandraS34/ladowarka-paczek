l_elementow = 0
liczba_paczek = 0
#liczba_kilogramow= 0
#waga_paczki = 0

l_elementow = int(input("Podal ilość elementów: "))
waga_elementu = input("Podaj wagę elementów separując je przecinkiem: ")
print(f"Ilość elementów do wysłania: {l_elementow}")
print(f"Waga elementów: {waga_elementu.split(',')}")
