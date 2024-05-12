class Categorie:
    def __init__(self,id_categorie,nom_categorie ):
        self.id_categorie = id_categorie
        self.nom_categorie = nom_categorie
       

    def Ajouter_cat(self):
        
        print(f"Le Categorie {self.nom_categorie} a ete ajoute avec success")
       
        
    def Modifier_cat(self):
        return ".."

    def Supprimer_cat(self):
        nom_categorie_Categorie = self.nom_categorie
        del self
        Categorie.quantiteCategorie -=1
        print(f"Le Categorie {nom_categorie_Categorie} a ete supprime")
        print(f"Le stock est maintenant a : {Categorie.quantiteCategorie}")