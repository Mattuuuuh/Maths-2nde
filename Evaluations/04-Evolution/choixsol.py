def choix(prix_panier):
    if prix_panier < 60:
        return "Choisir le premier bon."
    if prix_panier == 60:
        return "Les deux bons sont équivalents."
    if prix_panier > 60:
        return "Choisir le deuxième bon."
