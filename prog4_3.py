import sys
from prog4_1 import Tokenize
from prog4_1 import Parse

def main():
    list = []
    with open(sys.argv[1]) as f:
        for line in f:
            valid_tokens = Tokenize(line)
            list.append(valid_tokens)
    for tokens in list: 
        Parse(tokens)

if __name__ == '__main__':
    main()
