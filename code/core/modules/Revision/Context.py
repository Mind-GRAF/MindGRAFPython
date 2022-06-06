from Support.py import Support
from PropositionSet.py import PropositionSet
from operator import itemgetter
class Context: 
    
    def __init__(self):
        pass 
    
    def __init__(self, name, hyps, id):
        self.name = name
        self.hyps = hyps
        self.id   = id
        

    hyps: {}
    # def populatehyps():
    #  keys = range(len(attitudes))
    #  values = PropositionSet(propset) #call constructor of proposition set 
    #  for i in keys:
    #     hyps[i] = values(i)
    #     return hyps        
        
    def generate_sets(sets_input):
        
        sets_input = re.sub(" ", "", sets_input)
        sets_input = sets_input[1:-1]

        index1 = 0

        for current_index, character in enumerate(sets_input):
            if character == '[':
                index1 = current_index + 1
                continue

            if character == ']':
                result.append(get_set_from_comma_separated(sets_input[index1:current_index]))

        return result
        

    def get_set_from_comma_separated(text):
         generated_set = set()

         split_text = text.split(',')
         for item in split_text:
            generated_set.add(item)

         return frozenset(generated_set)
     
    def insert_into_dictionary(key, sets_array, dictionary):
        if Context.getIndex(key) not in hyps:
            hyps[Context.getIndex(key)] = set()

        for item in sets_array:
            hyps[Context.getIndex(key)].add(item) 
            
            
    

    for i in range(0, 5):
        input_key = input("Enter key")

        generated_sets = generate_sets(input("Enter sets"))
        insert_into_dictionary(input_key, generated_sets, hyps)        
            
    def get_context(self):
         return self._name
        
    # def addtoContext(node, attitude):  
    #     hyps[self.getIndex(attitude)].append(node)

        
    def isSupported(node, attitude):
        x = Support.supportStruct[node.supportset()]
        if isinstance(x, dict):
            
            for i in x:
                supps = list(Support.supportStruct[key])
                for j in hyps:
                    if supps <= list(hyps.get((Context.getIndex(attitude)))):
                       return True
                 
                    return False         
         # dictofsupports = dict(Support.supportStruct.get(key))
        # for i in dictofsupports:
        #     if key in Support.supportStruct.keys():     
        #      res = list(map(itemgetter(key), Support.supportStruct))
             
    def setAttitudes(attitude):
        setofattitudes = [ ] 
        input_string = input("Enter all attitudes separated by space  ")
        # Split string into words
        family_list = input_string.split(" ")
        for attitude in family_list:
            setofattitudes.append(attitude)
            
        return setofattitudes    
    
    x = setofattitudes 

         
    def setconsistentatts(consistentatts):
        setofconistentatts = [ ] 
        n = int(input("Enter number of elements : ")) 
        
        for i in range(0, n): 
            ele = [input(), int(input())] 
            setofconistentatts.append(ele) 
        return setofconistentatts
        
    y = setofconistentatts        
     
    def getIndex(key):
        for i in setofattitudes:
            if setofattitudes(i)==key:
                return i 
        
   # Attitudes = hyps.keys()
    #def search(Attitudes, a):
     #     for i in range(len(Attitudes)):
      #      if Attitudes[i] == a:
       #       return True
        #  return False
        
        #setconsistent
 
    def contexttoString():
        
       return str(self.id) + str(self.hyps) + str(self.name)
  
    key_list = list(hyps.keys())
    val_list = list(hyps.values())
    presentin = []
    def checkContradiction(node):
        
        #for i in self.setofconsistentatts {B,I},{O,D}
        # badal ! check andor with 0.0:
        
        for i in Context.val_list:
            if val_list(i)== node:
                att = val_list.index(node)
                Context.presentin.append(att)
                
                
        for j in Context.setofconistentatts:
            key =  Context.getIndex(Context.setofconistentatts(j))
            keystring = Context.setofconistentatts(j)
            
            v_list = list(hyps[key])
            # if node and !node in v_list:
                  #val_to_resolve = (node,!node,keystring)
                  #Context.resolveContradiction(val_to_resolve)
            #     return valtoresolve
            # else:
            #     return ""
            
         
   
        #node.supportset in an attitude in resolve 
        #ret a tuple that says the nodes that contradict each other and the attitude they are in
        #law mafeesh contradictionn ret empty string
        
    
    # def resolveContradiction(val_to_resolve):
        
    #     val = list(val_to_resolve)
    #     del hyps[val(2)[val(1)]]
    #hayerga3li not p w edisres, haseel not p men desires
     
     
    
#hakhod node
#1. check law node.downcable.rel (negation) is in the same context
#2. if false, break, return no contradiction
#3. if true:
#4. check the consistent attitudes, if negation of the node and the node are both present in
#   attitudes that have to be consistent. 
#5. if false; break.
#6. if true; check if the node and its negation are supported.


#def checkContradiction(node):
    
   # if node.ant(e).downcable.channels(i).report.sign == 
   
   #check if n and not n are supported in the context for that set
   
   #hansheel n or not n? ask the user
   #if they want to remove n
   #hanrooh lel values that are in att 1 that pass the test and display them to the user
   #remove one from each row so it is no longer supported
   #update hyps
   #give the supports n and ask to remove one node from each cell
   
   
   