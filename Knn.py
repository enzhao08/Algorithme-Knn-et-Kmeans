import numpy as np
import random

"""
Calcul distance
"""
def euclidienne(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


"""
Exécution du Knn
"""
def Knn(point_ref, lst_pnts, k):
    liste_distance = [(euclidienne(point_ref, p), idx) for idx, p in enumerate(lst_pnts)]
    liste_distance.sort(key=lambda x: x[0])  # Tri sur la distance
    return liste_distance[:k]  # On garde seulement les k plus proches


# Création des points
tab = [(random.randint(0, 7000), random.randint(0, 7000)) for _ in range(784)]


def main(tab, nbPoints, k):
    for _ in range(nbPoints):
        randx = random.randint(0, len(tab) - 1)
        Knn_result = Knn(tab[randx], tab, k)

        # Moyenne des k voisins
        taillex = sum(tab[i][0] for _, i in Knn_result) / k
        tailley = sum(tab[i][1] for _, i in Knn_result) / k

        # Ajout du nouveau point
        tab.append((taillex, tailley))

    return Knn_result[-1][0]  # Retourne la plus grande distance parmi les k voisins


# Nombre de paquets et de voisins
nbPoints = int(input("Donnez nombre de points : "))
k = int(input("Donnez nombre k de voisins : "))

maxrep = 0
der = main(tab, nbPoints, k)

while der > 1 and maxrep < 100:
    der = main(tab, nbPoints, k)
    maxrep += 1

print("Dernier point ajouté ->", tab[-1])
print("Nombre total de points :", len(tab))
