import csv

with open("mesure.csv") as f:
    reader = csv.DictReader(f,delimiter=";")
    theoricals = []
    mesures = []
    for row in reader:
        theorical = float(row["good"])
        mesure = float(row["bad"])
        theoricals.append(theorical)
        mesures.append(mesure)

print(mesures)

import numpy as np

t = np.array(theoricals)
m = np.array(mesures)
diff = m - t
print(diff)
quadratic = np.square(m-t)
print(quadratic)




