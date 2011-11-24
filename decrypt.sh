#!/bin/bash - 
#===============================================================================
#
#          FILE:  decrypt.sh
# 
#         USAGE:  ./decrypt.sh 
 
#   DESCRIPTION:  décrypte les fichiers d'un répertoire de man symétrique
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR: Dr. Fritz Mehner (fgm), mehner@fh-swf.de
#       COMPANY: FH Südwestfalen, Iserlohn
#       CREATED: 23/11/2011 14:19:10 CET
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
echo "déchiffrage des fichiers doc"
for fichier in *.doc do
	RESULTAT="$(basename ${fichier} .gpg)"
gpg --output $(basename ${fichier} .gpg) --symmetric --decrypt
gpg --output essai.doc2 --decrypt essai.doc.pgp
done
echo "déchiffrage fichiers pdf"
for fichier in *.pdf do 
	RESULTAT="$(basename ${fichier} .gpg)"
	echo "hellodolly" | gpg --output $(basename ${fichier}.gpg) --symetric --decrypt
done
gpg --output essai.doc2 --decrypt essai.doc.pgp

#!/usr/bin/env python
import pexpect
import os
# pour chaque fichier doc faire

# le sous env est un fichier python
from path import path
d = path('/home/corentin/projets/cv')
for f in d.files('*.pgp'):
	
#rep="/home/corentin/projets/cv"
#dirList=os.listdir(rep)
#for fname in dirList:
	# construie la chaine et appeler pexpect.spawn
	chaine = "gpg --output " + fname
child = pexpect.spawn('gpg --output $(
