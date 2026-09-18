def affich (list):
    for m in list:
        print("[",end=" ")
        for e in m :
            print(e, end=" ")
        print("]")
    
def placerR (m,l,c):

    for k in range(8):
        m[k][c]="X"
        m[l][k]="X"

        if ( l-k>=0 and c-k>=0) :      
            m[l-k][c-k]="X"
        if (l+k<=7 and c-k>=0) :       
            m[l+k][c-k]="X"
        if (l-k>=1 and c+k<=7) :       
            m[l-k][c+k]="X"
        if (l+k<=7 and c+k<=7) :       
            m[l+k][c+k]="X"
    
    m[l][c]="R"


def full (m,l):
    for ci in range (8):
        if m[l][ci]==" " :
            return -1
    return 1


import random   #var = random.randrange(0,7)

R8=0

#for s in range(8):
while R8==0 :    
    m=[ [" " for j in range(8)] for i in range(8)]
    
    for l in range (8):
        while full(m,l)==-1 :
            c = random.randrange(0,8)
            if m[l][c]==" " :
                break
        if full(m,l)==1 :
            print("Bloqué")
            l=0
            c=0
            break
        
        placerR(m,l,c)
        affich(m)
        print("-"*20,l+1)
        for ci in range (8):
            if m[7][ci]=="R":
                print(" !!! SUCCES !!! "*5)
                R8=1
                break
    print("MW"*40)
      
print("Fin !!")   