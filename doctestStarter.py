import os
import platform

# Write code to get your OS name
# Read about how to use the platform module # to achieve this.
#Julia Jablonski
def getOSName():
    '''
    >>> name = getOSName()
    >>> name in {'Linux', 'Windows', 'Darwin'}
    True
    '''
    return platform.system()
    

# Write code to find the function name
# given a function call. 
#Kareem
def findFunc(block):
    '''
    >>> findFunc('  rectangle(50,100)')
    'rectangle'
    >>> findFunc('add(50,100)')
    'add'
    >>> findFunc('      onlyTwo(5,10,13)')
    'onlyTwo'
    '''
    argIndex = block.find("(")
    return block[:argIndex].strip()




# Write filterErrors, which takes a 
# list of strings as an input and 
# outputs a list containing only
# the strings that DONT have the 
# substring 'ok' in them. 

#Josh Famous
def filterErrors(strList):
    '''
    >>> S = ['hello', 'error in module 5', 'test ok', 'everying ok']
    >>> filterErrors(S)
    ['hello', 'error in module 5']
    '''
    newList = []
    for item in strList:
        if item.find("ok") == -1:
            newList.append(item)
    return newList


# This function is a crucial part of parsing the 
# block of text from each doctest. 
# It takes in a string that represents 
# ONE test that failed.
#Kareem Mi

def findError(block):
    # split the block by '\n', generating. a list of lines
    block = block.split("\n")

    # strip the white space from each line of text in the list
    for line in block:
        line = line.strip()

    # Look for the line that contains 'Error:' in the list of lines.
    errorline = [index(line) for line in block if "Error" in line]
    pointer = errorline[0] - 2

    # Then, parse the line number that the error occurred on (this will be 
    # two lines before the line where 'Error:' occurs) You will have to split this
    # line by a comma and then strip the white space to revtrieve the actual line number.
    lnlst = block[pointer].split()
    line_number = lnlst[2].rstrip(",")
    
    # In addition, you should parse the line of code that caused the error and the 
    # type of error itself, which will be the next two lines after the line number line.
    pointer += 1
    code = block[pointer]

    error_type = block[errorline]

    # If you are confused, debug your code and print out what each block looks like to 
    # get a better idea of what's happening. 
    # You should return a 3-tuple in the form of: 
    #      (line number, code, error_type)

    tup = (line_number, code, error_type)
    return tup

# Write the function to run the doctest in 
# the terminal. You should output the results
# of the doctest to a text file, which is what
# the docFilename variable represents. 
# This function does not need any outputs. 
# Make use of the OS module. 

# Josh Famous
def runDoctest(pyfile, docFilename):
    # IMPORTANT: you should write the command-line command
    # in accordance to the operating system you're using. 
    # Use the getOSName() function in here. 
    # You will either use python or python3 based on your OS.
    command = "" 
    # Write command line command based on OS
    if(getOSName() == 'Windows'):
        command = "python -m doctest -v " + pyfile + " > " + docFilename
    else:
        command = "python3 -m doctest -v " + pyfile + " > " + docFilename

    # Run command
    os.system(command)


# Write the function to get the output of the doctest
# Essentially, you have to read the text file that
# contains the result of the doctest. 

#Julia Jablonski

def getDoctestOutput(docFilename):
    # Read in the doctest output from the file
    txt = open(docFilename,"r")
    txtinfo = txt.read()
    
    # Split your full doctest string by the string 'Trying:'
    splat = txtinfo.split("Trying:")
    tupleforend=[]

    # Initialize a new list, and
    # for each error in the error list, 
    # append a 4-tuple in the form of: 
    # (function, line number, code, error_type)

    # Filter the errors, store in new list
    errorlist = filterErrors(splat)

    for x in errorlist:
        tupleforend.append((findFunc(x),) + findError(x))

    # Return that list of tuples

    return tupleforend

# Write a main function that puts together all of your code.
# In this function, you should prompt for a Python file name to
# doctest and then choose a file name to store the output in.
# Then, you should run the doctest then retrieve the errors. 
# If no error was found, return 'No errors found.' Otherwise, 
# for each error, format an output to present the errors that occured
# and their associated function / line numbers / code / type.

#Julia Jablonski and Kareem 
def main():

    filename= input("please enter a file name(add .py)")
    outputloc= input("where should we put the outputs?(add .txt)") 
    runDoctest(filename,outputloc)
    finaltup= getDoctestOutput(outputloc)
    final=''
    if not finaltup:
        return "no errors found"
    else:
        for x in finaltup:
            final=final+str(x[0])+' / '+str(x[1]+' / '+str(x[2])+' / '+ str(x[3]) + '/n')

    return final 

# Uncomment the code below to make your program run.

print(main())