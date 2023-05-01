import random
import datetime
import re

class Personnel:
 
 ### Contructeur avec des attributs ###
    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email, age):
        # Informations de base
        self.nom = self.valider_nom(nom)
        self.prenom = self.valider_prenom(prenom)
        self.date_naissance = self.valider_date_naissance(date_naissance)                   ### appel au méthodes de vérification ###
        self.adresse =self.adresse
        self.telephone = self.valider_numero_telephone(telephone)
        self.email = self.valider_email(email)
        self.age=self.valider_age(age)

  ### Contructeur sans attribut
    def __init__(self):
         self.Personnel= {}
    ### constructeur avec des attributs aléatoire 


    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email,age):
        self.nom=nom
        self.prenom=prenom
        self.date_naissance=date_naissance
        self.adresse=adresse
        self.telephone=telephone
        self.email=email
        self.age = random.randint(20, 60)

        ################### vérication des données entrées #########


    def valider_nom(self, nom):
        if not nom.isalpha():
            raise ValueError("Le nom ne doit contenir que des lettres")
        return nom
    
    def valider_prenom(self, prenom):
        if not prenom.isalpha():
            raise ValueError("Le prénom ne doit contenir que des lettres")
        return prenom
    
    def valider_date_naissance(self, date_naissance):
        try:
            datetime.datetime.strptime(date_naissance, '%Y-%m-%d')
        except ValueError:
            raise ValueError("La date de naissance doit être au format AAAA-MM-JJ")
        return date_naissance
    
    def valider_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("L'adresse email est invalide")
        return email
    
    def valider_numero_telephone(self, numero_telephone):
        if not re.match(r"^(?:\+212|0)[1-9][0-9]{8}$", numero_telephone):
            raise ValueError("Le numéro de téléphone est invalide")
        return numero_telephone
    
    def valider_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("L'âge doit être un nombre positif")
        return age




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

    ########## instance de classe personnel 

    
personne1l = Personnel("Dupont", "Jean", "1990-01-01", "10 Rue de la Paix, Paris", "+33 6 12 34 56 78", "jean.dupont@example.com", 33)
personnel2 = Personnel("Martin", "Sophie", "1985-05-12", "20 Rue des Lilas, Lyon", "+33 6 23 45 67 89", "sophie.martin@example.com", 38)
personnel3 = Personnel("Garcia", "Pablo", "1978-08-25", "30 Rue du Commerce, Marseille", "+33 6 34 56 78 90", "pablo.garcia@example.com", 43)
personnel4 = Personnel("Nguyen", "Thi", "1995-02-18", "40 Rue de la Liberté, Lille", "+33 6 45 67 89 01", "thi.nguyen@example.com", 28)
personnel5 = Personnel("Rousseau", "Lucie", "1998-11-03", "50 Rue de la République, Bordeaux", "+33 6 56 78 90 12", "lucie.rousseau@example.com", 23)
personne6 = Personnel("Lefebvre", "Marie", "17/08/1998", "7 rue de la Liberté", "0789564123", "marie.lefebvre@outlook.com", 23)
personne7 = Personnel("Nguyen", "Thi", "23/06/1989", "23 rue des Lilas", "0132548967", "thi.nguyen@gmail.com", 32)
personne8 = Personnel("Ali", "Ahmed", "12/04/1985", "50 avenue de la République", "0654789251", "ahmed.ali@hotmail.com", 36)
personne9 = Personnel("Bouvier", "Franck", "08/02/1991", "9 avenue du Soleil", "0689741236", "franck.bouvier@free.fr", 30)
personne10 = Personnel("Tremblay", "Sophie", "25/12/1980", "3 rue des Roses", "0612356897", "sophie.tremblay@orange.fr", 41)


