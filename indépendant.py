#!/usr/bin/env python
# -*- coding: utf8 -*- 

import pexpect
def withregex():
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
	#ne fonctionne que si on vire child.close()
	#child.close()
# marche pas.
withregex()

# par contre le meme passé en commandes simples hors fonction ... ok!
child = pexpect.spawn("gpg --output essai.txt.pgp.2 --symmetric essai.txt", timeout=6 )
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
#ne fonctionne que si on vire child.close()
#child.close()

