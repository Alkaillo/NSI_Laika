import csv
import pandas as pd
from collections import Counter

with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003.csv", encoding='utf-8') as prenoms2003:
    reader = csv.DictReader(prenoms2003, delimiter=',')
    table1 = [dict(ligne) for ligne in reader]

with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2004.csv", encoding='utf-8') as prenoms2004:
    reader = csv.DictReader(prenoms2004, delimiter=',')
    table2 = [dict(ligne) for ligne in reader]

table3 = table1 + table2
def writer():
    field_names = ['sexe', 'prenom', 'annee', 'nombre']
    with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003-2004.csv", 'w', newline='' ) as listPrenom:
        objet = csv.DictWriter(listPrenom, fieldnames=field_names, delimiter=',')
        objet.writeheader()
        objet.writerows(table3)


def MostPopular2003():
    df = pd.read_csv('/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003.csv')
    dictio = dict(zip(df["nombre"], df["prenom"]))
    dictionary_items = dictio.items()
    sorted_items = sorted(dictionary_items)
    print(sorted_items)


def MostPopular2004():
    df = pd.read_csv('/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2004.csv')
    dictio2 = dict(zip(df["nombre"], df["prenom"]))
    dictionary_items2 = dictio2.items()
    sorted_items2 = sorted(dictionary_items2)
    print(sorted_items2)

    '''df = pd.read_csv('/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003.csv')
    dictio = dict(zip(df["prenom"], df["nombre"]))
    df2 = pd.read_csv('/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2004.csv')
    dictio2 = dict(zip(df2["prenom"], df2["nombre"]))
    print(dictio2, dictio)'''


def writerJoin():
    di = pd.read_csv("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/Prenoms2003-2004.csv")
    dictTotal = dict(zip(di["prenom"], di["nombre"]))
    field_names = ['sexe', 'prenom', 'annee', 'nombre']
    with open("/home/laika/Documents/GitHub/NSI_Laika/TraitementDonnees/miniProjet/prenomCombine.csv", 'w', newline='' ) as listPrenomCombine:
        l = []
        L = []
        nbTotal = 0
        for line in dictTotal:
            if dictTotal[line]["prenom"] not in l:
                l.append(dictTotal["prenom"][line])
                nbTotal = nbTotal + dictTotal[line].value()
            elif dictTotal["prenom"][line] in l:
                nbTotal = nbTotal + dictTotal['prenom'][line].value()
            
        L = dict(zip(l, nbTotal))
        objet = csv.DictWriter(listPrenomCombine, fieldnames=field_names, delimiter=',')
        objet.writeheader()
        objet.writerows(l)