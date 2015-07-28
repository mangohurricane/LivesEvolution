import random
def rworld():
    wlist=[[" "for a in range (8)] for b in range(8)]
    for a in range(random.randint(0,36)):
        wlist[random.randint(1,6)][random.randint(1,6)]="*"
    return wlist

def calculateNeighbour(world,r,c):
    count=0
    for m in range(r-1,r+2):
        for n in range (c-1,c+2):
            if (world[m][n]=="*") and (m!=r or n!=c):
                count+=1
    return count
nworld=rworld() 
for element in nworld:
    print(element)
while 1:
    choise2=input("Update? (Y/N):").upper()
    if choise2=="Y":
        newworld=[[" "for a in range (8)] for b in range(8)]
        for r in range(1,len(nworld)-1):
            for c in range(1,len(nworld[0])-1):
                count=calculateNeighbour(nworld,r,c)
                if count==3 or (newworld[r][c]==" " and count==2):
                    newworld[r][c]="*"
        nworld=newworld
    for element in nworld:
        print(element)