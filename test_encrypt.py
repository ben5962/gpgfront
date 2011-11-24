#!/usr/bin/env python
# -*- coding: utf8 -*- 
import pexpect
import os
import unittest
import traceback
import sys
# pour chaque fichier doc faire
def creeobjet_commande(fichier):
	class CObjetCommande():
		def __init__(self):
			self.commande_chiffrage = "gpg --output " + fichier + ".pgp --symmetric " + fichier
			self.commande_dechiffrage = 'gpg --output encoreun.txt --decrypt encoreun.txt.gpg'
	return CObjetCommande()

# le sous env est un fichier python
from path import path
# le répertoire d'essai sera gpg
d = path('/home/corentin/projets/gpg')
# les fichiers d'essai seront des fichiers texte
#for f in d.files('*.txt'):
	# syntaxe:
	# gpg --output essai.doc.pgp --symmetric essai.doc
#	commande = "gpg --output " + f + ".pgp --symetric " + f
def makefile(fichier):
	try:
		path = './' + fichier
		open(path, 'w').close()
	except Exception, e:
		print str(e)
		traceback.print_exc()
		os.exit(1)
	
def rmfile(fichier):
	try:
		path = './' + fichier
		os.remove(path)
	except Exception, e:
		print str(e)
		traceback.print_exc()
		os.exit(1)

def remplis(fichier):
	try:
		f = open(fichier, 'w')
		f.write("qmslfjdmqfjd\n")
		f.close()
	except Exception, e:
		print str(e)
		traceback.print_exc()
		#os.exit(1)


class test_chiffrage_symetrique(unittest.TestCase):


	def test_construit_commande_chiffrage(self):
		objet_commande = creeobjet_commande("le_fichier.txt")
		commande = objet_commande.commande_chiffrage
		self.assertEqual('gpg --output le_fichier.txt.pgp --symmetric le_fichier.txt', commande)

	def test_construit_autre_commande_chiffrage(self):
		objet_commande = creeobjet_commande("lautre.txt")
		commande = objet_commande.commande_chiffrage
		self.assertEqual('gpg --output lautre.txt.pgp --symmetric lautre.txt', commande)
	def test_construit_commande_dechiffrage(self):
		objet_commande = creeobjet_commande("encoreun.txt.gpg")
		commande = objet_commande.commande_dechiffrage
		self.assertEqual('gpg --output encoreun.txt --decrypt encoreun.txt.gpg', commande)
	
	def test_pexpect(self):
		entree = "essai entree"
		a_tester = pexpect.run("""sh -c 'echo "valeur entree?"; read ENTREE; echo "$ENTREE"'""", events = { "valeur entree?" : entree  }, timeout=1)
		valeur_attendue = "valeur entree?\r\n" + entree
		self.assertEqual(a_tester, valeur_attendue)

	def test_encrypt_first_pass(self):
		fichier = "essai.txt"
		makefile(fichier)
		remplis(fichier)
		self.assertTrue(os.path.isfile(fichier))
		objet_commande = creeobjet_commande(fichier)
		#child = pexpect.spawn(objet_commande.commande_chiffrage, timeout=2)
		child = pexpect.spawn("gpg --output essai.txt.pgp --symmetric essai.txt", timeout=6 )
		# putain! ca marche en raw mais pas avec objet commande! wtf? 
		#st='gpg --output essai.txt.pgp --symmetric essai.txt'
		#child = pexpect.spawn(st, timeout=2)
		# putain! ca marche aussi comme ca. wtf?
		#st = objet_commande.commande_chiffrage
		#child = pexpect.spawn(st, timeout=4)
		# putain ! ca marche aussi. pourquoi???
		# soit. il faut que la chaine soit completement formee avant
		# d' etre utilisee dans spawn. ok.
		# d'ailleurs ca marche pas tant que cela puisque le fichier n'est pas écrit
		fout = file("mylog.txt", 'w')
		child.logfile = fout
		child.expect('passe')
		#child.waitnoecho(timeout=1)
		child.sendline('hellodolly')
		#child.waitnoecho(timeout=1)
		child.expect('passe')
		child.sendline('hellodolly')
		#child.waitnoecho()
		child.close()
	#	fout.close()
		#self.assertEqual(child.status, 0)
		#a_tester = pexpect.run(objet_commande.commande_chiffrage, events = { 'Entrez la phrase de passe : ' : 'hellodolly\n', 'Répétez la phrase de passe: ' : 'hellodolly\n' }, timeout = 2)
		#(command_output, exit_status) = pexpect.run(st, events = { 'Entrez la phrase de passe: ' : 'hellodolly\n', '.*passe.*' : 'hellodolly\n' }, withexitstatus=1, timeout = 2)
		#self.assertEqual(command_output, "Entrez la phrase de passe: ")
		self.assertEqual(exit_status, 0)
		#print a_tester
		nomfich='./' + fichier + '.pgp'
		#self.assertEqual(nomfich, './essai.txt.pgp')
		self.assertTrue(os.path.isfile(nomfich))
	#	rmfile(fichier)
	#	except Exception, e:
	#		print str(e)
	#		traceback.print_exc()
	#		os.exit(1)



