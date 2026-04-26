from pathlib import Path


def ouvrirYAML(nomFichier):
    chemin = Path(nomFichier)
    with chemin.open("r", encoding="utf-8") as flux:
        lignes = flux.readlines()

    result = []
    current = None

    for ligne in lignes:
        stripped = ligne.rstrip("\n")
        if stripped.startswith("- "):
            if current is not None:
                result.append(current)
            current = {}
            contenu = stripped[2:]
            if ":" in contenu:
                cle, val = contenu.split(":", 1)
                current[cle.strip()] = _convertir(val.strip())
        elif stripped.startswith("  ") and current is not None:
            contenu = stripped.strip()
            if ":" in contenu:
                cle, val = contenu.split(":", 1)
                current[cle.strip()] = _convertir(val.strip())

    if current is not None:
        result.append(current)

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
