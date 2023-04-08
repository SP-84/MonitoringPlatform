#!/bin/bash

# Stockage
i=1

# Effacer les donnees precedentes pour actualiser les donnees
# rm ./donnees.txt

while true
do
	echo "Affichage des sondes";
	(python3 sonde1.py && ./sonde2.sh && ./sonde3.sh && python3 sonde4.py) | tee -a ./donnees.txt;
	((i++));
	sleep 5;
done
