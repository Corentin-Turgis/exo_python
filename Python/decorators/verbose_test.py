import functools
from colorama import Fore, Style

def verbose_params(func):
    """
    Décorateur qui affiche les arguments
    passés à la fonction, puis exécute la fonction.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(Fore.CYAN + f"[verbose_params] Appel de '{func.__name__}' avec :")
        print("  - args:", args)
        print("  - kwargs:", kwargs)
        print(Style.RESET_ALL)
        return func(*args, **kwargs)
    return wrapper

def verbose_return(func):
    """
    Décorateur qui exécute la fonction et affiche ensuite sa valeur de retour.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(Fore.BLUE + f"[verbose_return] La fonction '{func.__name__}' retourne : {result}")
        print(Style.RESET_ALL)
        return result
    return wrapper

def verbose_params_no_exec(func):
    """
    Décorateur qui affiche les arguments (positionnels et mots-clés)
    avec lesquels la fonction serait appelée, sans exécuter la fonction.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[verbose_params_no_exec] La fonction '{func.__name__}' serait appelée avec :")
        print("  - args:", args)
        print("  - kwargs:", kwargs)
        print("[//////////////////////]")
    return wrapper

def verbose_params_end(func):
    """
    Décorateur qui exécute la fonction, puis affiche les paramètres (args et kwargs)
    avec lesquels la fonction a été appelée, après son exécution.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(Fore.LIGHTBLUE_EX + f"[verbose_params_end] Après l'exécution de '{func.__name__}':")
        print("  - args :", args)
        print("  - kwargs :", kwargs)
        print(Style.RESET_ALL)
        return result
    return wrapper

