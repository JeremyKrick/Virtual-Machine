class StackMachine:
    #CurrentLine = 0
    #save = []
    def __init__(self, items):
        self.items = []
        self.Execute(items)
        self.save = []
        self.CurrentLine = 0
        #print(items)
        
    def push(self, item):
        StackMachine.CurrentLine += 1
        self.items.append(item)
        #print(item)

    def pop(self):
        StackMachine.CurrentLine += 1
        return self.items.pop()
    
    def add(self):
        StackMachine.CurrentLine += 1
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 + var2
        self.push(var3)

    def sub(self):
        StackMachine.CurrentLine += 1
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 - var2
        self.push(var3)
    
    def mul(self):
        StackMachine.CurrentLine += 1
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 * var2
        self.push(var3)

    def div(self):
        StackMachine.CurrentLine += 1
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 / var2
        self.push(var3)

    def mod(self):
        StackMachine.CurrentLine += 1
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
        StackMachine.CurrentLine += 1
        var1 = int(self.items.pop())
        StackMachine.save.append(var1)

    def get(self, item):
        StackMachine.CurrentLine += 1
        var1 = StackMachine.save[-1]
        self.push(var1)
    
    def Execute(self, tokens):
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
