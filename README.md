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

## Décorateurs pour tests

Le module `utils/decorators.py` contient plusieurs décorateurs permettant d'afficher en couleur dans la console les informations sur les appels de fonctions :


- **@verbose_params** : Affiche les paramètres (args et kwargs) avec lesquels la fonction est appelée, avant son exécution.
- **@verbose_return** : Affiche la valeur de retour de la fonction après son exécution.
- **@verbose_params_no_exec** : Affiche les paramètres qui auraient été passés à la fonction, sans exécuter celle-ci.
- **@verbose_params_end** : Affiche les paramètres avec lesquels la fonction a été appelée, après son exécution.


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

- Ce projet utilise le module externe [click](https://pypi.org/project/click/) pour gérer la saisie utilisateur.
- Pour l'affichage coloré, la bibliothèque [Colorama](https://pypi.org/project/colorama/) est utilisée.

### Décorateurs de débogage (Verbose)


- Les paramètres passés à la fonction (avant ou après son exécution).
- La valeur de retour de la fonction.