#task is to take the multiple inputs from the user and then append the appropriate signs at the end of each ine and print it.

def sentence(ph):
    inter=("how","why","what")
    b=ph.capitalize()
    if ph.startswith(inter):
        return "{}?".format(b)
    else:
        return "{}.".format(b)
r=[]
while True:
    i=input("say: ")
    if i=='break':
        break
    else:
        r.append(sentence(i))
print(" ".join(r))
