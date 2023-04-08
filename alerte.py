from db import users, disk, mem, cpu
import pygal
from pygal.style import DarkStyle
from pygal.style import NeonStyle
import smtplib
import getpass
import time
 
f = open("donnees.txt", "r")
data = f.read()
print(data)

# Condition alerte
utilisation_ram = sum(mem)
alerte = 0
if (utilisation_ram > 25):
    print ("RAM : ", utilisation_ram, "%")
    print("Alerte RAM")
    alerte = 1

# Envoyer un mail
if (alerte == 1):
    password = getpass.getpass(prompt = 'Mot de passe : ')
    smtp = smtplib.SMTP_SSL('smtpz.univ-avignon.fr:465')
    smtp.login("guillaume.salloum@alumni.univ-avignon.fr", password)
    msg = """Subject: Alerte RAM 
L utilisation de la RAM sur la VM est superieure a 25% ! """
    smtp.sendmail("guillaume.salloum@alumni.univ-avignon.fr", "guillaume.salloum@alumni.univ-avignon.fr", msg)

# Graphiques
chart = pygal.Bar(title = "Evolution du %CPU")
chart.x_labels = users
chart.add('CPU', int(cpu[0]))
chart.render_to_file('SondeCPU.svg')

chart2 = pygal.StackedLine(title = "Evolution de la place libre du disque", style=DarkStyle)
chart2.x_labels = users
chart2.add('Disque', int(disk[1]))
chart2.render_to_file('SondeDISK.svg')

chart3 = pygal.Bar(title = 'Evolution de la RAM/Utilisateur', style=NeonStyle)
chart3.x_labels = users
chart3.add('RAM', mem)
chart3.render_to_file('SondeRAM.svg')
