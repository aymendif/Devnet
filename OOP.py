class ingenieur :
  def __init__(self,firstname,lastname,birthday,home,mailaddress,telephone):
   self.nom=firstname
   self.prenom=lastname
   self.naissance=birthday
   self.address=home
   self.email=mailaddress
   self.phone=telephone
  def affichercontent(self) :
    print (self.nom,self.prenom,self.naissance,self.address,self.email,self.phone)
ingenieur1=ingenieur("zaki","difaoui","08/05/1990","alger","zaki@gmail.com","06779889")
ingenieur2=ingenieur("iyad","difaoui","08/05/2000","medea","iyad@gmail.com","05666569")

class developpeur (ingenieur):
  def __init__(self, firstname, lastname, birthday, home, mailaddress,telephone,degree, specialite, position, experience,project):
   super().__init__(firstname, lastname, birthday, home, mailaddress,telephone)
   self.etude=degree
   self.spec=specialite
   self.position=position
   self.exp=experience
   self.projet=project
  def __str__(self) :
    return f"{self.nom} {self.prenom} {self.naissance} {self.address} {self.email} {self.phone} {self.etude} {self.spec} {self.position} {self.exp} {self.projet} "
 
developpeur1=developpeur("aimane","difaoui","05/05/1999","paris","aimane@gmail.com","0780861769","master","java","ingenieur","5ans","SFR")
print (developpeur1)
ingenieur1.affichercontent()
ingenieur2.affichercontent()
