def d(x1,x2,y1,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def centre(k):
    mn = 10**100
    for i in range(len(k)):
        s = 0
        tx,ty = k[i][0], k[i][1]
        for j in range(len(k)):
            px, py = k[j][0], k[j][1]
            s += d(tx,px,ty,py)
        if s < mn:
            mn = s
            cntx = tx
            cnty = ty
    return [cntx,cnty]

s = open('27_A.txt').readlines()
k1 = []
k2 = []
for j in s:

    j = j.replace(',','.').split()
    x,y = float(j[0]), float(j[1])
    if x < 0:
        k1.append([x,y])
    else: k2.append([x,y])

x1,y1 = centre(k1)
x2,y2 = centre(k2)

print(abs((x1+x2)/2 *10_000))
print(abs((y1+y2)/2 *10_000))
