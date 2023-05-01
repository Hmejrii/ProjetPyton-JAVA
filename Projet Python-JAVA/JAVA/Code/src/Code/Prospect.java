package Code;

import java.util.Random;

public class Prospect{
	private String nom;
	private String prenom;
	private String adresse;
	private String telephone;
	private int age;
	

    private String dateDeContact;
    private String commentaire;
    private String poste;
    private double budget;
    
    
    
	public Prospect(String nom, String prenom, String adresse, String telephone, int age, String dateDeContact,String commentaire, String poste, double budget) {
		
		this.nom = nom;
		this.prenom = prenom;
		this.adresse = adresse;
		this.telephone = telephone;
		this.age = age;
		this.dateDeContact = dateDeContact;
		this.commentaire = commentaire;
		this.poste = poste;
		this.budget = budget;
	}
    
	public Prospect() {};
	
    
	public Prospect(String nom, String prenom, String adresse, String telephone, String dateDeContact,String commentaire, String poste, double budget) {
		
		this.nom = nom;
		this.prenom = prenom;
		this.adresse = adresse;
		this.telephone = telephone;
		this.age = new Random().nextInt(40) + 20;
		this.dateDeContact = dateDeContact;
		this.commentaire = commentaire;
		this.poste = poste;
		this.budget = budget;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getPrenom() {
		return prenom;
	}

	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}

	public String getAdresse() {
		return adresse;
	}

	public void setAdresse(String adresse) {
		this.adresse = adresse;
	}

	public String getTelephone() {
		return telephone;
	}

	public void setTelephone(String telephone) {
		this.telephone = telephone;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public String getDateDeContact() {
		return dateDeContact;
	}

	public void setDateDeContact(String dateDeContact) {
		this.dateDeContact = dateDeContact;
	}

	public String getCommentaire() {
		return commentaire;
	}

	public void setCommentaire(String commentaire) {
		this.commentaire = commentaire;
	}

	public String getPoste() {
		return poste;
	}

	public void setPoste(String poste) {
		this.poste = poste;
	}

	public double getBudget() {
		return budget;
	}

	public void setBudget(double budget) {
		this.budget = budget;
	}

	@Override
	public String toString() {
		return "Prospect [nom=" + nom + ", prenom=" + prenom + ", adresse=" + adresse + ", telephone=" + telephone
				+ ", age=" + age + ", dateDeContact=" + dateDeContact + ", commentaire=" + commentaire + ", poste="
				+ poste + ", budget=" + budget + "]";
	}
	
	
	
}
    
    
    
