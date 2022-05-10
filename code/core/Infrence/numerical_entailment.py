from apply import apply

class numerical_entailment(apply):
    pass
def numerical_entailment(node ,context ):
    min = node.i
    counter = 0
    for e in node.ant:
        if (e==True) :
            counter+=1
            if counter>= min:
                return node.con