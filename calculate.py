# solve expression

import intopost as ip
import stack


def compute(expression):
    try:
        postfix = str(ip.inftopof(expression))
        answer = stack.stack()
        # print(postfix)
        ops = ['+', '-', '*', '^', '/']
        postfix = postfix.split()
        for p in postfix:
            if p not in ops:
                answer.push(float(p))
            else:
                x = answer.pop()
                y = answer.pop()
                if p == '^':
                    answer.push(y**x)
                elif p == '+':
                    answer.push(y+x)
                elif p == '-':
                    answer.push(y-x)
                elif p == '*':
                    answer.push(y*x)
                elif p == '/':
                    answer.push(y/x)
        fans = 1
        # print(answer)
        while answer.seek() != None:
            fans = fans * answer.pop()
        return (0, fans)
    except ValueError:
        return (1, "Math Error")
    except Exception as e:
        return (1, "Unknown Error occured", e)
