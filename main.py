import calculate
import tkinter as tk
from tkinter import ttk
from tkinter import *

# class Application(Frame):
#     def __init__(self) -> None:
#         self._top
#     def calc(self, expression):
#         ans = calculate.compute(expression)
#         if ans[0] != 0:
#             print(ans)
#         return ans[1]


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        options = {'padx': 5, 'pady': 5}
        self.__keys = ['\u232B', '/', '*', 'clear', '1', '2', '3', '+', '4', '5',
                       '6', '-', '7', '8', '9', '^', '0', '00', '.', '=']
        self.__create_widgets()

    @staticmethod
    def __addtoexp(ent: ttk.Entry, c: str):
        """update entry text

        Args:
            ent (ttk.Entry): entry text
            c (str): button text
        """
        if c == '\u232B':
            ent.delete(END-1, END)
        elif c == 'clear':
            ent.delete(0, END)
        elif c == '=':
            ans = calculate.compute(ent.get())
            ent.delete(0, END)
            ent.insert(0, ans[1])
        elif c == '(':
            if ent.get()[-1].isdigit():
                c = '*'
            ent.insert(END, c)

        else:
            ent.insert(END, c)
        ent.focus()

    def __create_widgets(self):
        """create widgets for layout
        """
        options = {'padx': 2, 'pady': 2}
        self.__expent = ttk.Entry()
        self.__expent.grid(row=0, column=0, columnspan=4,
                           **options, sticky='NSEW')
        self.__expent.focus()
        self.__expent.bind(
            '<Return>', lambda j: self.__addtoexp(self.__expent, '='))
        self.__expent.bind(
            '<Escape>', lambda j: self.__addtoexp(self.__expent, 'clear'))
        self.__expent.bind(
            '(', lambda j: self.__addtoexp(self.__expent, '('))
        self.__buttons = []
        x = 4
        for key in self.__keys:
            button = ttk.Button(
                text=key, command=lambda j=key: self.__addtoexp(self.__expent, j))
            button.grid(column=x % 4, row=x//4, sticky='NSEW', ** options)
            self.__buttons.append(button)
            x = x+1


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')


if __name__ == '__main__':
    app = App()
    frame = MainFrame(app)
    app.mainloop()
