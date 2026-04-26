from utils import quelType

def statsFichier(data, colonne):
    valeurs = [ligne[colonne] for ligne in data]
    typeVal = quelType(valeurs[0])
    taille = len(valeurs)

    if typeVal == "nombre":
        nums = [float(x) for x in valeurs]
        minimumVal = min(nums)
        maximumVal = max(nums)
        moyenneVal = sum(nums) / taille

        print(f"- {colonne} ({typeVal}):")
        print(f"   - minimum : {minimumVal}")
        print(f"   - maximum : {maximumVal}")
        print(f"   - moyenne : {moyenneVal:.1f}")

    elif typeVal == "booleen":
        nbTrue = sum(1 for x in valeurs if x)
        pourcVrai = nbTrue / taille * 100
        pourcFaux = 100 - pourcVrai

        print(f"- {colonne} ({typeVal}):")
        print(f"   - % Vrai : {pourcVrai:.1f}%")
        print(f"   - % Faux : {pourcFaux:.1f}%")

    elif typeVal in ("liste", "chaine"):
        longueurs = [len(x) for x in valeurs]
        minimumVal = min(longueurs)
        maximumVal = max(longueurs)
        moyenneVal = sum(longueurs) / taille

        print(f"- {colonne} ({typeVal}):")
        print(f"   - minimum : {minimumVal}")
        print(f"   - maximum : {maximumVal}")
        print(f"   - moyenne : {moyenneVal:.1f}")


        