import sys
from prog4_1 import Tokenize
from prog4_1 import Parse
from prog4_2 import StackMachine

def main():
    validTokens = []
    with open(sys.argv[1]) as f:
        for line in f:
            validTokens.append(Tokenize(line))
    f.close
    #print(validTokens)
    for tokens in validTokens: 
        Parse(tokens)
        #print(Parse(tokens))
    sm1 = StackMachine(validTokens)
    #sm1.Execute()

if __name__ == '__main__':
    main()
