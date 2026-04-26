from pathlib import Path
from utils import FichierDonnees
import csv


def ouvrirCSV(nomFichier):
    chemin = Path(nomFichier)
    with chemin.open("r", encoding="utf-8", newline="") as flux:
        lecteur = csv.DictReader(flux)
        lignes = [dict(ligne) for ligne in lecteur]
    return lignes

def sauvegardeCSV(f: FichierDonnees):
    return