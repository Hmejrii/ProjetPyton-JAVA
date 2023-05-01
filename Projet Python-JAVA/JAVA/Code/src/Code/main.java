package Code;
import java.io.*;
import java.util.*;


public class main {

	public static void main(String[] args) {
		
		
		// Instanciation de 10 objets de la classe Personne
		Personne p1 = new Personne("Durand", "Jean", "10 rue du Paradis", "0102030405", 30,"A");
        Personne p2 = new Personne("Dupont", "Marie", "5 rue des Lilas", "0607080910", 25,"B");
        Personne p3 = new Personne("Martin", "Pierre", "18 avenue des Champs-Elysées", "0203040506", 40,"B");
        Personne p4 = new Personne("Leclerc", "Sophie", "12 rue de la Paix", "0708091011", 22,"C");
        Personne p5 = new Personne("Dubois", "Luc", "7 rue de la Liberté", "0506070809", 5,"C");
        Personne p6 = new Personne("Durand", "Jean", "12 avenue de la Paix", "0102030405", 1, "A");
        Personne p7 = new Personne("Martin", "Julie", "6 rue du Commerce", "0607080910", 3, "B");
        Personne p8 = new Personne("Lefevre", "Pierre", "20 avenue des Champs-Elysées", "0102030405", 2, "A");
        Personne p9= new Personne("Moreau", "Sophie", "15 boulevard Haussmann", "0607080910", 4, "C");
        Personne p10 = new Personne("Dupont", "Luc", "7 rue de la Liberté", "0506070809", 5,"C");
        

		// Instanciation de 10 objets de la classe Etudiant
        etudiant e1 = new etudiant("Dupont", "Marie", "5 rue des Lilas", "0607080910", 25,"c","123456", true, 14.5, "Licence");
        etudiant e2 = new etudiant("Martin", "Pierre", "18 avenue des Champs-Elysées", "0203040506", 40,"c", "789101", false, 10.0, "Master");
        etudiant e3 = new etudiant("Leclerc", "Sophie", "12 rue de la Paix", "0708091011", 22,"c", "234567", true, 13.0, "Licence");
        etudiant e4 = new etudiant("Dubois", "Luc", "7 rue de la Liberté", "0506070809", 50,"c", "891011", false, 11.5, "Master");
        etudiant e5 = new etudiant("Durand", "Jean", "10 rue du Paradis", "0102030405", 30,"b", "345678", true, 12.0, "Licence");
        etudiant e6 = new etudiant("Durand", "Jean", "10 rue du Paradis", "0102030405", 30, "b", "345678", true, 12.0, "Licence");

        etudiant e7 = new etudiant("Dupont", "Marie", "15 avenue des Champs-Elysées", "0607080910", 25, "a", "123456", false, 14.5, "Master");
        etudiant e8 = new etudiant("Martin", "Pierre", "20 rue de la Paix", "0203040506", 27, "c", "567890", true, 10.0, "Licence");

        etudiant e9 = new etudiant("Garcia", "Sophie", "5 place de la République", "0304050607", 23, "a", "234567", false, 16.0, "Master");

        etudiant e10 = new etudiant("Lefebvre", "Lucie", "12 boulevard Haussmann", "0809101112", 29, "b", "789012", true, 13.5, "Licence");

		// Instanciation de 10 objets de la classe Professeur
       Professeur pr1 = new Professeur("Smith", "John", "12 Rue de la Paix", "0612345678", 35,"c", "Mathématiques", 3500.0, 5, new String[]{"Doctorat en Mathématiques", "CAPES"});
       Professeur pr2 = new Professeur("Dupont", "Marie", "6 Rue des Lilas", "0678901234", 45,"b", "Physique-Chimie", 4500.0, 15, new String[]{"Doctorat en Physique", "Agrégation de Physique"});
        Professeur pr3 = new Professeur("Martin", "Julie", "8 Rue de la Liberté", "0645678901", 40,"a", "Histoire-Géographie", 4200.0, 8, new String[]{"Doctorat en Histoire", "CAPES"});
        Professeur pr4 = new Professeur("Dubois", "Lucas", "3 Rue de la République", "0698765432", 30,"c", "Informatique", 3000.0, 2, new String[]{"Master en Informatique"});
        Professeur pr5 = new Professeur("Leclerc", "Camille", "16 Avenue des Champs-Élysées", "0634567890", 50,"c","Langues Étrangères", 5000.0, 20, new String[]{"Doctorat en Langues Étrangères", "Agrégation de Langues"});
        Professeur pr6 = new Professeur("Dupont", "Sophie", "5 Rue de la Paix", "0102030405", 40, "A", "Informatique", 7000.0, 10, new String[]{"Doctorat en Informatique", "Habilitation à diriger des recherches en Informatique"});
        Professeur pr7 = new Professeur("Martin", "Paul", "12 Rue du Faubourg Saint-Honoré", "0654321098", 45, "B", "Mathématiques", 8000.0, 15, new String[]{"Doctorat en Mathématiques Appliquées", "Agrégation de Mathématiques"});
        Professeur pr8 = new Professeur("Lefebvre", "Julie", "3 Rue de la République", "0678901234", 35, "C", "Philosophie", 6000.0, 5, new String[]{"Doctorat en Philosophie", "Habilitation à diriger des recherches en Philosophie"});
        Professeur pr9 = new Professeur("Garcia", "Pierre", "8 Avenue des Gobelins", "0645678901", 50, "D", "Sciences Politiques", 9000.0, 20, new String[]{"Doctorat en Sciences Politiques", "Agrégation de Sciences Sociales"});
        Professeur pr10 = new Professeur("Moreau", "Marie", "15 Rue de la Pompe", "0612345678", 42, "E", "Histoire", 6500.0, 7, new String[]{"Doctorat en Histoire", "Habilitation à diriger des recherches en Histoire"});
        
        // Instanciation de 5 objets de la classe Prospect 
        
      Prospect prosp1 = new Prospect("Dupont", "Marie", "123 rue de la Victoire", "01 23 45 67 89", 30, "12/04/2023", "Intéressé", "Chef de projet", 50000.0);
        Prospect prosp2 = new Prospect("Durand", "Pierre", "456 avenue des Lilas", "02 34 56 78 90", 40, "15/04/2023", "A relancer", "Développeur", 40000.0);
       Prospect prosp3 = new Prospect("Martin", "Lucie", "789 boulevard des Roses", "03 45 67 89 01", 25, "20/04/2023", "Pas intéressé", "Commercial", 45000.0);
        Prospect prosp4 = new Prospect("Garcia", "Antoine", "147 rue des Champs", "04 56 78 90 12", 35, "25/04/2023", "En attente de réponse", "Ingénieur R&D", 55000.0);
        Prospect prosp5 = new Prospect("Lefebvre", "Sophie", "258 avenue du Parc", "05 67 89 01 23", 28, "30/04/2023", "Non disponible pour l'instant", "Designer", 35000.0);
        Prospect prosp6 = new Prospect("Dupont", "Luc", "12 rue des Roses", "0612345678", 25, "01/06/2023", "Disponible à partir de septembre", "Développeur web", 40000.0);
        Prospect prosp7 = new Prospect("Martin", "Laura", "7 rue des Lilas", "0645678901", 30, "15/05/2023", "Disponible immédiatement", "Chef de projet", 50000.0);
        Prospect prosp8 = new Prospect("Garcia", "Carlos", "3 avenue des Orangers", "0656789012", 27, "30/06/2023", "Disponible à partir de juillet", "Designer graphique", 35000.0);
        Prospect prosp9 = new Prospect("Dubois", "Jeanne", "18 rue des Chênes", "0678901234", 23, "10/07/2023", "Disponible à partir d'octobre", "Développeur mobile", 45000.0);
        Prospect prosp10 = new Prospect("Lefevre", "Pierre", "5 avenue de la Gare", "0690123456", 29, "20/05/2023", "Non disponible pour l'instant", "Analyste financier", 60000.0);
     // Instanciation de 5 objets de la classe directeur 
        Directeur d1 = new Directeur("Dupont", "Pierre", "12 Rue de la Paix", "0123456789", 45, "A", "01/01/2022", "Finance", 100000.0, "Bureau 1");

        Directeur d2 = new Directeur("Martin", "Sophie", "7 Rue des Fleurs", "0654321098", 50, "B", "01/02/2022", "Marketing", 95000.0, "Bureau 2");

        Directeur d3 = new Directeur("Girard", "Jacques", "25 Avenue de la République", "0789456123", 55, "A", "01/03/2022", "Ressources humaines", 110000.0, "Bureau 3");

        Directeur d4 = new Directeur("Dubois", "Marie", "9 Rue des Lilas", "0321654987", 40, "C", "01/04/2022", "Informatique", 120000.0, "Bureau 4");

        Directeur d5 = new Directeur("Moreau", "François", "14 Rue de la Liberté", "0956784321", 48, "B", "01/05/2022", "Communication", 90000.0, "Bureau 5");
        Directeur d6 = new Directeur("Dupont", "Pierre", "12 rue de la Paix", "06 12 34 56 78", 45, "A", "01/01/2022", "Finance", 120000.0, "Bureau 1");
        Directeur d7 = new Directeur("Martin", "Sophie", "8 avenue des Champs-Élysées", "06 98 76 54 32", 50, "B", "01/02/2022", "Marketing", 130000.0, "Bureau 2");
        Directeur d8 = new Directeur("Leroy", "Thomas", "22 rue de la République", "06 23 45 67 89", 55, "C", "01/03/2022", "Ressources humaines", 140000.0, "Bureau 3");
        Directeur d9 = new Directeur("Girard", "Marie", "5 boulevard Voltaire", "06 34 56 78 90", 60, "A", "01/04/2022", "Informatique", 150000.0, "Bureau 4");
        Directeur d10 = new Directeur("Moreau", "Lucie", "18 avenue de la Liberté", "06 87 65 43 21", 40, "B", "01/05/2022", "Communication", 160000.0, "Bureau 5");

	}}
		

