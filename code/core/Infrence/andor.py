from apply import apply

class andor (apply):
    pass

def andor(node ,context ):
    min = node.i
    max = node.j
    counter =0
    for e in node.ant:
        if(e==True):
            counter+=1
            if(counter==max):
                node.con=node.ant.iter(max)
                return node.con
            elif(counter==min):
                node.con=node.ant.remove(node.ant.iter(node.size-min))
                return node.con