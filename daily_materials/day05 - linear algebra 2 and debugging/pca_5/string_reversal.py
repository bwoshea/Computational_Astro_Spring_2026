'''
Simple (broken) program to reverse a string.  Look for 'BUG' to find the bug.

Takes in a string of arbitrary (but assumed to be non-zero) length; returns a 
string of the same length, but reversed.
'''

def reverse_string(mystring):
    '''
    Reverses the ordering of characters in a string using a simple loop.
    Input: a string.
    Output: a completely reversed version of that string, including all characters.
    '''
    
    reversed_string = ""

    if len(mystring)==0:
        return []

    '''
    Put a pdb breakpoint here and then step through the loop, printing out i,
    mystring[i], and reversed_string at each step - do you see where the loop
    breaks?
    '''
    
    # BUG: the 0 in the range() method should be -1, given how range() works!
    for i in range(len(mystring)-1,0,-1):  
        
        reversed_string += mystring[i]

    '''
    put a breakpoint here to see what the function is returning, as well as
    the final value of i.  Change range() and then re-run the code to
    see how these variables change!
    '''
    
    return reversed_string

mystring = "Go green!"

print("\noriginal string:    ",mystring,"\n")

reversed = reverse_string(mystring)

print("reversed string:    ",reversed,"\n")
