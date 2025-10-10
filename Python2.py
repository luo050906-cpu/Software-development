import random
klas25a = ["Daan A", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V.", "Kateryna"]
if len(klas25a) > 2:
    namen = random.sample(klas25a, 2)
    print(f"De namen zijn {namen[0]} en {namen[1]}")