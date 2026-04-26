from pathlib import Path

from parsers import parserCSV
from parsers import parserJSON
from parsers import parserYAML
from parsers import parserXML


def chargerFichier(nomFichier):
    chemin = Path(nomFichier)
    if not chemin.exists():
        print("Le fichier demandé n'existe pas.")
        return None

    extension = chemin.suffix.lstrip(".").lower()

    if extension == "csv":
        return parserCSV.ouvrirCSV(str(chemin))
    if extension == "json":
        return parserJSON.ouvrirJSON(str(chemin))
    if extension == "yaml" or extension == "yml":
        return parserYAML.ouvrirYAML(str(chemin))
    if extension == "xml":
        return parserXML.ouvrirXML(str(chemin))

    print("Extension de fichier incompatible (CSV, JSON, YAML, XML uniquement).")
    return None
