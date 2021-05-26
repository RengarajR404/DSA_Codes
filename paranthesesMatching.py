import stack
"""Return True if all delimiters are proprly matched
   False otherwise"""
def is_matched(expr):
    left="({["
    right=")}]"
    S= stack.ArrayStack()
    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c)!=left.index(S.pop()):
                return False
    return S.is_empty()
print(is_matched('[{7+(5+x)-(y+z)}]'))
