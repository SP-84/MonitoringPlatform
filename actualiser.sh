#!/bin/bash

i=1;
#rm donnees.txt
while true
do
	echo "Affichage des sondes";
	(python3 sonde1.py && ./sonde2.sh && ./sonde3.sh && python3 sonde4.py) | tee -a ./donnees.txt;
	((i++));
	python3 format.py
	python3 db.py
	python3 alerte.py
	sudo cp SondeCPU.svg ./Sonde1.svg
	sudo cp SondeDISK.svg ./Sonde2.svg
        sudo cp SondeRAM.svg ./Sonde3.svg
	sleep 10;
done
