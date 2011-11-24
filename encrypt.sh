#!/bin/bash - 
#===============================================================================
#
#          FILE:  encrypt.sh
# 
#         USAGE:  ./encrypt.sh 
# 
#   DESCRIPTION:  encrypte les fichiers d'un répertoire de man symétrique
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR: Dr. Fritz Mehner {fgm}, mehner@fh-swf.de
#       COMPANY: FH Südwestfalen, Iserlohn
#       CREATED: 23/11/2011 14:19:10 CET
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
echo "chiffrage des fichiers doc"
for fichier in *.doc
do
gpg --output ${fichier}.gpg --symmetric <<FINDELINPUT
hellodolly
hellodolly
FINDELINPUT
done
: <<ZONECOMMENTEEPOURLINSTANT
echo "chiffrage fichiers pdf"
for fichier in *.pdf 
do 
gpg --output ${fichier}.gpg --symetric
done
gpg --output essai.doc.pgp --symmetric essai.doc
ZONECOMMENTEEPOURLINSTANT
