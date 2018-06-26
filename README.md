Files: prog4_1.py prog4_2.py prog4_3.py

prog4_1.py
  Two functions:
  
    Tokenize(str) - Takes a string and splits by whitespace and then tokenizes by a list of allowed words
  
    Parse(tokens) - Takes a list of tolkens that has already passed through the Tokenize() and validates they are of the accepted syntax.
    
prog4_2.py

    class StackMachine - Takes a list of tolkens that has been Tokenized and Parsed. It then takes instructions via the tolkens and pushes/pops from the stack
    as appropriate. It also allows for saving values into a dictionary named "saved" Thereby, creating a virtual machine.
  
prog4_3.py

    main() - This driver class opens a file passed as a cmd line arg, validates it using the Tokenize/Parse methods and then instantiates a StackMachine.
    It then executes the instructions from the file and notifies the user if the program terminated correctly.