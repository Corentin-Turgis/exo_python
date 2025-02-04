# Exercice Python

## Description

Ce projet est un exercice pour découvrir les bonnes pratiques en Python: modularisation, encapsulation, gestion des exceptions.

## Structure du projet

```
exo_python/
└── Python/
    ├── main.py
    ├── Ex4.py
    └── utils/
        ├── IP_utils.py
        └── Tools_utils.py
```

### Détail des fichiers

- **main.py** :  
Point d'entrée du programme.

- **Ex4.py** :  
La classe `Ex4` va lancer la série de méthodes demandées dans l'exercice 4 via la méthode `start()`

- **utils/IP_utils.py** :    
- `detect_ip_type(ip)` retourne `'IPv4'`, `'IPv6'` ou `'Bad Ip'` selon l'adresse passée.  
- `detect_multiple_ip(ips)` accepte une liste ou un dictionnaire d'IPs et affiche le résultat pour chacune d'elles (elle lève une `ValueError` si les éléments ne sont pas des chaînes de caractères).

- **utils/Tools_utils.py** :  
La classe `Tools` est la pour les utilitaires generiques.
## Exécution

Pour lancer le programme, exécutez simplement le fichier `main.py` :

```bash
python3 main.py
```

### Dépendances

Ce projet utilise le module externe [click](https://pypi.org/project/click/) pour gérer la saisie utilisateur.


