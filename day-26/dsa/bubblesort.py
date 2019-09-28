def bs(ar):
    for i in range(len(ar)):
        swap=True
        for j in range(0,len(ar) -i -1):
            if ar[j]>ar[j+1]:
                (ar[j],ar[j+1])=(ar[j+1],ar[j])
                swap=False
                if swap==True:
                    break

data=[-7,8,9,17,-36,0,5]
bs(data)
print("sorted : ")
print(data)
