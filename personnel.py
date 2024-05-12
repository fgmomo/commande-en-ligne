from users import User
from produit import Produit
class Personnel(User):
    
    def __init__(self, id_user, nom_user, prenom_user, mot_de_passe, telephone, role):
        super().__init__(id_user, nom_user, prenom_user, mot_de_passe, telephone, role)
      