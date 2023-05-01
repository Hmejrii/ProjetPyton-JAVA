class Etudiant:

    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email, age, sexe, nationalite, filiere, annee_etude, groupe, niveau, langue1, langue2, note1, note2, note3, moyenne, mention):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.age = age
        self.sexe = sexe
        self.nationalite = nationalite
        self.filiere = filiere
        self.annee_etude = annee_etude
        self.groupe = groupe
        self.niveau = niveau
        self.langue1 = langue1
        self.langue2 = langue2
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3
        self.moyenne = (note1 + note2 + note3) / 3
        self.mention = self.mention
 

    def __init__(self):
        self.etudiant={}
    


       
     # Getter et Setter pour l'attribut "nom"
        def get_nom(self):
            return self._nom
        
        def set_nom(self, nom):
            self._nom = nom
        
        # Getter et Setter pour l'attribut "prenom"
        def get_prenom(self):
            return self._prenom
        
        def set_prenom(self, prenom):
            self._prenom = prenom
        
        # Getter et Setter pour l'attribut "date_naissance"
        def get_date_naissance(self):
            return self._date_naissance
        
        def set_date_naissance(self, date_naissance):
            self._date_naissance = date_naissance
        
        # Getter et Setter pour l'attribut "adresse"
        def get_adresse(self):
            return self._adresse
        
        def set_adresse(self, adresse):
            self._adresse = adresse
        
        # Getter et Setter pour l'attribut "telephone"
        def get_telephone(self):
            return self._telephone
        
        def set_telephone(self, telephone):
            self._telephone = telephone
        
        # Getter et Setter pour l'attribut "email"
        def get_email(self):
            return self._email
        
        def set_email(self, email):
            self._email = email

            # Getter et Setter pour l'attribut "sage"
        def get_age(self):
            return self.age
        
        def set_age(self, age):
            self._age = age
    
        
    def calculer_mention(self):
        if self.moyenne >= 16:
            return "Très bien"
        elif self.moyenne >= 14:
            return "Bien"
        elif self.moyenne >= 12:
            return "Assez bien"
        elif self.moyenne >= 10:
            return "Passable"
        else:
            return "Échec"
        
    # Getter et Setter pour l'attribut sexe
    def get_sexe(self):
        return self.sexe
    
    def set_sexe(self, nouveau_sexe):
        self.sexe = nouveau_sexe
    
    # Getter et Setter pour l'attribut nationalite
    def get_nationalite(self):
        return self.nationalite
    
    def set_nationalite(self, nouvelle_nationalite):
        self.nationalite = nouvelle_nationalite
        
    # Getter et Setter pour l'attribut filiere
    def get_filiere(self):
        return self.filiere
    
    def set_filiere(self, nouvelle_filiere):
        self.filiere = nouvelle_filiere
    
    # Getter et Setter pour l'attribut annee_etude
    def get_annee_etude(self):
        return self.annee_etude
    
    def set_annee_etude(self, nouvelle_annee):
        self.annee_etude = nouvelle_annee
    
    # Getter et Setter pour l'attribut groupe
    def get_groupe(self):
        return self.groupe
    
    def set_groupe(self, nouveau_groupe):
        self.groupe = nouveau_groupe
        
    # Getter et Setter pour l'attribut niveau
    def get_niveau(self):
        return self.niveau
    
    def set_niveau(self, nouveau_niveau):
        self.niveau = nouveau_niveau
    
    # Getter et Setter pour l'attribut langue1
    def get_langue1(self):
        return self.langue1
    
    def set_langue1(self, nouvelle_langue):
        self.langue1 = nouvelle_langue
    
    # Getter et Setter pour l'attribut langue2
    def get_langue2(self):
        return self.langue2
    
    def set_langue2(self, nouvelle_langue):
        self.langue2 = nouvelle_langue
    
    # Getter et Setter pour l'attribut note1
    def get_note1(self):
        return self.note1
    
    def set_note1(self, note1):

        self.note2=note1
 # Getter et Setter pour l'attribut note2
    def get_note2(self):
        return self.note2
    
    def set_note2(self, note2):

        self.note2=note2
     # Getter et Setter pour l'attribut note3
    def get_note3(self):
        return self.note3
    
    def set_note3(self, note3):

        self.note3=note3

    
    def get_moyenne(self):
        return self._moyenne

    # Setter pour moyenne
    def set_moyenne(self, nouvelle_moyenne):
        if nouvelle_moyenne < 0 or nouvelle_moyenne > 20:
            raise ValueError("La moyenne doit être comprise entre 0 et 20.")
        self._moyenne = nouvelle_moyenne
        if nouvelle_moyenne < 10:
            self._mention = "Non admis"
        elif nouvelle_moyenne < 12:
            self._mention = "Passable"
        elif nouvelle_moyenne < 14:
            self._mention = "Assez bien"
        elif nouvelle_moyenne < 16:
            self._mention = "Bien"
        else:
            self._mention = "Très bien"

    # Getter pour mention
    def get_mention(self):
        return self._mention
    
    def set_mention(self, mention):
        self.mention=mention


    
        






     