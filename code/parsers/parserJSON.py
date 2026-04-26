from pathlib import Path
from utils import FichierDonnees
import json

def ouvrirJSON(nomFichier):
    chemin = Path(nomFichier)
    with chemin.open("r", encoding="utf-8") as flux:
        donnees = json.load(flux)

    if isinstance(donnees, list):
        elements = donnees
    else:
        elements = [donnees]

    listeNormalisee = []
    for indice, element in enumerate(elements):
        if isinstance(element, dict):
            listeNormalisee.append(element)
        else:
            listeNormalisee.append({"index": indice, "value": element})

    return listeNormalisee

def sauvegardeJSON(f: FichierDonnees):
    return