def or_entailment(RuleNode):
    for e in RuleNode.downCableS.antecedents:
        for i in RuleNode.downCableS.antecedents(e).supports:
            if RuleNode.downCableS.antecedents(e).supports(i).sign == True:
                return RuleNode.downCableS.consequents
