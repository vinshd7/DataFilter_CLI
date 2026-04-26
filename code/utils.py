from dataclasses import dataclass, field
from typing import List, Dict, Any
import os

@dataclass
class FichierDonnees:
    nom: str =""
    extension: str = ""
    data: List[Dict[str, Any]] = field(default_factory=list)


def quelType(val):
    if isinstance(val, bool):
        return "booleen"
    if isinstance(val, (int, float)):
        return "nombre"
    if isinstance(val, list):
        return "liste"
    if isinstance(val, str):
        try:
            float(val)
            return "nombre"
        except ValueError:
            return "chaine"
    return "chaine"


def clear():
    # windows : cls
    # linux/mac : clear
    os.system("cls" if os.name == "nt" else "clear")


