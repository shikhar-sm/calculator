import calculate


class Application():
    def calc(self, expression):
        ans = calculate.compute(expression)
        if ans[0] != 0:
            print(ans)
        return ans[1]


app = Application()
inp = input("Enter expression: ")
print(app.calc(inp))
