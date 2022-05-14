from agenda import agenda


class act(Entity) :
   
    def __init__(self) -> None:
        super().__init__()
        self.stage = agenda.start
    
    def start(act):
        #find a plan for supported complex acts or excute 
        #if the act is primitive else terminate the system
        if isSupported(act):
            if(act.is_primitive):
             act.stage = agenda.find_preconditions
             act.find_preconditions(act)
            else:
              act.stage = agenda.find_plan
              act.find_plan(act)
        else:
            print("This action is not supported")
            return

    def find_plan(act) :
      #find a plan if exists, push the plan to the stack 
      #then pull the first act and start again (to check if primitve)
     plans = BackwardChain(act) 
     if(plans.count()==0):
         print("No possible plans were found")
         return False
     else:
        plan = plans.do_one
        actStack.push(plan)
        act.stage = agenda.find_preconditions
        new_act = actStack.pull()
        new_act.stage = agenda.start
        act.start(new_act)

    def execute(act) :
     #execute primitive acts
     if(act.isPrimitive):
        act.executePrimitive()
        act.stage = agenda.find_effects
        act.find_effects(act)
     #find a plan for complex acts
     else:
        act.stage = agenda.start
        act.start(act)

    def test_precondition(precondition):
        #check that the preconditions are asserted else return false
        if precondition.isAsserted():
         return True
        else :
         return False

    def find_preconditions(act) :
     #check for preconditions and test them else execute
     preconditions = backward_chain(act)
     if(preconditions.count()!=0):
       act.stage = agenda.test_precondition
       for precondition in preconditions:
        isSatisfied = act.test_precondition(precondition)
        #if preconditions are not satisfied find another plan, else continue executing
        if not isSatisfied:
            #try finding another way to reach this act
            act.stage = agenda.find_plan
            planFound = act.find_plan(act)
            #if no plan is found try finding a plan for the initial act
            if(not planFound):
             while actStack.count()>0:
              act = actStack.pop()
            act.find_plan(act)
        else:
            act.stage = agenda.execute
            act.execute(act)
     else:
      stage = agenda.execute

    def find_effects(act) :
        #check effects by traversing the support & precond or from the user's input 
        external_effect = input("Enter effects")
        internal_effect = BackwardChain(act)
        #believe both effects then solve contradiction if found
        ForwardChain(internal_effect)
        ForwardChain(external_effect)
        checkContradiction(external_effect)
          # resolve_contradiction(external_effect)
        checkContradiction(internal_effect)
          # resolveContradiction(internal_effect)
        act.stage = agenda.done


