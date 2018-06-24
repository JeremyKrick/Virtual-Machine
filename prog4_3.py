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
    f.close
    #print(validTokens)
    for tokens in validTokens: 
        Parse(tokens)
        print(Parse(tokens))
    #print("Number of lines: ", len(validTokens))

    sm = StackMachine() # Instantiate StackMachine class
    #sm.Execute(validTokens)
    #print("CurrentLine: ", sm.CurrentLine)
    for line, i in enumerate(validTokens):
        try:
            temp = sm.Execute(validTokens[line])
            if(temp != None):
                print(temp)
                #print("CurrentLine: ", sm.CurrentLine)
            #if(sm.CurrentLine < 0): 
                #print("Trying to execute invalid line:",sm.CurrentLine)
                #sys.exit(0)
            #print(sm.Execute(validTokens[line]))
                
        except IndexError:
            print("Line",sm.CurrentLine+1,": ",validTokens[line],"caused Invalid Memory Access.")
    print("Program terminated correctly")
        #print("CurrentLine: ", sm.CurrentLine)

if __name__ == '__main__':
    main()
