import pdb

def reverse_string(mystring):
    '''
    Simple (buggy) program to reverse a string.
    '''
    
    reversed_string = ""

    if len(mystring)==0:
        return []

    pdb.set_trace()
    
    # BUG: the 0 should be -1, given how range() works!
    for i in range(len(mystring)-1,0,-1):  
        
        # use debugger to print out i, mystring[i], and
        # reverse_string right here to see what's going on!
        reversed_string += mystring[i]

    pdb.set_trace()

    return reversed_string

mystring = "lions and tigers and bears, oh my!"

mystr = reverse_string(mystring)

print(mystr)