class Professeur(Personnel):
    # Attribut de classe
  
    
    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email,age, matiere_enseignee, anciennete, diplome='', genre=None, nationalite='', pays_origine='',langue1= '', langue2='', specialisation1=None, specialisation2=None, classe1='', classe2='', grade='', disponibilite='', experience='', competence=''):
        super().__init__(nom, prenom, date_naissance, adresse, telephone, email,age)

        # Informations de professeur
        self.matiere_enseignee = matiere_enseignee
        self.anciennete = anciennete
        self.diplome = diplome
        self.genre = genre
        self.nationalite = nationalite
        self.pays_origine = pays_origine
        self.langue1 = langue1
        self.langue2 = langue2
        self.specialisation1 = specialisation1
        self.specialisation2 = specialisation2
        self.classe1 = classe1
        self.classe2 = classe2
        self.grade = grade
        self.disponibilite = disponibilite
        self.experience = experience
        self.competence = competence
     ### Contructeur sans attribut
    def __init__(self):
         self.Professeur= {}
    ### constructuer avec des randoms attributs 




# Getter pour l'attribut matiere_enseignee

    def matiere_enseignee(self):
        return self._matiere_enseignee

    # Setter pour l'attribut matiere_enseignee
   
    def matiere_enseignee(self, value):
        self._matiere_enseignee = value

    # Getter pour l'attribut anciennete
  
    def anciennete(self):
        return self._anciennete

    # Setter pour l'attribut anciennete
   
    def anciennete(self, value):
        self._anciennete = value

    # Getter pour l'attribut diplome
   
    def diplome(self):
        return self._diplome

    # Setter pour l'attribut diplome
   
    def diplome(self, value):
        self._diplome = value

    # Getter pour l'attribut genre
    
    def genre(self):
        return self._genre

    # Setter pour l'attribut genre
   
    def genre(self, value):
        self._genre = value

    # Getter pour l'attribut nationalite
    
    def nationalite(self):
        return self._nationalite

    # Setter pour l'attribut nationalite
   
    def nationalite(self, value):
        self._nationalite = value

    # Getter pour l'attribut pays_origine
    
    def pays_origine(self):
        return self._pays_origine

    # Setter pour l'attribut pays_origine
    @pays_origine.setter
    def pays_origine(self, value):
        self._pays_origine = value

    # Getter pour l'attribut langue1
    
    def langue1(self):
        return self._langue1

    # Setter pour l'attribut langue1

    def langue1(self, value):
        self._langue1 = value

    # Getter pour l'attribut langue2

    def langue2(self):
        return self._langue2

    # Setter pour l'attribut langue2
 
    def langue2(self, value):
        self._langue2 = value

    # Getter pour l'attribut specialisation1
   
    def specialisation1(self):
        return self._specialisation1

    # Setter pour l'attribut specialisation1
  
    def specialisation1(self, value):
        self._specialisation1 = value

    # Getter pour l'attribut specialisation2
   
    def specialisation2(self):
        return self._specialisation2

    # Setter pour l'attribut specialisation2
 
    def specialisation2(self, value):
        self._specialisation2 = value

    # Getter pour l'attribut classe1
 
    def classe1(self):
        return self._classe1

    # Setter pour l'attribut classe1
    @classe1.setter
    def classe1(self, value):
        self._classe1 = value

    # Getter pour l'attribut classe2

    def classe2(self):
        return self._classe2

    # Setter pour l'attribut classe2
  
    def classe2(self, value):
        self._classe2 = value

    # Getter pour l'attribut grade

    def grade(self):
        return self._grade

    # Setter pour l'attribut grade
 
    def grade(self, value):
        self._grade = value

    # Getter pour l'attribut disponibilite

    def disponibilite(self):
        return self._disponibilite

    # Setter pour l'attribut disponibilite
 
    def disponibilite(self, value):
        self._disponibilite = value

    # Getter pour l'attribut experience

    def experience(self):
        return self._experience

    # Setter pour l'attribut experience

    def experience(self, value):
        self._experience = value


