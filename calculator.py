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
            "/", "divide", "*", "multiply", "power", "times", "pow", "**"]
    if ((operation_as_list[0] not in operators_twooperands) and 
        (operation_as_list[0] not in operators_oneoperand)):    
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
    return operation_as_list


def split_operation(operation):
    operation_as_list = []
    if " " in operation:
        operation_as_list = operation.split(" ")  
    elif "," in operation:
        operation_as_list = operation.split(",")
    return operation_as_list
    



#while True:
#    oper = raw_inptut()
#    if op == "q":
#        break
#    if not valid:
#        print "duh"
#        continue

#    ... do stuff



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
        operand1 = int(operation_as_list[1])

        #if the function requires 2 operands, assign the second one
        if len(operation_as_list) == 3:
            operand2 = int(operation_as_list[2])

        if operator in ["+", "add", "plus"]:
            print add(operand1,operand2)
        if operator in ["-", "subtract", "minus"]:
            print subtract(operand1,operand2)
        if operator in ["*", "multiply", "times"]:
            print multiply(operand1,operand2)
        if operator in ["/", "divide"]:
            print divide(operand1,operand2)
        if operator in ["%", "modulo", "mod"]:
            print mod(operand1,operand2)
        if operator == "square":
            print square(operand1)
        if operator == "cube":
            print cube(operand1)
        if operator in ["power", "pow", "**"]:
            print power(operand1,operand2)
    

if __name__ == '__main__':
    main()
