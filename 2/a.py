def d(x1,y1,x2,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def dia(k):
    mx = 0
    for i in range(len(k)):
        s = 0
        tx,ty = k[i][0], k[i][1]
        for j in range(len(k)):
            px, py = k[j][0], k[j][1]
            s = d(tx,ty,px,py)
            if s > mx:
                mx = s
    return mx

s = open('27A (1).txt').readlines()
k1 = []
k2 = []
k3 = []
k4 = []
for j in s:
    j = j.split()
    x,y = float(j[0]), float(j[1])
    if (x < 0) and (y > 0):
        k1.append([x,y])
    elif (y<0) and (x < 1):
        k2.append([x, y])
    elif (x > 2) and (y > 2):
        k3.append([x, y])
    else:
        k4.append([x,y])

a = []
a.append(float(dia(k1)))
a.append(float(dia(k2)))
a.append(float(dia(k3)))
a.append(float(dia(k4)))

print(min(a)*100_000)
s1 = 0
for i in a:
    s1 += i
print( (s1/4) * 100_000)

