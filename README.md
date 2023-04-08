#Projet UE Administration des systèmes d'exploitation 2022-2023
***
L’objectif de ce mini-projet et de réaliser une plate-forme logiciel de monitoring d’un parc
informatique. Cette plate-forme, une fois installée, permettra à l’administrateur système que
vous êtes de connaître rapidement à chaque fois que vous le demandez l’état détaillé de
l’ensemble des serveurs faisant partis du parc et les dernières alertes du C.E.R.T.
(http://www.cert.ssi.gouv.fr/). Le logiciel permettra aussi d’être prévenu par e-mail en cas de
situation de crise. Une situation de crise étant par exemple : quand un serveur n’a pas donné
signe de vie depuis plus de 30 minutes, quand un disque dur atteint 100% d’occupation ou
lorsque la RAM est utilisée à 100% , etc ..

## Table of Contents
1. [General Info](#general-info)
2. [Usage](#usage)
3. [Technologies](#technologies)

## General Info
***
Tout d'abord, il existe quatres sondes, deux en Python et deux en Bash, permettant de récupérer des données respectivement sur l'utilisation du CPU, les processus de l'utilisateur de la VM, l'espace disque occupé ainsi que l'utilisation de la RAM.

Ensuite à l'aide d'un gestionnaire de stockage on peut un archiver historique de sorties des sondes et nettoyer la base de donée. De plus on peut aisement accéder aux informations de la base de données avec l'interface phpMyAdmin

D'autre part on a une interface graphique de l'évolution des données des sondes. Ce
module permet de gérer les alertes et d'envoyer aussi des e-mails en cas de situation de crise.

Enfin le dernier élément est page web qui permet de visualiser directement les graphiques générés avec Pygal sur les sorties des sondes.

Les fichiers "sonde1.py", "sonde2.sh" et "sonde3.sh"et "sonde4.py" permettent de récupérer 
des données sur les utilisateurs (%CPU, processus, espace disque et RAM respectivement). 
Ces données sont ensuite envoyées dans un fichier "donnees.txt" et formattées par le fichier "format.py" 
pour être utilisées par "db.py", qui génère une base de données, une archive XML "db.xml" et supprime les 10 premières données les plus anciennes à chaque itération.

Si une crise est détectée (RAM totale > 20%), "alerte.py" prévient l'utilisateur 
en lui envoyant un mail à l'utilisateur pour le prévenir.

## Usage
***
./actualiser.sh permet d'afficher les données des sondes, 
d'insérer leur sortie dans la base de données MySQL "sonde.sql", et de générer les graphiques avec Pygal.
Pour consulter l'affichage des sondes, aller sur la page web en ouvrant la page "affichage.html", disponible dans Shared partagé entre la VM et le client. 

## Technologies
***
Liste des logiciels utilisés :
* [Python3]
* [Bash]
* [Psutil] 
* [Pygal] 
* [MySQL] 
* [phpMyAdmin] 
* [getpass] 
* [time] 
* [html] 
* [CSS] 
* [javascript] 
