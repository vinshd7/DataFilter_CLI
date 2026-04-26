from pathlib import Path
import xml.etree.ElementTree as ET


def ouvrirXML(nomFichier):
    chemin = Path(nomFichier)
    tree = ET.parse(str(chemin))
    root = tree.getroot()

    result = []
    for enfant in root:
        ligne = {}
        for element in enfant:
            val = element.text.strip() if element.text else ""
            ligne[element.tag] = _convertir(val)
        result.append(ligne)

    return result


def _convertir(val):
    if val.lower() == "true":
        return True
    if val.lower() == "false":
        return False
    try:
        return int(val)
    except ValueError:
        pass
    try:
        return float(val)
    except ValueError:
        pass
    return val
