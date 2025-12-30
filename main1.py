def match(w):
    c=0
    l=[]
    for word in w:
        if len(w)>1 and w[0]==w[-1]:
            c=c+1
            l.append(w)
    print("words with repeat characters:",l)
    return c
a=match(['abc','reyaan','amrutha','aca'])
print("same count=",a)

