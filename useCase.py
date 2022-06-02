import sys

if len(sys.argv)!=6:
    print("error invalid arg count")
    print("usage : python3 "+sys.argv[0]+"<input_file> <a> <b> <M> <MAF>")
    exit(0)

print("Start")

ifile = open(sys.argv[1],"r")
dist = list(map(int,ifile.readline().split(",")))
l = sum(dist)
n = len(dist)
thetas = []
for i in range(0,n):
    line = ifile.readline()
    li = list(line.split(","))
    li = list(map(int,li))
    thetas.append(li)

u = []
for i in range(0,l):
    ui=0
    for j in range(0,n):
        ui+=thetas[j][i]
    ui/=n
    u.append(ui)

s = []

for j in range(0,n):
    sj=0
    for i in range(0,l):
        sj+=(u[i]-thetas[j][i])**2
        # print((u[i]-thetas[j][i])**2)
    sj = (sj/l)**0.5
    s.append(sj)
print("Number of Recognised Players")
print(l)
print("Number of Academies")
print(n)
print("Player Distribution")
print(dist)
print("Type Sets(private info by the Academy Representatives")
print(thetas)
print("Mean Rating of Recognised Players")
print(u)
print("Deviation of Type Sets of Academy Representatives")
print(s)

#Mean Sports Rating Among All Players
D = 0
for j in range(0,n):
    for i in range(0,l):
        D+=thetas[j][i]
D/=n*l

#Assigning Academies to Players
a = 0
acad = []
for i in dist:
    for j in range(0,i):
        acad.append(a)
    a+=1

#mean of Standard Deviation
us = sum(s)/len(s)
ss = []
for i in range(0,n):
    sj = s[i]-us
    ss.append(sj)

#Social Choice Function - 2
a=float(sys.argv[2])
b=float(sys.argv[3])
M=int(sys.argv[4])
MAF=int(sys.argv[5])

player_utility =[]

for i in range(0,l):
    v = a*(u[i]-D) - b*ss[acad[i]]    
    if(v<0):
        player_utility.append(0)
    elif v>=0 and v<M:
        player_utility.append(v)
    else:
        player_utility.append(M)

all_u = sum(player_utility)
representative_utility = []
for j in range(0,n):
    players = [idx for idx, element in enumerate(acad) if element == j]
    print(players)
    sum_u = 0
    for i in players:
        sum_u+=player_utility[i]
    sum_u/=all_u
    sum_u*=MAF
    representative_utility.append(sum_u)



print("Academies of each Player")
print(acad)
print("Average Rating Among All Players : {}".format(D))
print("Mean Of Deviations of Academy Representatives : {}".format(us))
print("[Deviation - Mean(Deviations)] of Academy Representatives ")
print(ss)
print("a: {}, \tb: {}, \tM: {}, \tMAF: {}".format(a,b,M,MAF))
print("Utility of Recognised Players")
print(player_utility)
print("Sum of Utility of All Recognised Players: {}".format(all_u))
print("Utility of Academy Representatives")
print(representative_utility)
