###########								###########
###									     	###
###	Simulation avec classement du niveau de bienveillance des personnes.	###
###										###
##########								###########

## By Just4Dahu
## https://github.com/Just4Dahu


import random

class Participant:
    def __init__(self, nom):
        self.nom = nom
        self.points = 0

    def ajouter_points(self, points):
        self.points += points

participants = [
    Participant("Eliott"),
    Participant("Grégorie"),
    Participant("Clement"),
    Participant("Damien")
]

actions = {
    "Confident de X": 5,
    "!! Masterclass !! à sucer X": 3,
    "Fait un cadeau à X": 1,
    "Féliciter X pour son succès récent": 2,
    " "
}

def simuler_action(participant, action):
    if action in actions:
        participant.ajouter_points(actions[action])

def game(participants, nombre_de_tours):
    for tour in range(nombre_de_tours):
        print(f"\nTour {tour + 1} :")
        for participant in participants:
            action_aleatoire = random.choice(list(actions.keys()))
            simuler_action(participant, action_aleatoire)
            print(f"{participant.nom} a effectué l'action : {action_aleatoire} et a maintenant {participant.points} points.")
        
        # Appeler la fonction classement à la fin de chaque tour
        classement(participants)


def classement(participants):
    # Trier les participants en fonction de leurs points
    participants_tries = sorted(participants, key=lambda x: x.points, reverse=True)

    # Afficher le classement en CLI
    print("\nClassement:")
    for i, participant in enumerate(participants_tries, 1):
        print(f"{i}. {participant.nom}: {participant.points} Points")

# Spécifier le nombre de tours
nombre_de_tours = int(input("Entrez le nombre de tours pour la partie : "))

# Appeler la fonction game avec le nombre de tours spécifié
game(participants, nombre_de_tours)
