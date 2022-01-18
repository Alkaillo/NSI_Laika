'''import statistics
import numpy
rectangle_list = [4.5, 6, 7.5]
def is_square():
    if rectangle_list[0]**2 + rectangle_list[1]**2 == rectangle_list[2]**2:
        is_square = True
        print(is_square)
    else:
      is_square = False
       print(is_square)

is_square()

def min_max_moy(a_list):
    maxi=max(a_list)
    mini=min(a_list)
    moy = statistics.mean(a_list)
    print(maxi,mini,moy)

min_max_moy([7,9,71,6,27,89])

def is_square(rectangle_list):
    if rectangle_list[0]**2 + rectangle_list[1]**2 == rectangle_list[2]**2:
        is_square = True
        print(is_square)
    else:
      is_square = False
       print(is_square)

is_square([4.5, 6, 7.5])

def min_max_moy(a_list):
    maxi=max(a_list)
    mini=min(a_list)
    moy = statistics.mean(a_list)
    print(maxi,mini,moy)

min_max_moy([7,9,71,6,27,89])


pays = {
    'paris':{'pays':'france',
    'distance':float(391.18),
    'nb_habit':2590771}
}

def ficheCp(capital):
    cp = str(capital)
    print(pays[cp])
    

ficheCp('paris')

def distanceInferieur(distanceInf):
    dis = float(distanceInf)
    print(pays['']['distance'] < dis)'''