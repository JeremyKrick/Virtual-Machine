class StackMachine:
    CurrentLine = 0
    saved = []
    def __init__(self):
        self.items = []
        #self.Execute(items)
        #self.saved = []
        #print(items)
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def add(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 + var2
        self.push(var3)

    def sub(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 - var2
        self.push(var3)
    
    def mul(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 * var2
        self.push(var3)

    def div(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 / var2
        self.push(var3)

    def mod(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 % var2
        self.push(var3)

    def skip(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        if(var1 == '0'):
            StackMachine.CurrentLine += var2
        else:
            StackMachine.CurrentLine += 1
    
    def save(self):
        var1 = int(self.items.pop())
        StackMachine.saved.append(var1)

    def get(self):
        var1 = StackMachine.saved[-1]
        self.push(var1)
    
    def Execute(self, tokens):
        if(tokens[0] == "push"):
            self.push(tokens[1])
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "pop"):
            StackMachine.CurrentLine += 1
            return self.pop()
        elif(tokens[0] == "add"):
            self.add()
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "sub"):
            self.sub()
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "mul"):
            self.mul()
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "div"):
            self.div()
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "mod"):
            self.mod()
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "skip"):
            self.skip()
        elif(tokens[0] == "save"):
            self.save()
            StackMachine.CurrentLine += 1
        elif(tokens[0] == "get"):
            self.get()
            StackMachine.CurrentLine += 1
"""
        for n, i in enumerate(tokens):
            if(tokens[n][0] == "push"):
                self.push(tokens[n][1])
            elif(tokens[n][0] == "pop"):
                self.pop()
            elif(tokens[n][0] == "add"):
                self.add()
            elif(tokens[n][0] == "sub"):
                self.sub()
            elif(tokens[n][0] == "mul"):
                self.mul()
            elif(tokens[n][0] == "div"):
                self.div()
            elif(tokens[n][0] == "mod"):
                self.mod()
            elif(tokens[n][0] == "skip"):
                self.skip()
            elif(tokens[n][0] == "save"):
                self.save()
            elif(tokens[n][0] == "get"):
                self.get()
"""
