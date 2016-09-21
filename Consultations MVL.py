"""Programme pour consultations en étude de pharmacie"""

import random

class Main:

	def __init__(self):

		patient = Patient()
		if patient.get_child() == True:
			intro = random.randint(1, 10)
		else:
			intro = random.randint(1, 12)
		variante = random.randint(1, 4)

		if intro == 1:  #### Douleur

			input("Bonjour, je ne sais pas quoi choisir : Tylenol ou Advil")

			if variante == 1:
				input("Mal de dos")
			elif variante == 2:
				input("Mal de tête")
			elif variante == 3:
				input("Mal au bras")
			elif variante == 4:
				input("38,5 de fièvre")

		elif intro == 2: #### Constipation

			input("Bonjour, je constipe, qu'est-ce que je fais?")

			if variante == 1:
				input("j'ai vraiment vraiment mal au ventre")
			elif variante == 2:
				input("j'ai déjà essayé le Lax-A-Day, sans succès")
			elif variante == 3:
				input("Ca fait 4 jours environ que j'ai pas été à la selle")
			elif variante == 4:
				input("c'est juste plus dur en fait")

		elif intro == 3: #### Problème aux yeux
			
			input("Bonjour, j'ai l'oeil rouge et des croutes sur les cils")

			if variante == 1:
				input("j'ai comme mal à l'oeil")
			elif variante == 2:
				input("j'ai mis un vieux tube de polysporin de chez nous pi ca a pas aidé")
			elif variante == 3:
				input("Est-ce que c'est contagieux?")
			elif variante == 4:
				input("Donne moi du polysporin, j'ai eu la même affaire l'été passé")

		elif intro == 4: #### Toux
			
			input("Bonjour, est-ce que du Buckley, c'est pas pire?")

			if variante == 1:
				input("J'ai une toux full de liquide")
			elif variante == 2:
				input("Je tousse sec depuis 2 semaines")
			elif variante == 3:
				input("Des fois, je suis pu capable de m'arrêter de tousser")
			elif variante == 4:
				input("J'ai vraiment mal à gorge")

		elif intro == 5: #### Rhume
			input("Bonjour, j'ai une grippe")

			if variante == 1:
				input("J'ai mal à la tête et au dos")
			elif variante == 2:
				input("J'ai le nez bouché")
			elif variante == 3:
				input("Je fais de la grosse fièvre")
			elif variante == 4:
				input("J'ai le nez qui coule")

		elif intro == 6: #### Allergies
			input("Bonjour, j'ai des grosses allergies")

			if variante == 1:
				input("J'atchoum tout le temps")
			elif variante == 2:
				input("Je pleure full de mon oeil droit")
			elif variante == 3:
				input("J'ai essayé le Reactine mais ca me fait dormir")
			elif variante == 4:
				input("Aucun effet avec du claritin")

		elif intro == 7: #### Verrue
			input("J'ai de quoi sur la peau, une verrue peut-être?")

			if variante == 1:
				input("Des affaires qui gèlent, c'est tu bon?")
			elif variante == 2:
				input("C'est comme une petite boule qui est apparu hier")
			elif variante == 3:
				input("Je suis sûr c'est une verrue mais je l'ai accroché pi ca saigne")
			elif variante == 4:
				input("Pourtant, je me lave tous les jours")

		elif intro == 8: #### Dermatite / plaie infectée
			input("Bonjour, qu'est-ce que je peux faire pour une plaque qui pique?")

			if variante == 1:
				input("j'ai pogné ca quand je suis allé dans le bois")
			elif variante == 2:
				input("C'est arrivé tout d'un coup sans explication")
			elif variante == 3:
				input("J'ai pris du Tylenol hier, ca a tu rapport?")
			elif variante == 4:
				input("Il y a du pus")

		elif intro == 9: #### RGO
			input("Bonjour, j'ai comme une sensation de brulure dans la gorge")

			if variante == 1:
				input("J'ai pris des Tums, mais ca a rien fait")
			elif variante == 2:
				input("On m'a parlé du Olex, c'est bon?")
			elif variante == 3:
				input("Ca fait environ 2 semaines et demi")
			elif variante == 4:
				input("J'ai l'impression que ca engourdi toute ma machoire")
		elif intro == 10: #### Gastro
			input("Bonjour, je veux quelque chose pour une gastro")

			if variante == 1:
				input("J'ai vomi une fois hier")
			elif variante == 2:
				input("Je fais de la fièvre, j'ai l'impression")
			elif variante == 3:
				input("Je vomi non-stop depuis 2 jours")
			elif variante == 4:
				input("J'ai pris 1 imodium, mais ca a pas tant aidé")

		elif intro == 11: #### Tabac

			input("J'aimerais arrêter de fumer")
			if variante == 1:
				input("J'ai pris une cigarette rendu à l'étape 2 de mes patchs")
			elif variante == 2:
				input("J'ai recommencé à fumer 1 paquet par jour")
			elif variante == 3:
				input("La gomme, ca marche pas")
			elif variante == 4:
				input("Je veux l'inhalateur hi-tech! Ca a l'air de bien aller.")

		elif intro == 12: #### Vaginite
			input("J'ai des rougeurs ici-bas")

			if variante == 1:
				input("Ca sent un peu bizarre")
			elif variante == 2:
				
				input("Je suis pu capable, ca fait vraiment mal")
			elif variante == 3:
				input("J'ai entendu dire que mettre du yogourt, ca aide. C'est vrai?")
			elif variante == 4:
				input("C'est la 2e fois depuis 3 mois, memes symptomes")

		input("Je peux répondre à vos questions")
		print(patient.get_info()[0])
		print(patient.get_info()[1])
		print("Allergie {}".format(patient.get_info()[2]))
		print("Co-morbidité : {}".format(patient.get_info()[3]))
		print("Autres médicaments : {}".format(patient.get_info()[4]))
		input("Qu'est-ce que je dois faire?")
		input("C'est une bonne option... : {}".format(patient.get_info()[5]))
		input("Parfait, je vais prendre ce que vous me proposez")
		input("Merci, au revoir")





