import sys
from prog4_1 import Tokenize
from prog4_1 import Parse
from prog4_2 import StackMachine

def main():
    validTokens = []
    print("Assignment #4-3, Jeremy Krick, jkrick@sdsu.edu")
    with open(sys.argv[1]) as f:
        for line in f:
            validTokens.append(Tokenize(line))
    for tokens in validTokens: 
        Parse(tokens)
    sm = StackMachine()
    while(sm.CurrentLine < len(validTokens)):
        try:
            temp = sm.Execute(validTokens[sm.CurrentLine])
            if(temp != None):
                print(temp)
            if(sm.CurrentLine < 0): 
                print("Trying to execute invalid line:",sm.CurrentLine)
                sys.exit(0)       
        except IndexError:
            print("Line",sm.CurrentLine,": ",validTokens[sm.CurrentLine],"caused Invalid Memory Access.")
    print("Program terminated correctly")

if __name__ == '__main__':
    main()
