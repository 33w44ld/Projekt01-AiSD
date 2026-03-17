import random

# ----------------------------- Zwraca losowy ciąg liczb ---------------------------- #
def generate_random(n):
    wynik = []
    for i in range(n):
        random_num = random.randint(1, 10000)
        wynik.append(random_num)
    return wynik

# ------------------- Zwraca losowy ciąg liczb posortowany rosnąco ------------------ #
def generate_ascending(n):
    wynik = []
    for i in range(1, n + 1):
        wynik.append(i)
    return wynik

# ------------------ Zwraca losowy ciąg liczb posortowany malejąco ------------------ #
def generate_descending(n):
    wynik = []
    for i in range(n, 0, -1):
        wynik.append(i)
    return wynik

# ---------------------------- Zwraca ciąg stały liczby losowej ---------------------------- #
def generate_constant(n):
    wynik = []
    random_num = random.randint(1, 10000)
    for i in range(n):
        wynik.append(random)
    return wynik

# -------------------------- Zwraca ciąg A-kształtny ------------------------- #
def generate_a_shaped(n):
    wynik = []
    for i in range(1, n+1):
        if i % 2 != 0:
            wynik.append(i)
    for i in range(n, 0, -1):
        if i % 2 == 0:
            wynik.append(i)
    
    return wynik