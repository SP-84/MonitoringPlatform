# Sonde CPU
#!/bin/python

import psutil

print("Informations CPU :")
print(psutil.cpu_percent(0.1))
print("Fin affichage CPU")
