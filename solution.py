resultat = 100  # Valeur de départ
resultat = resultat * 100

for i in range(3141*2):
    if (i%2):
        resultat += 1

resultat = resultat ** 4
resultat = resultat / 1000000000000000
print("Résultat final :", resultat, "root : " , 29825402027423607 ** 0.25, "diff: ", 29825402027423607 - 13141.55**4)

resultat = 100  # Valeur de départ
resultat = resultat * 100

for i in range(130*2):
    if (i%2 != 0):
        resultat -= 10
resultat = resultat - 24/10
resultat = resultat ** 4
resultat = resultat / -1000000000000000
print("Résultat final :", resultat, "root : " , 5722615680620322 ** 0.25, "diff: ", 5722615680620322 - 8697.6**4)
