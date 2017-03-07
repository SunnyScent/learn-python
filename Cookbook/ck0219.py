""" 实现一个简单的递归下降分析器
    BNF 巴科斯范式
    expr ::= expr + term
         |   expr + term
         |  term

    term ::= term * factor
         |   term / factor
         |   factor

    factor ::= ( expr )
         |   NUM


    EBNF 扩展巴科斯范式
    expr ::= term { (+j-) term }*

    term ::= factor { (*j/) factor }*

    factor ::= ( expr )
         | NUM
"""
