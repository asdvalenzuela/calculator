"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

#from sys import argv
"""I know this is bad practice but I'm it doing it anyway
because we're using all the functions in the file and no other
libraries
"""
from arithmetic import *

def is_input_valid(operation):
    

    #what if people put random spaces or commas?
    #this is to split it according to spaces or commas.
    #if there are no spaces/commas, it's not valid
    if operation == "q" or operation == "quit":
        return True

    operation_as_list = split_operation(operation) #returns empty list if not possible

    if operation_as_list == []:
        print "Please separate arguments with commas or spaces."
        return False

    #check whether list has only 2 or 3 characters
    if not (len(operation_as_list) == 2 or len(operation_as_list) == 3):
        print "Please enter one operator and one or two operands."
        return False
    
    #make sure the first character is an operator
    operators_oneoperand = ["square", "cube"]
    operators_twooperands = ["+", "add", "-", "plus", "subtract", "minus", "modulo", "%", "mod",
            "/", "divide", "*", "multiply", "power", "times", "pow"]
    if (operation_as_list[0] not in operators_twooperands) and (operation_as_list[0] not in operators_oneoperand):    
        print "Please enter a valid operator."
        return False

    #make sure the last 1 (or two) are operands
    if not operation_as_list[1].isdigit():
        print "Please enter valid operands."
        return False

    if operation_as_list[0] in operators_twooperands:
        if len(operation_as_list) != 3:
            print "Please enter two operands."
            return False
        if not operation_as_list[2].isdigit():
            print "Please enter valid operands."
            return False

    #otherwise continue to split the operation with commas or spaces        
    return True


def split_operation(operation):
    operation_as_list = []
    if " " in operation:
        operation_as_list = operation.split(" ")  
    elif "," in operation:
        operation_as_list = operation.split(",")
    return operation_as_list
    

def main(): 
    continue_playing = True
    while continue_playing:

        #get user's input for the first time
        operation = raw_input("Please enter an operation in prefix notation: ")

        #as long as it's not valid input, keep prompting the user
        while is_input_valid(operation) == False:
            operation = raw_input("Please enter an operation in prefix notation: ")

        if operation == "q" or operation == "quit":
            continue_playing = False
        else:
            #if the input is valid, we know we can successfully split it
            #with either spaces or commas
            operation_as_list = split_operation(operation)

            operator = operation_as_list[0]
            operand1 = operation_as_list[1]

            #if the function requires 2 operands, assign the second one
            if len(operation_as_list) == 3:
                operand2 = operation_as_list[2]

            if operator == "+" or operator == "add":
                print add(int(operand1), int(operand2))
            if operator == "-" or operator == "subtract":
                print subtract(int(operand1), int(operand2))
            if operator == "*" or operator == "multiply":
                print multiply(int(operand1), int(operand2))
            if operator == "/" or operator == "divide":
                print divide(int(operand1), int(operand2))
            if operator == "%" or operator == "mod" or operator == "modulo":
                print mod(int(operand1), int(operand2))
            if operator == "square":
                print square(int(operand1))
            if operator == "cube":
                print cube(int(operand1))
            if operator == "power" or operator == "pow":
                print power(int(operand1), int(operand2))
        

if __name__ == '__main__':
    main()
