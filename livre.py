class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def retourner(self):
        self.disponible = True


class Membre:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            return True
        else:
            print(f"Le livre '{livre.titre}' n'est pas disponible.")
            return False

# Exemple d'utilisation :
livre1 = Livre("Le Seigneur des Anneaux", "aimande difaoui", 1954)
livre2 = Livre("1984", "George Orwell", 1949)

membre1 = Membre("aimane", "John")
membre2 = Membre("youcef", "Jane")

membre1.emprunter_livre(livre1)  # Le livre est emprunté par membre1
membre2.emprunter_livre(livre1)  # Le livre n'est pas disponible

livre1.retourner()  # Le livre est retourné à la bibliothèque

membre2.emprunter_livre(livre1)  # Le livre est emprunté par membre2

print(membre1.livres_empruntes[0].titre)  # Output: [Livre object at ...]
print(membre2.livres_empruntes[0].titre)  # Output: [Livre object at ...]
