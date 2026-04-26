from pathlib import Path
from utils import FichierDonnees
import csv
import json


def sauvegarderFichier(f: FichierDonnees):
    if not f.data:
        print("Aucune donnée à sauvegarder.")
        input("Appuie sur Entrée pour continuer...")
        return

    print("\nChoisissez le format de sauvegarde :")
    print("1 - CSV")
    print("2 - JSON")
    print("0 - Annuler")
    choix = input("Votre choix : ").strip()

    if choix == "0":
        return

    nom_base = Path(f.nom).stem

    if choix == "1":
        chemin = Path("donnees") / f"{nom_base}_filtre.csv"
        with chemin.open("w", encoding="utf-8", newline="") as flux:
            writer = csv.DictWriter(flux, fieldnames=list(f.data[0].keys()))
            writer.writeheader()
            writer.writerows(f.data)
        print(f"Fichier sauvegardé : {chemin}")

    elif choix == "2":
        chemin = Path("donnees") / f"{nom_base}_filtre.json"
        with chemin.open("w", encoding="utf-8") as flux:
            json.dump(f.data, flux, ensure_ascii=False, indent=2)
        print(f"Fichier sauvegardé : {chemin}")

    else:
        print("Choix invalide.")

    input("Appuie sur Entrée pour continuer...")
