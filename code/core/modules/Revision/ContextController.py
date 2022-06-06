class ContextController(Context):
      
      def __init__(self, contextSet, attitudeSet, id):
        super().__init__(self, contextSet, attitudeSet)
        
        
      
      
      # setOfAttitudes = ["Beliefs", "Desires", "Intentions", ]
      # #setter dynamic
      
      # def setAttitudes(attitude):
      #   setofattitudes = [ ] 
      #   input_string = input("Enter all attitudes separated by space  ")
      #   # Split string into words
      #   family_list = input_string.split(" ")
      #   for attitude in family_list:
      #       setofattitudes.append(attitude)
            
      def getkey(val):
          for key, value in Context.hyps.items():
              if val == value:
                  return key
      
          return "key doesn't exist"
        
      
      setOfContexts = []
      #append self fel constructor
      
      #method to translate set pf attitudes to indices and then haave them be the key to both dictionaries.
     
     
      def removeContext(context): 
        setOfContexts.remove((Context(context.id)) 
          

   
