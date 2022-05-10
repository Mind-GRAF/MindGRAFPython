from apply import apply

class and_entailment(apply):
    pass

def and_entailment(node ,context ):
    flag=False
    for e in node.ant:
        if (e==True):
            flag=True
        else:
            flag=False
            break
    if(flag==True):
        return node.con