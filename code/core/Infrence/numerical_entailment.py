def numerical_entailment(RuleNode):
    min = RuleNode.downCableS.min
    counter = 0
    for e in RuleNode.downCableS.antecedents:
        for i in RuleNode.downCableS.antecedents(e).supports:
            if RuleNode.downCableS.antecedents(e).supports(i).sign == True:
                counter += 1
                if counter >= min:
                    return RuleNode.downCableS.consequents
