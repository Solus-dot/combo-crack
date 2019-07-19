a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))
d = int(input("Enter 4th no: "))

x = []
x.append(a)
x.append(b)
x.append(c)
x.append(d)

for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            for l in range(0,4):
                if(i != j and j != k and k != l and l != i):
                    print(x[i],x[j],x[k],x[l])