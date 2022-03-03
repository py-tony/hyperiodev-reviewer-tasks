#to run this program you just need python install on your system. it also possible to run on a phone no extra installations or dependencies is needed.


#this is the begibing of this program find details on how the program(functionworks) down below

print(""" Welcome to the ISBN 13 AND 10 VALIDATOR
≈==≈====================================

FEEL FREE TO INPUT YOUR OWN DIGIT OR SELECT ONE FROM THE MENU

enter 1 to test: "0330301624"
enter 2 to test: "0316066524"
enter 3 to test: "0330301824"
enter 4 to test: "9780316066525X"
enter 5 to test: "033522249u"

or enter your own digits directly.
""")

isbn = input("here: ")

if isbn == "1":
    isbn = "0330301624"
elif isbn == "2":
    isbn = "0316066524"
elif isbn == "3":
    isbn = "0330301824"
elif isbn == "4":
    isbn = "9780316066525X"
elif isbn == "4":
    isbn = "033522249u"
elif isbn == "5":
  isbn = "033522249u"
else:
    print("Ok, Guess we're trying your own digts, which is: ",isbn )
    


def isbn13tst(isbn):
    """this function takes takes a string of numbers (possibly with an X at the end) 
    and checks it if its valid according to the International Standard Book Number
    
    Examples

isbn13("9780316066525") ➞ "Valid" isbn13("0330301824") ➞ "Invalid" isbn13("0316066524") ➞ "9780316066525"
    """
    
    
    #check if the number is a potential valid isbn but has an "X" at the end 
    
    if len(isbn) == 11 or len(isbn) == 14 :
        if isbn.endswith("X"):
            isbn = isbn[:-1]
        else:
            return "Invalid"
         
   #start by checking is a 13 digit 
   
    if len(isbn) == 13:
        
        #if so we proceed to create the test number and the algorithm
        test = "13"
        sum = 0
        
        
        #here we're looping through each digit and multiply it by 1 or 3 and adding the result to the sum var
        for i in isbn:
            sum += int(i) * int(test[0])
            #this checks if the previous digit was multuply by 1. if so we replace the test var with 3 else we reset it to 13
            test = test[1] if len(test) == 2 else "13"
        
        #checking if the sum of all the products is disable by 10 or not and stop the function
        return "Invalid" if sum%10 else "Valid"
        
    #if the isbn is a 10 digit num we repeat  what we did above
    elif len(isbn) == 10:
        
        test = 10
        sum = 0
        
        for i in isbn:
            sum += int(i) * test
            test -= 1
            
        #here we re checking if its not disable by 11 then its not a valid isbn
        if sum % 11:
            return "Invalid"
            
        #if its a valid isbn we need to convert to a valid 13 isbn
        
        # we do by doing a mixture of validation and recursion
        
        #since there was no specific instructions on how to change the last digit 
        #we're just gonna be adding one or substracting one to the last digit till we get a valid 13 isbn
        else:
            
            n = 10
            for i in range(n):
                if i + int(isbn[-1]) < 9:
                    isbn2 = "978"+isbn[:-1] + str(i + int(isbn[-1]))
                else:
                    isbn2 = "978"+isbn[:-1] + str(int(isbn[-1]) - 1)
                
                if isbn13tst(isbn2) == "Valid":
                    return isbn2
             
             
            
    else:
        return "Invalid"
        
        
print(isbn13tst(isbn))






"""

I'm not to concern about the space, if we think about the type of inputs that we're 
expecring we assume to be 4 to 8byte... I think i have created too much variables, looping, 
and the recursion that might make my program needing more space depending on the input, but its still a O(n) algorithm. 

"""