class Conteneur : # création de la classe Conteneur  
    def __init__ (self, nb_colis_max = 20, colis = []):
            self.nb_colis_max = nb_colis_max
            self.colis = colis
    
    def est_vide(self):
        if len(self.colis) == 0:
            print ("C'est vide")
            return True
        else:
            return False
    
    def est_plein(self):
        if len(self.colis) >= self.nb_colis_max:
            print ("C'est plein")
            return True
        else: 
            return False
            
"""     
    def empile(self, gobelin):
        if self.est_plein():
            return False
        else:
            self.colis.append(gobelin)
   
    def depile(self):
        if self.est vide():
"""    
    
    
        
a = Conteneur()
b = Conteneur(30)
print(a.est_vide())
"""
a.empile("gfd")
    """
print(a.est_vide())