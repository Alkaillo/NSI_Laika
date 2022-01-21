#1.2
'''def SeuilListe(L,val):
    i = 0
    while i < len(L):
        if val < L[i]:
            L[i]=0
        i=i+1
    print(L)
SeuilListe([1,12,15,3],10)'''

#1.3
'''def PlusPetitElement(L):
    print(min(L))

PlusPetitElement([1,12,15,3])'''

#1.4
'''def EchangeElement(L,i,j):
    if i in L:
        if j in L:
            index1= L.index(i)
            index2= L.index(j)
            L[index1], L[index2] = L[index2],L[index1]
            print(L)
        else:
            print("une ou plusieurs valeur(s) n'est/ne sont pas dans la liste")

EchangeElement([73,12,11],73,87)'''

#1.5
'''def check_palindrome(v): 
    reverse = v[::-1]  
  
    if (v == reverse): 
        print(True)
    else:
        print(False) 
  
check_palindrome([1,2,1])'''

#1.6
'''def ComptageListe(L,val):
    w = 0
    i = 0
    for i in range(len(L)):
        if L[i] == val:
            w = w+1
            i = i+1
        else:
            i = i+1
    print(w)
ComptageListe([78,78,78,78,4,6,72,5,3], 78)'''

