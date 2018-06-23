import sys
from prog4_1 import Tokenize

def main():
    with open(sys.argv[1]) as f:
        data = f.readlines()
    my_object = Tokenize(data)

if __name__ == '__main__':
    main()
