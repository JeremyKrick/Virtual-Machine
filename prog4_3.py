import sys
from prog4_1 import Tokenize
from prog4_1 import Parse

def main():
    validTokens = []
    with open(sys.argv[1]) as f:
        for line in f:
            validTokens.append(Tokenize(line))
    for tokens in validTokens: 
        Parse(tokens)
        #print(Parse(tokens))
        

if __name__ == '__main__':
    main()
