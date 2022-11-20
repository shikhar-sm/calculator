# implement stack data structure in python

class stack:
    """stack implementation
    """

    def __init__(self) -> None:
        self._st = list()

    def push(self, ele):
        """push to stack

        Args:
            ele (Any): element to be pushed
        """
        self._st.append(ele)

    def pop(self):
        """pop from stack (remove top element)

        Returns:
            Any: element on top of stack or None if stack is empty
        """
        if len(self._st) > 0:
            return self._st.pop()
        else:
            return None

    def seek(self):
        """seek

        Returns:
            Any: element on top of stack or None if stack is empty
        """
        if len(self._st) > 0:
            return self._st[-1]
        else:
            return None

    def __str__(self) -> str:
        """converts stack to string

        Returns:
            str: string equivalent of stack
        """
        s = ''
        for i in self._st:
            s = s+str(i)+' '
        return s
