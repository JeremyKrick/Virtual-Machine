class StackMachine:
    CurrentLine = 0
    save = []
    def __init__(self, items):
        self.items = []
        self.Execute(items)
        #print(items)
        
    def push(self, item):
        self.items.append(item)
        print(item)

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
    """
    def skip(self):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        if(var1 == '0'):
            CurrentLine = var2
        
        var3 = var1 * var2
        self.push(var3)
    """
    def save(self, item):
        var1 = int(self.items.pop())
        save.append(var1)
    """
    def get(self, item):
        var1 = int(self.items.pop())
        var2 = int(self.items.pop())
        var3 = var1 * var2
        self.push(var3)
    """
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
