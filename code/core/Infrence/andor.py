from code.core.Infrence.apply import apply

class andor (apply):
    pass

def andor(node ,context ):
    min = node.i
    max = node.j
    counter =0
    for e in node.ant:
        if(e==True):
            counter+=1
            if(counter>=max):
                return node.con