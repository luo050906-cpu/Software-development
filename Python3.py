import random
klas25a = ["Daan A", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V.", "Kateryna"]
x = int(input(f"Hoeveel namen (1–{len(klas25a)})? "))
if 1 <= x <= len(klas25a):
    for n in random.sample(klas25a, x):
        print(n)
else:
    print("Ongeldige keuze.")
        