class Prospect:
    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email, age, profession, entreprise, experience, diplome='', genre=None, nationalite='', pays_origine='', langue1='', langue2='', specialisation1=None, specialisation2=None, interet1='', interet2='', interet3='', interet4='', interet5='', projet='', budget='', besoin='', priorite=''):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.age = age
        self.profession = profession
        self.entreprise = entreprise
        self.experience = experience
        self.diplome = diplome
        self.genre = genre
        self.nationalite = nationalite
        self.pays_origine = pays_origine
        self.langue1 = langue1
        self.langue2 = langue2
        self.specialisation1 = specialisation1
        self.specialisation2 = specialisation2
        self.interet1 = interet1
        self.interet2 = interet2
        self.interet3 = interet3
        self.interet4 = interet4
        self.interet5 = interet5
        self.projet = projet
        self.budget = budget
        self.besoin = besoin
        self.priorite = priorite

    def get_nom(self):
        return self.nom
    
    def set_nom(self, nouveau_nom):
        self.nom = nouveau_nom
    
    def get_prenom(self):
        return self.prenom
    
    def set_prenom(self, nouveau_prenom):
        self.prenom = nouveau_prenom
        
    def get_date_naissance(self):
        return self.date_naissance
    
    def set_date_naissance(self, nouvelle_date_naissance):
        self.date_naissance = nouvelle_date_naissance
    
    def get_adresse(self):
        return self.adresse
    
    def set_adresse(self, nouvelle_adresse):
        self.adresse = nouvelle_adresse
        
    def get_telephone(self):
        return self.telephone
    
    def set_telephone(self, nouveau_telephone):
        self.telephone = nouveau_telephone
    
    def get_email(self):
        return self.email
    
    def set_email(self, nouveau_email):
        self.email = nouveau_email
        
    def get_age(self):
        return self.age
    
    def set_age(self, nouvel_age):
        self.age = nouvel_age
    
    def get_profession(self):
        return self.profession
    
    def set_profession(self, nouvelle_profession):
        self.profession = nouvelle_profession
        
    def get_entreprise(self):
        return self.entreprise
    
    def set_entreprise(self, nouvelle_entreprise):
        self.entreprise = nouvelle_entreprise
    
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
        return self
    
    def set_pays_origine(self, pays_origine):
        self.pays_origine=pays_origine
    
     # getters et setters pour l'attribut langue1
    def get_langue1(self):
        return self.langue1
    
    def set_langue1(self, nouvelle_langue):
        self.langue1 = nouvelle_langue
    
    # getters et setters pour l'attribut langue2
    def get_langue2(self):
        return self.langue2
    
    def set_langue2(self, nouvelle_langue):
        self.langue2 = nouvelle_langue
    
    # getters et setters pour l'attribut specialisation1
    def get_specialisation1(self):
        return self.specialisation1
    
    def set_specialisation1(self, nouvelle_specialisation):
        self.specialisation1 = nouvelle_specialisation
    
    # getters et setters pour l'attribut specialisation2
    def get_specialisation2(self):
        return self.specialisation2
    
    def set_specialisation2(self, nouvelle_specialisation):
        self.specialisation2 = nouvelle_specialisation
    
    # getters et setters pour l'attribut niveau_etude
    def get_niveau_etude(self):
        return self.niveau_etude
    
    def set_niveau_etude(self, nouveau_niveau):
        self.niveau_etude = nouveau_niveau
    
    # getters et setters pour l'attribut diplome
    def get_diplome(self):
        return self.diplome
    
    def set_diplome(self, nouveau_diplome):
        self.diplome = nouveau_diplome
    
    # getters et setters pour l'attribut experience
    def get_experience(self):
        return self.experience
    
    def set_experience(self, nouvelle_experience):
        self.experience = nouvelle_experience
    
    # getters et setters pour l'attribut entreprise
    def get_entreprise(self):
        return self.entreprise
    
    def set_entreprise(self, nouvelle_entreprise):
        self.entreprise = nouvelle_entreprise
    
    # getters et setters pour l'


    def get_interet1(self):
        return self.interet1

    def set_interet1(self, nouvel_interet):
        self.interet1 = nouvel_interet

    def get_interet2(self):
        return self.interet2

    def set_interet2(self, nouvel_interet):
        self.interet2 = nouvel_interet

    def get_interet3(self):
        return self.interet3

    def set_interet3(self, nouvel_interet):
        self.interet3 = nouvel_interet

    def get_interet4(self):
        return self.interet4

    def set_interet4(self, nouvel_interet):
        self.interet4 = nouvel_interet

    def get_interet5(self):
        return self.interet5

    def set_interet5(self, nouvel_interet):
        self.interet5 = nouvel_interet

    def get_projet(self):
        return self.projet

    def set_projet(self, nouveau_projet):
        self.projet = nouveau_projet

    def get_budget(self):
        return self.budget

    def set_budget(self, nouveau_budget):
        self.budget = nouveau_budget

    def get_besoin(self):
        return self.besoin

    def set_besoin(self, nouveau_besoin):
        self.besoin = nouveau_besoin

    def get_priorite(self):
        return self.priorite

    def set_priorite(self, nouvelle_priorite):
        self.priorite = nouvelle_priorite