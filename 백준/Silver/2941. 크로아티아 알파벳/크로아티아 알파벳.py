N = input()
cnt = 0
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in croatia:
    N = N.replace(i, "*")
print(len(N))