class Patient:

	def __init__(self):

		possible_allergies = ["À l'iode",
							"À l'aspirine",
							"Au Motrin",
							"Au Advil",
							"Au Voltaren",
							"Aux adhésifs de patch",
							"Au miel",
							"À la codéine",
							"J'ai eu une mauvaise expérience avec un vaporisateur nasal",
							"Aucune allergie"]

		possible_diseases = ["Aucune",
							"Diabète",
							"Hypertension",
							"Insuffisance hépatique",
							"Insuffisance cardiaque",
							"Insuffisance rénale",
							"Arthrite",
							"Tabagisme",
							"Asthme",
							"Myopie"]

		possibles_preference = ["Je vais prendre le meilleur produit",
								"Il faut que ca soit pas cher",
								"Je suis souvent pressé",
								"Je préfère pas prendre d'affaire chimique",
								"Je veux que ca se règle vite"]

		possible_other_rx = ["Aucun médicament",
							"Acétaminophène",
							"Advil",
							"AAS"]

		self.child = False
		self.allergies = random.choice(possible_allergies)
		self.diseases = random.choice(possible_diseases)
		self.age = random.randint(18, 95)
		self.weight = random.randint(100, 300)
		probability = random.randint(0,100)
		if probability >= 80:
			self.preference = random.choice(possibles_preference)
		else:
			self.preference = possibles_preference[0]
		probability = random.randint(0, 100)
		if probability >= 80:
			self.other_rx = random.choice(possible_other_rx)
		else:
			self.other_rx = possible_other_rx[0]
		probability = random.randint(0, 100)
		if probability >= 80:
			self.child = True
		if self.child == True:
			self.age = random.randint(0,4)
			self.weight = random.randint(2, 10)*self.age
			self.diseases = possible_diseases[0]
			self.other_rx = possible_other_rx[0]

	def get_info(self):

		self.printable_age = "{} ans".format(self.age)
		self.printable_weight = "{} lbs".format(self.weight)

		return [self.printable_age, self.printable_weight, self.allergies, self.diseases, self.other_rx, self.preference] 

	def get_child(self):

		return self.child

if __name__ == "__main__":

	Main()