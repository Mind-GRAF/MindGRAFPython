import itertools
from PropositionSet.py import PropositionSet
from Support.py import Support
class SupportController(Support,PropositionSet):
    def __init__(self, id, node):
        Support.__init__(self, name, id, node, attitudes)
        PropositionSet.__init__(id, name, propset)
        #self.propositionset = []
        
        
        vals = [] 
        #helper method, cross product between two dictionaries
        
    # def cartesian_product(dict1, dict2):
    #     cartesian_dict = {}
    #     dict1_length = len(list(dict1.values())[0])
    #     dict2_length = len(list(dict2.values())[0])
    #     h = []
    #     for key in dict1:
    #       for value in dict1[key]:
    #         if not key in cartesian_dict:
    #             cartesian_dict[key] = []
    #             cartesian_dict[key].extend([value]*dict2_length)
    #         else:   
    #             cartesian_dict[key].extend([value]*dict2_length)
    #     for key in dict2:
    #       cartesian_dict[key] = dict2[key]*dict1_length
    #     return cartesian_dict 
    
    setofspropsets =[[]] #########menennnnnnnnnnn#####
    temp = []
    def combineSupports(setofspropsets):
        
        for index in setofspropsetst:
            var = index.supportset()
            support_sets.append(var)
            x = crossproduct(index, index+1)
            temp.append(x)
            
        for j in temp:
            self.union(j,j+1)    
            
       
    
    def crossproduct(list1, list2):
        for combination in itertools.product(list1, list2):
         return combination
     
    def union(list1, list2):
        final_list = lst1 + lst2
        return final_list 
        
        
        
    def removeFromSupports(propset, attitude):
        
        for v in Support.supportStruct.values():
            if isinstance(v, dict):
                allprops = supportStruct[v]
                for i in allprops:
                    if allprops(i) <= propset:
                        supportStruct[v].remove(propset)
                return supportStruct    
        
        # vals.append(supportStruct.get(attitude))
        # for index in vals:
        #     for j in propset:
        #      if vals(index) == PropositionSet(propset[j]):
        #          Support.supportStruct.pop(vals[index])
        # return supportStruct         
            
            
        #   def removePropFromSupports(supportStruct,node):
         
        #  for v in supportStruct.values():
        #     if isinstance(v, dict):
        #         allprops = supportStruct[v]
        #         for i in allprops:
        #             if allprops(i) == node:
        #               supportStruct[v].remove(node)
        #  return supportStruct            
           
            
            
        
            
            
            