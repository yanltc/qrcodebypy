import random

while True:
    choix = ["pierre", "papier", "ciseaux"]
    ordi = random.choice(choix)
    utilisateur = input("Veuillez entrez votre choix (pierre, papier, ciseaux) : ")

    print("L'ordinateur a choisi : ", ordi)

    if utilisateur == ordi:
        print("Vous venez de faire un match nul!")
    elif utilisateur == "pierre" and ordi == "ciseaux":
        print("Vous avez gagné!😂")
    elif utilisateur == "papier" and ordi == "pierre":
        print("Vous avez gagné!😂")
    elif utilisateur == "ciseaux" and ordi == "papier":
        print("Vous avez gagné!😂")
    else:
        print("Vous avez perdu! 🤦‍♂️")

    rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").lower()
    if rejouer != "oui":
        print("Merci d'avoir joué !")
        break
