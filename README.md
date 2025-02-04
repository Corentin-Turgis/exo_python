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
- **@log_verbose** : Execute params, return et params_end mais log tout dans /logs/logs.txt

### Détail des fichiers

- **main.py** :  
Point d'entrée du programme.

- **Ex4.py** :  
La classe `Ex4` va lancer la série de méthodes demandées dans l'exercice 4 via la méthode `start()`

- **Ex5.py** :  
  La classe `Ex5` va lancer la série de méthodes demandées dans l'exercice 5 via la méthode `start()`


- **utils/IP_utils.py** :    
Sert des fonctions utiles aux traitement d'Ips

- **utils/Tools_utils.py** :  
La classe `Tools` est la pour les utilitaires generiques. Principalement pour la gestion de fichier
## Exécution

Pour lancer le programme, exécutez simplement le fichier `main.py` :

```bash
python3 main.py
```

### Dépendances

- Ce projet utilise le module externe [click](https://pypi.org/project/click/) pour gérer la saisie utilisateur.
- Pour l'affichage coloré, la bibliothèque [Colorama](https://pypi.org/project/colorama/) est utilisée.
