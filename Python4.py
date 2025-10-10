import random
klas25a = ["Daan A", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V.", "Kateryna"]

x = int(input("Gewenste groepsgrootte (x): "))

y = int(input("Aantal groepjes (y): "))

if x < 1 or y < 1 or y > len(klas25a):
    print("Ongeldige keuze."); exit()

s = klas25a[:]; random.shuffle(s)

groepen = [[] for _ in range(y)]
i = 0

for _ in range(x):
    for g in range(y):
        if i < len(s): groepen[g].append(s[i]); i += 1

g = 0
while i < len(s):
    groepen[g % y].append(s[i]); i += 1; g += 1

for k, grp in enumerate(groepen, 1):
    print(f"Groep {k} ({len(grp)}): " + ", ".join(grp))