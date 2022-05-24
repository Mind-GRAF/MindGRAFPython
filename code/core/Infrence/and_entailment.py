def and_entailment(RuleNode):
    flag = False
    for e in RuleNode.downCableS.antecedents:
        for i in RuleNode.downCableS.antecedents(e).supports:
            if RuleNode.downCableS.antecedents(e).supports(i).sign == True:
                flag = True
            else:
                flag = False
                break
    if flag == True:
        return RuleNode.downCableS.consequents
