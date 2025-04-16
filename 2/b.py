def d(x1,x2,y1,y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def dia(k):
    mx = 0
    for i in range(len(k)):
        s = 0
        tx,ty = k[i][0], k[i][1]
        for j in range(len(k)):
            px, py = k[j][0], k[j][1]
            s = d(tx,px,ty,py)
            if s > mx:
                mx = s
    return mx

s = open('27B (1).txt').readlines()
k1 = []
k2 = []
k3 = []
k4 = []
k5 = []
k6 = []
k7 = []
for j in s:
    j = j.split()
    x,y = float(j[0]), float(j[1])
    if x < -4:
        k1.append([x, y])
    elif x > 6:
        if y > 0:
            k2.append([x, y])
        else:
            k3.append([x, y])
    elif x > - 4:
        if x < 1:
            if y > -2:
                k4.append([x, y])
            else:
                k5.append([x, y])
        else:
            if y > 1:
                k6.append([x, y])
            else:
                k7.append([x, y])

a = []
a.append(float(dia(k1)))
a.append(float(dia(k2)))
a.append(float(dia(k3)))
a.append(float(dia(k4)))
a.append(float(dia(k5)))
a.append(float(dia(k6)))
a.append(float(dia(k7)))

print(min(a)*100_000)
s1 = 0
for i in a:
    s1 += i
print( (s1/7) * 100_000)

