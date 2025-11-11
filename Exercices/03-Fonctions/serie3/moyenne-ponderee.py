def moyenne_ponderee(x,y,p):
    return x*p + y*(1-p)

print(moyenne_ponderee(7,10,.5))
print(moyenne_ponderee(7,10,1/3))
print(moyenne_ponderee(7,10,2/3))
