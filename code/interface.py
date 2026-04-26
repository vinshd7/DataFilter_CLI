from pathlib import Path

from utils import FichierDonnees, clear, quelType
from stats import statsFichier
from tri import trierFichier
from sauvegarde import sauvegarderFichier
import fichier


def afficherData(data):
    if not data:
        print("Aucune donnée.")
        return

    colonnes = list(data[0].keys())
    print(" | ".join(colonnes))
    print("-" * (4 * len(colonnes) + 3))

    for ligne in data:
        valeurs = [str(ligne[col]) for col in colonnes]
        print(" | ".join(valeurs))


def menuAccueil(f: FichierDonnees):
    while True:
        clear()
        print("\n=== Bienvenu sur le menu data filter ===")
        print("1 - Choisir un fichier")
        print("0 - Quitter")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            menuChoixFichier(f)
        elif choix == "0":
            print("Au revoir.")
            break
        else:
            print("Choix invalide, réessaie.")


def menuChoixFichier(f: FichierDonnees):
    clear()
    dossier = Path("donnees")
    fichiers = [p for p in dossier.iterdir() if p.is_file()] if dossier.exists() else []

    if not fichiers:
        print("Aucun fichier n'est présent dans le dossier donnees")
        return

    print("\n=== Fichiers disponibles ===")
    for index, chemin in enumerate(fichiers, start=1):
        print(f"{index} - {chemin.name}")

    while True:
        print("\n=== Choix du fichier ===")
        print("Entre le numéro du fichier choisi")
        print("0 - Retour")
        choix = input("Votre choix : ").strip()

        if choix == "0":
            return

        try:
            numero = int(choix)
        except ValueError:
            print("Choix invalide, réessaie.")
            continue

        if 1 <= numero <= len(fichiers):
            cheminFichier = fichiers[numero - 1]
            donnees = fichier.chargerFichier(str(cheminFichier))

            if donnees is None:
                return

            f.nom = cheminFichier.name
            f.extension = cheminFichier.suffix.lstrip(".")
            f.data = donnees

            menuBaseFichier(f)
            return
        else:
            print("Choix invalide, réessaie.")


def menuBaseFichier(f: FichierDonnees):
    while True:
        clear()
        print(f"\n=== {f.nom} ===\n")
        afficherData(f.data)
        print("\nVeuillez choisir le traitement à appliquer :")
        print(" 1 - Afficher les stats du fichier")
        print(" 2 - Filtrer des données")
        print(" 3 - Trier les données")
        print(" 4 - Sauvegarder le fichier")
        print(" 5 - Revenir au menu principal")
        choix = input("Votre choix : ").strip()

        if choix == "1":
            afficherStats(f)
        elif choix == "2":
            menuFiltre(f)
        elif choix == "3":
            menuTri(f)
        elif choix == "4":
            sauvegarderFichier(f)
        elif choix == "5":
            return
        else:
            print("Choix invalide, réessaie.")


def afficherStats(f: FichierDonnees):
    clear()
    if not f.data:
        print("Aucune donnée n'est chargée.")
        return

    colonnes = list(f.data[0].keys())
    print(f"\n=== Statistiques pour {f.nom} ===")
    print(f"- Nombre de lignes : {len(f.data)}")
    print(f"- Colonnes : {', '.join(colonnes)}")
    print(f"--- Détails ---")
    for colonne in colonnes:
        statsFichier(f.data, colonne)
    input("\nAppuie sur Entrée pour revenir au menu...")


def menuFiltre(f: FichierDonnees):
    clear()
    if not f.data:
        print("Aucune donnée chargée.")
        input("Appuie sur Entrée pour continuer...")
        return

    colonnes = list(f.data[0].keys())
    print(f"\n=== Filtrage pour {f.nom} ===")
    print("Choisissez la colonne à filtrer :")
    for i, col in enumerate(colonnes, start=1):
        print(f"{i} - {col}")
    print("0 - Retour")

    choix = input("Votre choix : ").strip()
    if choix == "0":
        return

    try:
        colonne = colonnes[int(choix) - 1]
    except (ValueError, IndexError):
        print("Choix invalide.")
        input("Appuie sur Entrée pour continuer...")
        return

    typeVal = quelType(f.data[0][colonne])

    print(f"\nOpérateur pour '{colonne}' ({typeVal}) :")
    if typeVal == "nombre":
        operateurs = ["=", "!=", ">", "<", ">=", "<="]
    elif typeVal == "booleen":
        operateurs = ["=", "!="]
    else:
        operateurs = ["=", "!=", "contient"]

    for i, op in enumerate(operateurs, start=1):
        print(f"{i} - {op}")

    choixOp = input("Votre choix : ").strip()
    try:
        operateur = operateurs[int(choixOp) - 1]
    except (ValueError, IndexError):
        print("Choix invalide.")
        input("Appuie sur Entrée pour continuer...")
        return

    valeur = input("Valeur à comparer : ").strip()

    resultats = []
    for ligne in f.data:
        val = ligne[colonne]

        if typeVal == "nombre":
            try:
                val_num = float(val)
                val_cmp = float(valeur)
                if operateur == "=" and val_num == val_cmp:
                    resultats.append(ligne)
                elif operateur == "!=" and val_num != val_cmp:
                    resultats.append(ligne)
                elif operateur == ">" and val_num > val_cmp:
                    resultats.append(ligne)
                elif operateur == "<" and val_num < val_cmp:
                    resultats.append(ligne)
                elif operateur == ">=" and val_num >= val_cmp:
                    resultats.append(ligne)
                elif operateur == "<=" and val_num <= val_cmp:
                    resultats.append(ligne)
            except ValueError:
                pass

        elif typeVal == "booleen":
            val_bool = valeur.lower() in ("true", "vrai", "1")
            if operateur == "=" and val == val_bool:
                resultats.append(ligne)
            elif operateur == "!=" and val != val_bool:
                resultats.append(ligne)

        else:
            val_str = str(val).lower()
            val_cmp = valeur.lower()
            if operateur == "=" and val_str == val_cmp:
                resultats.append(ligne)
            elif operateur == "!=" and val_str != val_cmp:
                resultats.append(ligne)
            elif operateur == "contient" and val_cmp in val_str:
                resultats.append(ligne)

    print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
    afficherData(resultats)

    appliquer = input("\nAppliquer ce filtre aux données ? (o/n) : ").strip().lower()
    if appliquer == "o":
        f.data = resultats
        print("Filtre appliqué.")

    input("Appuie sur Entrée pour continuer...")


def menuTri(f: FichierDonnees):
    clear()
    print(f"\n=== Tri pour {f.nom} ===")
    print(f"Veuillez choisir la colonne de tri")
    colonnes = list(f.data[0].keys())
    for i, colonne in enumerate(colonnes, start=1):
        print(f"{i} - {colonne}")
    choix = input("Votre choix : ").strip()
    print(f"Veuillez choisir l'ordre du tri")
    print(f"1 - croissant")
    print(f"2 - décroissant")
    ordre = input("Votre choix : ").strip()
    f.data = trierFichier(f.data, choix, ordre)
