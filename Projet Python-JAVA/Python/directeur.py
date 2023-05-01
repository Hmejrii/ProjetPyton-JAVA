import random

class Directeur:
    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email, age, salaire_annuel, experience, diplome, genre, nationalite, pays_origine, langue1, langue2, specialisation1, specialisation2, bureau, disponibilite, entreprise):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.age = age
        self.salaire_annuel = salaire_annuel
        self.experience = experience
        self.diplome = diplome
        self.genre = genre
        self.nationalite = nationalite
        self.pays_origine = pays_origine
        self.langue1 = langue1
        self.langue2 = langue2
        self.specialisation1 = specialisation1
        self.specialisation2 = specialisation2
        self.bureau = bureau
        self.disponibilite = disponibilite
        self.entreprise = entreprise
        
    def __init__(self):
        self.Directeur= {}






    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.date_naissance = ""
        self.adresse = ""
        self.telephone = ""
        self.email = ""
        self.age = 0
        self.salaire_annuel = 0
        self.experience = ""
        self.diplome = ""
        self.genre = ""
        self.nationalite = ""
        self.pays_origine = ""
        self.langue1 = ""
        self.langue2 = ""
        self.specialisation1 = ""
        self.specialisation2 = ""
        self.bureau = ""
        self.disponibilite = ""
        self.entreprise = ""
        
        attributs_aleatoires = ["Informatique", "Finance", "Marketing", "Ressources Humaines", "Communication", "Logistique", "Juridique"]
        self.specialisation1 = random.choice(attributs_aleatoires)
        self.specialisation2 = random.choice(attributs_aleatoires)
        self.disponibilite = random.choice(["Plein temps", "Partiel", "Mi-temps"])
        self.entreprise = random.choice(["Entreprise A", "Entreprise B", "Entreprise C", "Entreprise D"])



 # Getters et Setters pour nom
    def get_nom(self):
        return self.nom

    def set_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    # Getters et Setters pour prenom
    def get_prenom(self):
        return self.prenom

    def set_prenom(self, nouveau_prenom):
        self.prenom = nouveau_prenom

    # Getters et Setters pour date_naissance
    def get_date_naissance(self):
        return self.date_naissance

    def set_date_naissance(self, nouvelle_date_naissance):
        self.date_naissance = nouvelle_date_naissance

    # Getters et Setters pour adresse
    def get_adresse(self):
        return self.adresse

    def set_adresse(self, nouvelle_adresse):
        self.adresse = nouvelle_adresse

    # Getters et Setters pour telephone
    def get_telephone(self):
        return self.telephone

    def set_telephone(self, nouveau_telephone):
        self.telephone = nouveau_telephone

    # Getters et Setters pour email
    def get_email(self):
        return self.email

    def set_email(self, nouvel_email):
        self.email = nouvel_email

    # Getters et Setters pour age
    def get_age(self):
        return self.age

    def set_age(self, nouvel_age):
        self.age = nouvel_age

    
    
    def get_salaire_annuel(self):
        return self.salaire_annuel
    
    def set_salaire_annuel(self, nouveau_salaire):
        self.salaire_annuel = nouveau_salaire
        
    def get_experience(self):
        return self.experience
    
    def set_experience(self, nouvelle_experience):
        self.experience = nouvelle_experience
        
    def get_diplome(self):
        return self.diplome
    
    def set_diplome(self, nouveau_diplome):
        self.diplome = nouveau_diplome
        
    def get_genre(self):
        return self.genre
    
    def set_genre(self, nouveau_genre):
        self.genre = nouveau_genre
        
    def get_nationalite(self):
        return self.nationalite
    
    def set_nationalite(self, nouvelle_nationalite):
        self.nationalite = nouvelle_nationalite
        
    def get_pays_origine(self):
        return self.pays_origine
    
    def set_pays_origine(self, nouveau_pays_origine):
        self.pays_origine = nouveau_pays_origine
        
    def get_langue1(self):
        return self.langue1
    
    def set_langue1(self, nouvelle_langue1):
        self.langue1 = nouvelle_langue1
        
    def get_langue2(self):
        return self.langue2
    
    def set_langue2(self, nouvelle_langue2):
        self.langue2 = nouvelle_langue2
        
    def get_specialisation1(self):
        return self.specialisation1
    
    def set_specialisation1(self, nouvelle_specialisation1):
        self.specialisation1 = nouvelle_specialisation1
        
    def get_specialisation2(self):
        return self.specialisation2
    
    def set_specialisation2(self, nouvelle_specialisation2):
        self.specialisation2 = nouvelle_specialisation2
        
    def get_bureau(self):
        return self.bureau
    
    def set_bureau(self, nouveau_bureau):
        self.bureau = nouveau_bureau
        
    def get_disponibilite(self):
        return self.disponibilite
    
    def set_disponibilite(self, nouvelle_disponibilite):
        self.disponibilite = nouvelle_disponibilite
        
    def get_entreprise(self):
        return self.entreprise
    
    def set_entreprise(self, nouvelle_entreprise):
        self.entreprise = nouvelle_entreprise


