from stringprep import c22_specials


def encode(l): 
    "encode une suite de 4bits en 7bits de Hamming"
    d1,d2,d3,d4 = l
    p1 = (d1 + d2 + d4) % 2
    p2 = (d1 + d3 + d4) % 2
    p3 = (d2 + d3 + d4) % 2
    return[p1,p2,d1,p3,d2,d3,d4]


def decode(l):
    p1,p2,d1,p3,d2,d3,d4 = l
    c1 = "0" if (d1 + d2 + d4) % 2 == p1 else "1"
    c2 = "0" if (d1 + d3 + d4) % 2 == p2 else "1"
    c3 = "0" if (d2 + d3 + d4) % 2 == p3 else "1"
    e = int(c1 + c2 + c3, 2)
    if e > 0 :
        l[e-1] = 1 - l[e-1]
            
    return[d1,d2,d3,d4]



x=[0,1,1,0]
print(x)
y = encode(x)
y[4]= 1 - y[4]
decode(y)
