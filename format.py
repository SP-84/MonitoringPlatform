#!/bin/python
# Formatter l'affichage des sondes

liste=[]
disk=[]
cpu=[]
proc=[]
users=[]
mem=[]
mem2=[]

with open("donnees.txt", "r") as f:
	liste=[line.strip() for line in f]

for i in range(0, len(liste)):
        if (liste[i] == "Informations CPU :"):
                while (liste[i+1] != "Fin affichage CPU"):
                        head, sep, tail = liste[i+1].partition(':')
                        cpu.append(int(float(head)))
                        i = i + 1

for i in range(0, len(liste)):
	if (liste[i] == "Sonde disque"):
		while (liste[i+1] != "Fin affichage disque"):
			head, sep, tail = liste[i+1].partition('\t/home/')
			disk.append(head)
			i = i + 1

for i in range(0, len(liste)):
	if (liste[i] == "Sonde processus"):
		while (liste[i+1] != "Fin affichage processus"):
			head, sep, tail = liste[i+1].partition('\t/home/')
			proc.append(head)
			i = i + 1

for i in range(0, len(liste)):
	if (liste[i] == "Memoire par utilisateur"):
		while (liste[i+1] != 'Fin'):
			head, sep, tail = liste[i+1].partition(' utilise ')
			users.append(head)
			mem.append(tail)
			i = i + 1
