# solve expression

import tools.intopost as ip
import tools.stack as stack


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
        fans = answer.pop()
        # print(answer)
        if answer.seek() != None:
            raise Exception("Invalid Expression"+' '+str(answer))
        else:
            return (0, fans)
    except ValueError:
        return (1, "Math Error")
    except Exception as e:
        return (1, 'error: '+e.__str__())
