l_elementow = 0
liczba_paczek = 0
calkowita_waga_elementow = 0
#waga_paczki = 0

l_elementow = int(input("Podal ilość elementów do wysłania: ")) #Podanie przez użytkownika liczbę elementów do wysłania
for element in range (l_elementow):
    waga_elementu = float(input(f"Podaj wagę {element+1} elementu: ")) #Pobranie informacji o wadze poszczególnych elementów
    if waga_elementu in range (1, 10):                                  # Warunek, że waga elementu musi być z zakresu 1-10 kg
        calkowita_waga_elementow += waga_elementu
    else:
        print("Waga elementu nie mieści się w zakresie 1-10 kg")

print(f"Całkowita waga elementów wynosi {calkowita_waga_elementow} kg.")
#waga_paczki = 0
#while waga_paczki <= 20:
 #   liczba_paczek = 1
  #  waga_paczki =