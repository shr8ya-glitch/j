def hc(n):
    return n*140
def pr(c):
if "Charlotte"==c:
    return 183
elif "Tampa"==c:
    return 220
elif "Pittusburgh"==c:
    return 222
elif "Los Angeles"==c:
    return 475
def rc(d):
    if d>=7:
    return 40*d-50
   elif d>=3:
    return 40*d-20
else:
return 40*d
def tc(c,d,s):
    return rc(d)+hc(d)+pr(c)+s
print("car rental:",rc(5))
print("Plane ride:",pr("Los Angeles"))
print("hotel cost:",hc(7))
print("total cost:",tc("Los Angeles",7,500))
print("trip cost",tc("Tampa",6,500))