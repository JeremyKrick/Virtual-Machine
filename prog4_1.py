class Tokenize():
    def __init__(self, str):
        self.str = str
        for line in str:
            words = line.split()
            for n, i in enumerate(words):
                if (words[n] == "push" or words[n] == "pop" or words[n] == "add" or 
                    words[n] == "sub" or words[n] == "mul" or words[n] == "div" or 
                    words[n] == "mod" or words[n] == "skip" or words[n] == "save" or 
                    words[n] == "get"): True
                elif words[n].lstrip('-').isdigit(): True
                else:
                    raise ValueError("Unexpected Token: " + words[n])
