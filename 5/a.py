def d(x1,y1,x2,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def dot(k):
    k = []
    mx = 0
    for i in range(len(k)):
        s = 0
        tx,ty = k[i][0], k[i][1]
        for j in range(len(k)):
            px, py = k[j][0], k[j][1]
            if d(tx,ty,px,py) <= 1:
                s+=1
        if s > mx:
            k.clear()
            mx = s
            cntx = tx
            cnty = ty
            k.append([cntx,cnty])
        if s == mx:
            cntx = tx
            cnty = ty
            k.append([cntx,cnty])
    return k

def maxk(k):
    it = []
    mx = 0
    for i in range(len(k)):
        x = k[i][0]
        if x > mx:
            mx = x
            it.clear()
            it.append([k[i][0], k[i][1]])
    return it

s = open('27A.txt').readlines()
k1 = []
k2 = []
k3 = []
k4 = []
for j in s:
    j = j.split()
    x,y = float(j[0]), float(j[1])
    if x < 1:
        if y > 0:
            k1.append([x, y])
        else:
            k2.append([x, y])
    else:
        if y < 2:
            k3.append([x, y])
        else:
            k4.append([x, y])

x1, y1 = maxk(dot(k1))
x2, y2 = maxk(dot(k2))
x3, y3 = maxk(dot(k3))
x4, y4 = maxk(dot(k4))

print(abs(x1+x2+x3+x4)/4*100_000)
print(abs(y1+y2+y3+y4)/4*100_000)
