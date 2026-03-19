import generators as gen
import sorting as sort

def menu():
    print("=== PROJEKT AiSD: SORTOWANIE ===")
    
    # ---------------------- Pobranie danych od użytkownika ---------------------- #
    try:
        n = int(input("Podaj liczbę elementów (n): "))
    except ValueError:
        print("To musi być liczba!")
        return

    print("\nWybierz rodzaj ciągu:")
    print("1. Losowy\n2. Rosnący\n3. Malejący\n4. Stały\n5. A-kształtny")
    c_wybor = input("Wybór (1-5): ")

    # ------------------ Generowanie tablicy na podstawie wyboru ----------------- #
    if c_wybor == '1': tablica = gen.generate_random(n)
    elif c_wybor == '2': tablica = gen.generate_ascending(n)
    elif c_wybor == '3': tablica = gen.generate_descending(n)
    elif c_wybor == '4': tablica = gen.generate_constant(n)
    elif c_wybor == '5': tablica = gen.generate_a_shaped(n)
    else: 
        print("Zły wybór!")
        return

    print("\nTablica przed sortowaniem:", tablica)

    # ------------------------------ Wybór algorytmu ----------------------------- #
    print("\nWybierz algorytm:")
    print("1. Insertion Sort\n2. Selection Sort\n3. Shell Sort\n4. Heap Sort\n5. Quick Sort (Left)\n6. Quick Sort (Random)")
    a_wybor = input("Wybór (1-6): ")

    # ------------- Wywołanie odpowiedniej funkcji z pliku sorting.py ------------ #
    if a_wybor == '1': wynik = sort.insertion_sort(tablica)
    elif a_wybor == '2': wynik = sort.selection_sort(tablica)
    elif a_wybor == '3': wynik = sort.shell_sort(tablica)
    elif a_wybor == '4': wynik = sort.heap_sort(tablica)
    elif a_wybor == '5': wynik = sort.quick_sort(tablica, pivot_type="left")
    elif a_wybor == '6': wynik = sort.quick_sort(tablica, pivot_type="random")
    
    print("\nTablica po sortowaniu:", wynik)

menu()