prof1 = Professeur("Dupont", "Jean", "1990-01-01", "10 Rue de la Paix, Paris", "+33 6 12 34 56 78", "jean.dupont@example.com", 33, "Mathématiques", 5, 'Doctorat','Homme','Française', 'France', 'Français', 'Anglais', 'Analyse', 'Algèbre', 'L1', 'L2', 'Professeur', 'À temps plein', '10 ans', 'Pédagogie')
prof2 = Professeur("Martin", "Sophie", "1985-05-12", "20 Rue des Lilas, Lyon", "+33 6 23 45 67 89", "sophie.martin@example.com", 38, "Physique", 7, 'Doctorat', 'Femme', 'Française', 'France', 'Français', 'Anglais', 'Mécanique quantique', 'Physique des particules', 'L3', 'M1', 'Professeur', 'À temps partiel', '15 ans', 'Recherche')
prof3 = Professeur("Garcia", "Pablo", "1978-08-25", "30 Rue du Commerce, Marseille", "+33 6 34 56 78 90", "pablo.garcia@example.com", 43, "Langues étrangères", 10, 'Doctorat', 'Homme', 'Espagnole', 'Espagne', 'Espagnol', 'Français', 'Linguistique', 'Traduction', 'L1', 'L2', 'Maître de conférences', 'À temps partiel', '20 ans', 'Informatique')
prof4 = Professeur("Nguyen", "Van", "1982-11-08", "40 Rue des Roses, Toulouse", "+33 6 45 67 89 01", "van.nguyen@example.com", 41, "Informatique", 8, 'Doctorat', 'Homme', 'Vietnamienne', 'Vietnam', 'Vietnamien', 'Français', 'Sécurité informatique', 'Intelligence artificielle', 'M1', 'M2', 'Maître de conférences', 'À temps plein', '15 ans','Programmation')
prof5 = Professeur("Wang", "Yan", "1995-03-23", "50 Rue des Champs, Lille", "+33 6 56 78 90 12", "yan.wang@example.com", 28, "Finance", 2, 'Master', 'Femme', 'Chinoise', 'Chine', 'Chinois', 'Anglais', 'Gestion de portefeuille', 'Analyse financière', 'L3', 'M1', 'Maître de conférences', 'À temps plein', '5 ans', 'Analyse financière')
prof6 = Professeur('Doe', 'John', '10/01/1970', '10 rue des Ecoles', '0102030405', 'john.doe@exemple.com', 51, 'Mathématiques', 5, 'PhD', 'M', 'Américain', 'USA', 'Anglais', 'Espagnol', 'Analyse', 'Algèbre', '1ère année', '', 'Professeur', 'Plein temps', '10 ans', 'Pédagogie')
prof7 = Professeur('Dupont', 'Sophie', '05/05/1980', '20 rue de la Liberté', '0607080910', 'sophie.dupont@exemple.com', 41, 'Physique', 3, 'Master', 'F', 'Française', 'France', 'Français', 'Anglais', 'Thermodynamique', '', '2ème année', '3ème année', 'Professeur', 'Plein temps', '5 ans', 'Recherche')
prof8 = Professeur('Garcia', 'Maria', '12/09/1975', '5 rue de la Paix', '0706050403', 'maria.garcia@exemple.com', 46, 'Espagnol', 7, 'Licence', 'F', 'Espagnole', 'Espagne', 'Espagnol', 'Français', 'Grammaire', 'Littérature', '3ème année', '', 'Professeur', 'Temps partiel', '8 ans', 'Multilingue')
prof9 = Professeur("Martin", "Sophie", "1985-05-18", "25 Rue de la Liberté, Lyon", "+33 6 98 76 54 32", "sophie.martin@example.com", 38, "Philosophie", 8, 'Doctorat','Femme','Belge', 'Belgique', 'Français', 'Anglais', 'Éthique', 'Métaphysique', 'L1', 'L2', 'Professeur', 'À temps partiel', '15 ans', 'Recherche')
prof10 = Professeur("Garcia", "Pablo", "1978-11-07", "5 Calle de la Plaza, Madrid", "+34 6 76 54 32 10", "pablo.garcia@example.com", 45, "Espagnol", 20, 'Doctorat','Homme','Espagnole', 'Espagne', 'Espagnol', 'Anglais', 'Langue et culture', 'Littérature', 'L1', 'L2', 'Professeur', 'À temps plein', '25 ans', 'Relations internationales')

 
