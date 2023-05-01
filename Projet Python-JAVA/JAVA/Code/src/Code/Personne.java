package Code;


public class Personne implements PersonneInterface{
	    private String nom;
	    private String prenom;
	    private String adresse;
	    private String telephone;
	    private int age;
	    private String groupe;
	    
	    
	    
	  

		public Personne(String nom, String prenom, String adresse, String telephone, int age,String groupe) {
	        this.nom = nom;
	        this.prenom = prenom;
	        this.adresse = adresse;
	        this.telephone = telephone;
	        this.age=age;
	        this.groupe=groupe;
	    }
	    

	    

		// Constructeur avec nom et prenom
	    public Personne(String nom, String prenom) {
	        this.nom = nom;
	        this.prenom = prenom;
	        this.adresse = "";
	        this.telephone = "";
	    }

	    // Constructeur avec nom, prenom et adresse
	    public Personne(String nom, String prenom, String adresse) {
	        this.nom = nom;
	        this.prenom = prenom;
	        this.adresse = adresse;
	        this.telephone = "";
	    }

	    // Constructeur sans paramètres
	    public Personne() {
	        this.nom = "";
	        this.prenom = "";
	        this.adresse = "";
	        this.telephone = "";
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
	    public String getGroupe() {
			return groupe;
		}


		public void setGroupe(String groupe) {
			this.groupe = groupe;
		}


		@Override
		public String toString() {
			return "Personne [nom=" + nom + ", prenom=" + prenom + ", adresse=" + adresse + ", telephone=" + telephone
					+ ", age=" + age + "]";
		}




		@Override
		public String getDateNaissance() {
			// TODO Auto-generated method stub
			return null;
		}




		@Override
		public void setDateNaissance(String dateNaissance) {
			// TODO Auto-generated method stub
			
		}




		@Override
		public String getEmail() {
			// TODO Auto-generated method stub
			return null;
		}




		@Override
		public void setEmail(String email) {
			// TODO Auto-generated method stub
			
		}




		@Override
		public String getGenre() {
			// TODO Auto-generated method stub
			return null;
		}




		@Override
		public void setGenre(String genre) {
			// TODO Auto-generated method stub
			
		}




		@Override
		public String getNationalite() {
			// TODO Auto-generated method stub
			return null;
		}




		@Override
		public void setNationalite(String nationalite) {
			// TODO Auto-generated method stub
			
		}




		@Override
		public String getPaysOrigine() {
			// TODO Auto-generated method stub
			return null;
		}




		@Override
		public void setPaysOrigine(String paysOrigine) {
			// TODO Auto-generated method stub
			
		}
	    
	    
	   
	    
	}


