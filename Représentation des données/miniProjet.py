inp = input('Souhaitez vous ajouter, supprimer ou rechercher un numéro ? ')

L = {}
if inp == 'ajouter' or "add" :
    num = input('Quel numéro souhaitez vous ajouter ? ')
    name = input('Pour quel nom ? ')
    L[name : num]

elif inp == 'supprimer' or 'del' or 'delete':
    del_name = input('Quel nom souhaitez vous supprimer ? ')
    if del_name in L['name']:
        del L[del_name]
        print('le nombre à été supprimé')
    else:
        print("le nom n'existe pas")

if inp == 'rechercher':
    search_name = input('Quel nom souhaitez vous rechercher ? ')
    if search_name in L['name']:
        print(L[search_name : 'num'])
    else :
        print("Ce nom n'existe pas")