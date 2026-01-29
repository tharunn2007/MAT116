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

#implication logic 
def implication(p,q):
    return not p or q
print("____________")
print("p \t q \t p IMPLIES q")
print("____________")
for p in (True,False):
    for q in (True,False):
        print (p,"\t",q ,"\t",implication(p,q))
print()

#biconditional logic
def biconditional(p,q):
    return not((p and not q) or (q and not p))
print("____________")
print("p \t q \t p only if q")
print("____________")
for p in (True,False):
    for q in (True,False):
        print (p,"\t",q ,"\t",biconditional(p,q))
print()



#practice questions
"""justification for each step in the proof that ((p ∨ q) ∧ (p ∨ ¬q)) ∨ q
simplifies to (p ∨ q)."""
def q1(p,q):
    return((p or q)and(p or not q)or q)
print("____________")
print("p \t q \t ((p ∨ q) ∧ (p ∨ ¬q)) ∨ q")
print("____________")
for p in (True,False):
    for q in (True,False):
        print (p,"\t",q ,"\t",q1(p,q))
print()


#2. (𝑝 → 𝑞)⋁(𝑞 → 𝑟) 
def q2(p,q,r):
    return((not p or q)or (not q or r))
print("________________________________")
print("p \t q \t r \t (r → q)⋁(q → r)")
print("________________________________")
for p in (True,False):
    for q in (True,False):
        for r in (True,False):
            print (p,"\t",q ,"\t",r,"\t",q2(p,q,r))

      




