"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

"""I know this is bad practice but I'm it doing it anyway
because we're using all the functions in the file and no other
libraries
"""
from arithmetic import *

def is_input_valid(operation):

    operation_as_list = split_operation(operation) #returns empty list if not possible

    if operation_as_list == []:
        print "Please separate arguments with commas or spaces."
        return False

    #check whether list has only 2 or 3 characters
    if len(operation_as_list) <= 1:
        print "Please enter one operator and one or two operands."
        return False
    
    #make sure the first character is an operator
    operators_oneoperand = ["square", "cube"]
    operators_twooperands = ["+", "add", "-", "plus", "subtract", "minus", "modulo", "%", "mod",
            "/", "divide", "*", "multiply", "power", "times", "pow", "**"]
    if ((operation_as_list[0] not in operators_twooperands) and 
        (operation_as_list[0] not in operators_oneoperand)):    
        print "Please enter a valid operator."
        return False

     #make sure the last 1 (or two) are operands
     #THIS DOES NOT WORK YET
    for i in operation_as_list:
        if not operation_as_list[i].isdigit():
            print "Please enter valid operands."
            return False

    if operation_as_list[0] in operators_twooperands:
        if len(operation_as_list) <= 2:
            print "Please enter two operands."
            return False

    #otherwise continue to split the operation with commas or spaces        
    return operation_as_list


def split_operation(operation):
    operation_as_list = []
    if " " in operation:
        operation_as_list = operation.split(" ")  
    elif "," in operation:
        operation_as_list = operation.split(",")
    return operation_as_list

def main(): 
    while True:

        #get user's input for the first time
        operation = raw_input("Please enter an operation in prefix notation: ")

        if operation == "q" or operation == "quit":
            break

        operation_as_list = is_input_valid(operation) #the list if true, otherwise false
        if operation_as_list == False:
            continue
        
        #if the input is valid, we know we can successfully split it
        #with either spaces or commas
        operator = operation_as_list[0]
        for i in operation_as_list:
            i = int(i)

        if operator in ["+", "add", "plus"]:
            print reduce(add, operation_as_list[1:])
        if operator in ["-", "subtract", "minus"]:
            print reduce(subtract, operation_as_list[1:])
        if operator in ["*", "multiply", "times"]:
            print reduce(multiply, operation_as_list[1:])
        if operator in ["/", "divide"]:
            print reduce(divide, operation_as_list[1:])
        if operator in ["%", "modulo", "mod"]:
            print reduce(mod, operation_as_list[1:])
        if operator == "square":
            print square(operation_as_list[1])
        if operator == "cube":
            print cube(operation_as_list[1])
        if operator in ["power", "pow", "**"]:
            print reduce(power, operation_as_list[1:])
    

if __name__ == '__main__':
    main()
