import random

# ----------------------------- Losowy ciąg liczb ---------------------------- #
def generate_random(n):
    return [random.randint(1,10000) for _ in range(n)]

# ------------------- Losowy ciąg liczb posortowany rosnąco ------------------ #
def generate_ascending(n):
    return list(range(1, n+1))

# ------------------ Losowy ciąg liczb posortowany malejąco ------------------ #
def generate_descending(n):
    return list(range(n, 0, -1))

