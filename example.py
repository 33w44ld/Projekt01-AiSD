import sys
import sorting as sort  # Importujesz swój plik z algorytmami

def sort_using_algorithm(data, algorithm):
    # Mapowanie numerów na Twoje funkcje (zgodnie z benchmark.sh)
    if algorithm == 1: return sort.insertion_sort(data)
    if algorithm == 2: return sort.shell_sort(data)
    if algorithm == 3: return sort.selection_sort(data)
    if algorithm == 4: return sort.heap_sort(data)
    if algorithm == 5: return sort.quick_sort(data, "left")
    if algorithm == 6: return sort.quick_sort(data, "random")
    return sorted(data)

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        sys.exit(1)

    algorithm_number = int(sys.argv[2])
    # Czytanie danych z wejścia (skrypt .sh przekazuje je tutaj)
    input_raw = sys.stdin.read().split()
    if not input_raw: return

    # Pierwsza liczba to rozmiar (n), reszta to tablica
    data = [int(x) for x in input_raw[1:]]
    
    # Wykonanie Twojego sortowania
    sorted_data = sort_using_algorithm(data, algorithm_number)
    
    # Benchmark nie potrzebuje wypisywania całej tablicy, 
    # wystarczy potwierdzenie dla Ciebie:
    # print(f"Sorted {len(sorted_data)} elements")

if __name__ == "__main__":
    main()