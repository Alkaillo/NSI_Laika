'''#exercice 1 : 

def renduMonnaieGlouton(x):
  piece = [5,2,1]
  i = 0
  while(x>0):
    if(piece[i] > x):
      i = i+1
    else:
      print(str(piece[i]))
      x -= piece[i];
renduMonnaieGlouton(13) #5,5,2,1
'''

#exercice 2 
'''def renduMonnaieGlouton(x):
  piece = [30,24,12,6,3,1]
  i = 0
  while(x>0):
    if(piece[i] > x):
      i = i+1
    else:
      print(str(piece[i]))
      x -= piece[i];
renduMonnaieGlouton(48) #36,12,6'''

#exercice 3
Listmalle = [{"nom": "train", "taille":18},{"nom": "pin", "taille":15}] 

def place_occupe():
    w = 0
    for i in Listmalle:
        i = int(i)
        w = w + Listmalle[i]
    print(w)
place_occupe()