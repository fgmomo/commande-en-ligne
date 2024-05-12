from produit import Produit
from categorie import Categorie
from users import User
from admin import Admin

admin = Admin(1, "Admin", "Admin", "motdepasse", "123456789", "admin")
admin.ajouter_produit(1, " portable", "2024-05-10", 1200)
admin2 = Admin(2, "Admin2", "Admin2", "motdepasse", "123456789", "admin")
admin2.ajouter_produit(1, "Ordinateur portable", "2024-05-10", 1200)

 
 

# cat1 = Categorie(1,"scolaire")
# cat2 = Categorie(2,"electro" )
# cat1.Ajouter_cat()
# cat2.Ajouter_cat()
