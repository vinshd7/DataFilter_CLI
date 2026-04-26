# DataFilter - Outil de Traitement de Données en Python

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)

## Contexte

Projet réalisé dans le cadre du cours **"Scripting Python"** à l'ESGI.
DataFilter est un outil en ligne de commande pour lire, parser et analyser des fichiers de données structurées (CSV, JSON, YAML, XML).

## Objectif

Développer une bibliothèque CLI polyvalente capable de :
- **Parser** différents formats de données (CSV, JSON, YAML, XML)
- **Normaliser** les données en structures unifiées
- **Filtrer et analyser** les datasets
- **Stocker et sauvegarder** les résultats

## Structure du Projet

```
DataFilter_CLI/
├── code/                           # Code source principal
│   ├── main.py                     # Point d'entrée de l'application
│   ├── interface.py                # Interface CLI et menus interactifs
│   ├── fichier.py                  # Chargement et lecture des fichiers sources
│   ├── parsers/                    # Parseurs pour chaque format de données
│   │   ├── parserCSV.py            # Parser CSV
│   │   └── parserJSON.py           # Parser JSON
│   ├── utils.py                    # Utilitaires (types, nettoyage)
│   ├── stats.py                    # Statistiques descriptives
│   ├── tri.py                      # Fonctions de tri
│   └── sauvegarde.py               # Sauvegarde des données traitées
├── donnees/                        # Fichiers de données d'exemple
│   ├── exemple.csv
│   ├── exemple.json
│   ├── exemple.yaml
│   └── exemple.xml
└── README.md                       # Ce fichier (documentation)
```

## Installation et Utilisation

### Prérequis
- Python **3.12+** installé sur votre système
- Aucun package externe requis (utilise uniquement les modules standards de Python)

### Lancer l'application

```bash
cd code/
python main.py
```

### Interagir avec DataFilter

Le programme lance un menu interactif en console :

1. **Charger un fichier** : sélectionner un fichier CSV ou JSON depuis le dossier `donnees/`
2. **Afficher les données** sous forme de tableau structuré
3. **Effectuer des statistiques** sur toutes les colonnes :
   - Colonnes numériques → min, max, moyenne
   - Colonnes booléennes (JSON natif) → % vrai / % faux
   - Colonnes texte → longueur min, max, moyenne
4. **Trier les données** par colonne, ordre croissant ou décroissant *(en cours)*
5. **Filtrer les données** *(en cours)*
6. **Sauvegarder le fichier traité** *(en cours)*

### Exemple de sortie — stats sur `exemple.json`

```
=== Statistiques pour exemple.json ===
- Nombre de lignes : 6
- Colonnes : id, nom, age, salaire, actif, ville
--- Détails ---
- id (nombre):
   - minimum : 1.0
   - maximum : 6.0
   - moyenne : 3.5
- nom (chaine):
   - minimum : 3
   - maximum : 7
   - moyenne : 5.0
- age (nombre):
   - minimum : 25.0
   - maximum : 45.0
   - moyenne : 33.8
- salaire (nombre):
   - minimum : 38000.0
   - maximum : 89000.0
   - moyenne : 59833.3
- actif (booleen):
   - % Vrai : 66.7%
   - % Faux : 33.3%
- ville (chaine):
   - minimum : 4
   - maximum : 9
   - moyenne : 6.2
```

## Fonctionnalités Implémentées

| Fonctionnalité | État | Description |
|---|---|---|
| Parser CSV | ✅ | Lecture avec `csv.DictReader`, délimiteurs personnalisables |
| Parser JSON | ✅ | Normalisation liste/dict, support imbriqué |
| Affichage en tableau | ✅ | Affichage structuré avec colonnes et lignes |
| Statistiques numériques | ✅ | Min, Max, Moyenne pour les colonnes numériques |
| Statistiques booléennes | ✅ | % Vrai / % Faux pour les colonnes booléennes (JSON) |
| Statistiques texte | ✅ | Longueur min, max, moyenne pour les colonnes texte |
| Tri des données | ✅ | Tri par colonne, ordre croissant ou décroissant |
| Filtrage avancé | ✅ | Filtre par colonne avec opérateurs (=, !=, >, <, contient…) |
| Sauvegarde des résultats | ✅ | Export CSV ou JSON dans `donnees/` |
| Parser YAML / XML | ✅ | Lecture YAML (parser natif) et XML (`xml.etree`) |

## Technologies Utilisées

- **Python 3.12** + modules standards (`csv`, `json`, `pathlib`, `dataclasses`)
- **CLI interactive** avec menus et navigation console
