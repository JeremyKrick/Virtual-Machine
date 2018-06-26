class StackMachine:
    #CurrentLine = 0
    #saved = []
    def __init__(self):
        self.items = []
        self.CurrentLine = 0
        self.saved = {}
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

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
        if(var1 == 0):
            self.CurrentLine += var2
    
    def save(self,idx):
        var1 = int(self.items.pop())
        self.saved[idx] = var1

    def get(self,idx):
        var1 = self.saved[idx]
        self.push(var1)
    
    def Execute(self, tokens):
        if(tokens[0] == "push"):
            self.push(tokens[1])
            self.CurrentLine += 1
        elif(tokens[0] == "pop"):
            self.CurrentLine += 1
            if(self.isEmpty()):
                raise IndexError("Invalid Memory Access")
            return self.pop()
        elif(tokens[0] == "add"):
            self.add()
            self.CurrentLine += 1
        elif(tokens[0] == "sub"):
            self.sub()
            self.CurrentLine += 1
        elif(tokens[0] == "mul"):
            self.mul()
            self.CurrentLine += 1
        elif(tokens[0] == "div"):
            self.div()
            self.CurrentLine += 1
        elif(tokens[0] == "mod"):
            self.mod()
            self.CurrentLine += 1
        elif(tokens[0] == "skip"):
            self.skip()
            self.CurrentLine += 1
        elif(tokens[0] == "save"):
            self.save(tokens[1])
            self.CurrentLine += 1
        elif(tokens[0] == "get"):
            if(not (tokens[1] in self.saved)):
                raise IndexError("Invalid Memory Access")
            self.get(tokens[1])
            self.CurrentLine += 1
