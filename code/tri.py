from utils import quelType


def trierFichier(data, choix, ordre):
    colonnes = list(data[0].keys())
    try:
        colonne = colonnes[int(choix) - 1]
    except (ValueError, IndexError):
        print("Colonne invalide.")
        return data

    reverse = (ordre == "2")

    def cle(ligne):
        val = ligne[colonne]
        if quelType(val) == "nombre":
            return float(val)
        return str(val).lower()

    return sorted(data, key=cle, reverse=reverse)
