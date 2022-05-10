class Support:
     def __init__(self, id, node):
         self.id = id
         self.node = node
         
         supportStruct: ({'Beliefs': 'Geeks',
           'Desires': 'For',
           'Intentions':'Geeks'})
     #props used to derive a propo for which this is a support
     #attitude:support
     
     def createSupport(Proposition p, Attitude a):
         
         supportStruct = add_values_in_dict(supportStruct, 'a', p)
         
         if a not in supportStruct:
             supportStruct[a] = p
         
         #3ayza ashoof law feeh key bel attitude da w law feeh azawed value,
         #law mafeesh n update el dict
         
    #helper method to append multiple values to the same key
     def add_values_in_dict(supportStruct, key , list_of_values):
         if key in supportStruct:
             supportStruct[key] = list()
         supportStruct[key].extend(list_of_values)
         return supportStruct
         
    
         
     def removePropFromSupports(Proposition p):
              
        allProps = supportStruct.values()
              for i in allProps:
                  if allProps[i] == p:
                      allProps.remove(p)
              
          