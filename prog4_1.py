def Tokenize(str):
        words = str.split()
        for n, i in enumerate(words):
            if (words[n] == "push" or words[n] == "pop" or words[n] == "add" or 
                words[n] == "sub" or words[n] == "mul" or words[n] == "div" or 
                words[n] == "mod" or words[n] == "skip" or words[n] == "save" or 
                words[n] == "get"): True
            elif words[n].lstrip('-').isdigit(): True
            else:
                raise ValueError("Unexpected Token: " + words[n])
        return words

def Parse(tokens):
    if(isValid(tokens)): True
    elif((tokens[0] == "push" or tokens[0] == "save" or tokens[0] == "get") and tokens[1].lstrip('-').isdigit()): True
    else:
        raise ValueError("Parse error: " + tokens[0])
    return tokens

def isValid(validate):
    return ((validate[0] == "pop" or validate[0] == "add" or validate[0] == "sub" or
             validate[0] == "mul" or validate[0] == "div" or validate[0] == "mod" or 
             validate[0] == "skip") and (len(validate) == 1))
