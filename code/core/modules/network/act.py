from pickle import FALSE, TRUE
from pydoc import resolve
from code.core.modules.network.agenda import agenda


class act(Entity) :
    def __init__(self) -> None:
        super().__init__()
        self.stage = agenda.start
    
    def start(act):
        #find a plan for supported complex acts or exexcute 
        #if the act is primitive else terminate the system
        if is_supported(act):
            if(act.is_primitive):
             act.stage = agenda.find_preconditions
             find_preconditions(act)
            else:
                act.stage = agenda.find_plan
                find_plan(act)
        else:
            print("This action is not supported")
            return

    def find_plan(act) :
      #find a plan if exists, push the plan to the stack 
      #then pull the first act and start again (to check if primitve)
     plans = backward_chain(act) 
     if(plans.isEmpty()):
         print("No possible plans were found")
         return FALSE
     else:
        plan = plans.do_one
        actStack.push(plan)
        act.stage = agenda.find_preconditions
        new_act = actStack.pull()
        new_act.stage = agenda.start
        start(new_act)

    def execute(act) :
     #execute primitive acts
     if(act.isPrimitive):
        act.executePrimitive()
        act.stage = agenda.find_effects
        find_effects(act)
     #find a plan for complex acts
     else:
        act.stage = agenda.start
        start(act)

    def test_precondition(precondition):
        #check that the preconditions are asserted else return false
        if precondition.isAsserted():
         return TRUE
        else :
         return FALSE

    def find_preconditions(act) :
     #check for preconditions and test them else execute
     preconditions = backward_chain(act)
     if(not preconditions.isEmpty()):
       act.stage = agenda.test
       for precondition in preconditions:
        isSatisfied = test_precondition(precondition)
        #if preconditions are not satisfied find another plan, else continue executing
        if not isSatisfied:
            #try finding another way to reach this act
            act.stage = agenda.find_plan
            planFound = find_plan(act)
            #if no plan is found try finding a plan for the initial act
            if(not planFound):
             while not actStack.isEmpty():
              act = actStack.pop()
            find_plan(act)
        else:
            act.stage = agenda.execute
            execute(act)
     else:
      stage = agenda.execute

    def find_effects(act) :
        #check effects by traversing the support & precond or from the user's input 
        external_effect = input("Enter effects")
        internal_effect = forward_chain(act)
        #believe both effects then solve contradiction if found
        believe(internal_effect)
        believe(external_effect)
        if(check_contradiction(external_effect)):
          resolve_contradiction(external_effect)
        if(check_contradiction(internal_effect)):
          resolve_contradiction(internal_effect)
        act.stage = done


