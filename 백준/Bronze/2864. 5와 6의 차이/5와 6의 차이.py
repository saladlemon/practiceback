A, B = map(str, input().split())
Amin = A.replace("6", "5")
Bmin = B.replace("6", "5")
Amax = A.replace("5", "6")
Bmax = B.replace("5","6")
Smin = int(Amin)+int(Bmin)
Smax = int(Amax)+int(Bmax)
print(Smin,Smax)
