import numpy as np
y =[2, 3, 8, 4, 10, 1, 9, 5, 1, 0]

mittelwert = np.mean(y)
n = len(y)
abweichung = (y - mittelwert)**2 

summe = sum(abweichung)

varianz = 1 / n * summe
standardabweichung = np.sqrt(varianz)
print(standardabweichung)

result2 = np.std(y)
print(result2)

