class Studente():
  def __init__(self, nome, cognome, eta, matricola):
    self.nome = nome
    self.cognome = cognome
    self.eta = eta
    self.matricola = matricola
    self.voti = []

  def presentati(self):
    print(f"Salve sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}")

  def aggiungi_voto(self, voto):
    if 18 <= voto <= 30:
        self.voti.append(voto)
        print(f"Voto {voto} registrato correttamente per {self.nome}.")
    elif voto < 18:
        print(f"Esame non superato: il voto {voto} è insufficiente.")
    else:
        print("Errore: un voto non può essere superiore a 30.")

  def calcola_media(self):
    if not self.voti:
      return 0
    media=sum(self.voti) / len(self.voti)
    print(f"{self.nome} {self.cognome} ha una media pari a {media}")

  def studia(self, ore):
    print(f"{self.nome} {self.cognome} ha studiato {ore} ore")

studente1 = Studente("Angelica", "Carrieri", 23, "20232934")
studente2 = Studente("Erika", "De Giorgi", 25, "39402019")

print(studente1.nome)
studente1.presentati()
studente1.aggiungi_voto(25)
studente1.aggiungi_voto(30)
studente1.calcola_media()
studente1.studia(5)