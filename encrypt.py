#!/usr/bin/env python
import pexpect
import os
import unittest
# pour chaque fichier doc faire

# le sous env est un fichier python
from path import path
# le répertoire d'essai sera gpg
d = path('/home/corentin/projets/gpg')
# les fichiers d'essai seront des fichiers texte
#for f in d.files('*.txt'):
	# syntaxe:
	# gpg --output essai.doc.pgp --symmetric essai.doc
#	commande = "gpg --output " + f + ".pgp --symetric " + f

class test_chiffrage_symetrique(unittest.TestCase):
	def test_construit_commande(self):
		objet_commande = creeobjet_commande("le_fichier.txt")
		commande = objet_commande.commande
		self.assertEqual('gpg --output le_fichier.txt.pgp --symmetric le_fichier.txt', commande)


