# Write a function in python that can 
# reverse a string using stack data structure. 
# Use Stack class.


#2.Write a function in python that checks if 
# paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". 
# Use Stack class from the tutorial.

from collections import deque

class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def look(self):
        return self.container

    def rev(self,val):                
        self.content = deque()
        for i in val:
            self.content.append(i)
        x = ""
        while len(self.content) != 0:
            x+=self.content.pop()    
        return x
    
    def is_balance(self,val):
        self.cont = deque()
        for i in val:
            self.cont.append(i)

        if self.cont.count("(") == self.cont.count(")") and self.cont.count("{") == self.cont.count("}") and self.cont.count("[") == self.cont.count("]") :
            print(True)
        else:
            print(False)

    

s = stack()
s.push('aniket')

s.push('ani')

# s.push('nike')

print(s.look())
print(s.rev('nike'))

print(s.rev('kl mai nhi aa raha a'))

s.is_balance("))((a+b)}{")
s.is_balance("((a+b))")



#solution given
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0



