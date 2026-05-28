#l_elementow = 0
liczba_paczek = 1
calkowita_waga_elementow = 0
max_waga_paczki = 20
aktualna_waga_paczki = 0
waga_najlzejszej_paczki = 0
najlzejsza_paczka = 1

l_elementow = int(input("Podaj ilość elementów do wysłania: ")) #Podanie przez użytkownika liczbę elementów do wysłania
for element in range (l_elementow):
    waga_elementu = int(input(f"Podaj wagę {element+1} elementu: ")) #Pobranie informacji o wadze poszczególnych elementów
    if waga_elementu in range (1, 10):                                  # Warunek, że waga elementu musi być z zakresu 1-10 kg
        calkowita_waga_elementow += waga_elementu
        if waga_elementu + aktualna_waga_paczki <= max_waga_paczki:     # Warunek sprawdza czy następny element zmieści się do aktualnej paczki
            aktualna_waga_paczki += waga_elementu
            waga_najlzejszej_paczki += waga_elementu
        else:
            aktualna_waga_paczki = waga_elementu
            liczba_paczek += 1
            if aktualna_waga_paczki < waga_najlzejszej_paczki:          # Warunek sprawdza czy aktualna paczka jest lżejsza od dotychczasowej najlżejszej paczki
                najlzejsza_paczka = liczba_paczek
                waga_najlzejszej_paczki = aktualna_waga_paczki

    else:
        print("Waga elementu nie mieści się w zakresie 1-10 kg")
puste_kg = liczba_paczek * 20 - calkowita_waga_elementow
print(f"Całkowita waga elementów wynosi {calkowita_waga_elementow} kg.")
print(f"Ilość paczek do wysłania: {liczba_paczek}")
print(f"Suma pustych kilogramów wynosi: {puste_kg} kg.")
print(f"Najwięcej pustych kilogramów miała paczka nr. {najlzejsza_paczka}, z wynikiem {max_waga_paczki - waga_najlzejszej_paczki} kg.")
