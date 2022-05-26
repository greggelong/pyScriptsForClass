
def turingMachine(tape):
    output = 0    ## it will return a 0 for odd, 1 for even
    halt = False    ## for start or stop
    state = "even"  # the starting state is even
    tapeIndex = 0   # index on tape to get current symbol
    print("The tape:", tape)

    while halt == False:    # not halted
        currentSymbol = tape[tapeIndex]

        ## rules
        if state == "even"  and currentSymbol ==1:
            print(f"The index is {tapeIndex}, the state is {state} the symbol is {currentSymbol}")
            print("I will change my state to odd and advance")
            state = "odd" 
            tapeIndex += 1
        elif state == "even" and currentSymbol == 0:
            print(f"The index is {tapeIndex}, the state is {state} the symbol is {currentSymbol}")
            print("I wll HALT and return a 1")
            halt = True
            output = 1
        elif state == "odd" and currentSymbol == 1:
            print(f"The index is {tapeIndex}, the state is {state} the symbol is {currentSymbol}")
            print("I will change my state to even and advance")
            state = "even" 
            tapeIndex += 1
        elif state == "odd" and currentSymbol == 0:
            print(f"The index is {tapeIndex}, the state is {state} the symbol is {currentSymbol}")
            print("I wll HALT and return a 0")
            halt = True
            output = 0
        
    return output




print("****Even Odd Turing Machine****")

tape1 = [1,1,0]
tape2 = [1,1,1,0]
tape3 = [1,1,1,1,0]

turingMachine(tape2)
#print(turingMachine(tape2))

## non turing way to tell if even or odd
'''
if tape2.count(1)%2 == 0:
    print("even")
else:
    print("odd")

    '''