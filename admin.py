from users import User
from produit import Produit
class Admin(User):
    
    def __init__(self, id_user, nom_user, prenom_user, mot_de_passe, telephone, role):
        super().__init__(id_user, nom_user, prenom_user, mot_de_passe, telephone, role)
       
    def ajouter_produit(self, id_produit, libelle, date, prix):
        nouveau_produit = Produit(id_produit, libelle, date, prix)
        Produit.liste_produits.append(nouveau_produit)
        print(f"Le produit {libelle} a été ajouté avec succès.")
        print(f"Le stock est maintenant à : {len(Produit.liste_produits)}")   
        print(f"Auteur de l'ajout : {self.nom_user}")     

