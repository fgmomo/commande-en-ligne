class Produit:
    quantiteProduit = 0
    liste_produits = []
    def __init__(self,id_produit,libelle,date,prix):
        self.id_produit = id_produit
        self.libelle = libelle
        self.date = date
        self.prix = prix
        Produit.liste_produits.append(self)

    # def Ajouter_prod(self):
    #     Produit.quantiteProduit +=1
    #     print(f"Le produit {self.libelle} a ete ajoute avec success")
    #     print(f"Le stock est a : {Produit.quantiteProduit}")
        
    # def Modifier_prod(self):
    #     return ".."

    # def Supprimer_prod(self):
    #     libelle_produit = self.libelle
    #     del self
    #     Produit.quantiteProduit -=1
    #     print(f"Le produit {libelle_produit} a ete supprime")
    #     print(f"Le stock est maintenant a : {Produit.quantiteProduit}")