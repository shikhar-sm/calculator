# infix to postfix

import stack
import re


def inftopof(infix):
    """infix to postfix

    Args:
        infix (str): infix expression

    Returns:
        str: postfix expression
    """
    delim = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    redelim = '(\+|-|\*|/|\^|\(|\))'
    tokens = re.split(redelim, infix)
    # print(tokens)
    output = stack.stack()
    ops = stack.stack()
    for t in tokens:
        if t in delim.keys():
            x = delim[t]
            if ops.seek() == None:
                ops.push(t)
            else:
                while(ops.seek() != None and ops.seek() != '(' and delim[ops.seek()] >= x):
                    output.push(ops.pop())
                ops.push(t)
        elif t == '(':
            ops.push(t)
        elif t == ')':
            while(ops.seek() != '('):
                output.push(ops.pop())
            ops.pop()
        else:
            output.push(t)
        # print(output)
        # print(ops)
    while ops.seek() != None:
        output.push(ops.pop())
    return output


# print(inftopof('10+15/16*16-19(24*34)'))
