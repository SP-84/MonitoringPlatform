import mysql.connector
from mysql.connector import Error
from format import liste, disk, cpu, proc
from sonde4 import users2 as users, mem
import xml.etree.ElementTree as ET
import xml.dom.minidom
import time

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='sondes',
        user='uapv2103100',
        password='1234')

    if connection.is_connected():
        curseur = connection.cursor()
        bdd_info = connection.get_server_info()
        i = 0
        TEMPS = int(time.time())
        k = TEMPS
        while (i < len(users)):
            info ="""INSERT INTO sonde
                     (Temps, CPU, Processus, Disque, Memoire)
                     VALUES (%s,%s,%s,%s,%s)"""
            values = (TEMPS,cpu[i],proc[i],disk[i],mem[i])
            curseur.execute(info, values)
            connection.commit()
            print(curseur.rowcount, "Insertion de valeurs dans la table sonde")
            i = i + 1
            TEMPS = TEMPS + 1
        curseur.close()

        # Gestionnaire d'historique et backup en XML
        curseur = connection.cursor()
        j = 0
        root = ET.Element('root')
        doc = ET.SubElement(root, 'doc')
        while (j < len(users)):
            curseur.execute('SELECT * FROM sonde')
            for row in curseur:
                print(row)
            u = ET.SubElement(doc, 'user')
            ET.SubElement(u, "TIME", name="TIME").text = "%s" % row[0]
            ET.SubElement(u, "CPU", name="CPU").text = "%s" % row[1]
            ET.SubElement(u, "PROC", name="PROC").text = "%s" % row[2]
            ET.SubElement(u, "DISK", name="DISK").text = "%s" % row[3]
            ET.SubElement(u, "RAM", name="RAM").text = "%s" % row[4]
            j = j + 1
        tree = ET.ElementTree(root)
        tree.write("db.xml")
        dom = xml.dom.minidom.parse("db.xml")
        p = dom.toprettyxml(indent = '\t')
        f = open("db.xml", "r+")
        f.truncate(0)
        f.write(p)
        f.close()
        curseur.close()

        curseur = connection.cursor()
        cmd = "DELETE FROM sonde ORDER BY Temps LIMIT 10"
        curseur.execute(cmd)
        print("Base nettoyee")
        curseur.close()

except Error as e:
    print("Erreur", e)
finally:
    if connection.is_connected():
        curseur.close()
        connection.close()
        print("Fermeture de la connextion a MySQL")
