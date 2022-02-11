import csv
import collections

with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003.csv", encoding='utf-8') as prenoms2003:
    reader = csv.DictReader(prenoms2003, delimiter=',')
    table1 = dict()
    for line in prenoms2003:
        line = line.strip('\n')
        (key,val) = line.split(',')
        table1[key] = val

'''with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2004.csv", encoding='utf-8') as prenoms2004:
    reader = csv.DictReader(prenoms2004, delimiter=',')
    table2 = [dict(ligne) for ligne in reader]

table3 = table1 + table2

field_names = ['sexe', 'prenom', 'annee', 'nombre']
with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003-2004.csv", 'w', newline='' ) as listPrenom:
    objet = csv.DictWriter(listPrenom, fieldnames=field_names, delimiter=',')
    objet.writeheader()
    objet.writerows(table3)'''

for line in prenoms2003.values:
    counter = []
    conter = 0 
    if table1 not in counter:
        counter.append(line)
        conter = conter+1
    elif line in counter:
        conter = conter+1
    
print(conter)