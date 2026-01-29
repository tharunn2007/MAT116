#negation logic
def negation(p):
    return not p
print("____________")
print("p \t ~p")
print("____________")
for p in (True,False):
    print(p,"\l",negation(p))
print()


# exclusive_or logic
def exclusive_or(p,q):
    return (p and not q) or (q and not p)
print("____________")
print("p \t q \t p XOR q")
print("____________")
for p in (True,False):
    for q in (True,False):
        print (p,"\t",q ,"\t",exclusive_or(p,q))
print()


