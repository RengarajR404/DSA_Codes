class Empty(Exception):
    """Error attempting  """
    pass
class ArrayStack:
    def __init__(self):
        self._data=[]
        """Creates an empty Stack """
    def __len__(self):
        """Returns the number of elements in python lists"""
        return len(self._data)
    def is_empty(self):
        """ Returns True or False based on the data inside it """
        return len(self._data)==0
    def push(self, e):
        """Add e in stack"""
        self._data.append(e)
    def top(self):
        """Reurns data at the topmost place but not remove it.
        Should also be able to raise exception if in case the stack is empty"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]
    def pop(self):
        """ Removes and returns the top most value of the stack
            Raise exception is stack is empty"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()