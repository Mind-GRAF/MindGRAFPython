from PropositionSet.py import PropositionSet
from Context.py import Context
class Support:
     def __init__(self, name, id, node, attitudes):
         self.name   = name
         self.id = id
         self.node = node
         self.attitudes = attitudes #not yet in thesis 27/5
         
         attitudes = Context.setofattitudes()
         
         supportStruct: {}
 
    
    
    
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
    
    #  def insert_into_nested_dictionary(key, innerkey, sets_array, dictionary):
    #      if Context.getIndex(key) not in dictionary:
    #         supportStruct[Context.getIndex(key)][Context.getIndex(innerkey)] = set()

    #      for item in sets_array:
    #         supportStruct[Context.getIndex(key)][Context.getIndex(innerkey)].add(item) 
        
        

   
        
     def insert_into_two_dimensional_dict(key1, key2, new_set_of_values, dictionary):
        
        attitude_mainkey = (Context.getIndex(key1))
        attitude_innerkey = (Context.getIndex(key2))
        
        if attitude_mainkey not in supportStruct:
            supportStruct[attitude_mainkey] = {}

        if attitude_innerkey not in supportStruct[attitude_mainkey]:
            supportStruct[attitude_mainkey][attitude_innerkey] = set()

        supportStruct[attitude_mainkey][attitude_innerkey].add(new_set_of_values)
    
        return supportStruct
        
        #insert_into_two_dimensional_dict(1, 2, frozenset(["test1", "tes2"]), x)
  
     
    #  def create_support(node, attitude):
         
    #      self.supportStruct = add_values_in_dict(self.supportStruct, Context.getIndex(attitude), node)
         
    #      if Context.getIndex(attitude) not in supportStruct:
    #          supportStruct[Context.getIndex(attitude)] = node
         
    #      #3ayza ashoof law feeh key bel attitude da w law feeh azawed value,
    #      #law mafeesh n update el dict
         
    # #helper method to append multiple values to the same key
    #  def add_values_in_dict(supportStruct, key , list_of_values):
    #      if key in self.supportStruct:
    #          supportStruct[key] = list()
    #      supportStruct[key].extend(list_of_values)
    #      return supportStruct
    
    
    #  def get_values(supportStruct):

    #      for v in supportStruct.values():
    #         if isinstance(v, dict):
    #           yield from supportStruct(v)
    #         else:
    #           yield v
        
        
    #  allProps = (list(get_values(supportStruct)))
     
     
    #  def removePropFromSupports(node):

    #       for i in allProps:
    #               if allProps(i) == node:
    #                   allProps.remove(node)
                      
                       
     def removePropFromSupports(supportStruct,node):
         
         for v in supportStruct.values():
            if isinstance(v, dict):
                allprops = supportStruct[v]
                for i in allprops:
                    if allprops(i) == node:
                      supportStruct[v].remove(node)
         return supportStruct            
        