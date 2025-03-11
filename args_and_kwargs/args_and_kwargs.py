# ARGS AND KWARGS (Variable Length Argument)
# video link https://www.youtube.com/watch?v=QSIAVAwQueE


# *args -> arguments    and  **kwargs -> keyword arguments
# Definition : ARGS => If you want to pass multiple or unlimited arguments to a funcion so just simply pass *args into function's parameter. Args has a type of tuple . you have to add single asterick(*) in the beginning and you can change "args" name put it as per ur choice but * is mandatory 
# exapmle : def name(*args):
            #    print(args)
            # name(2,3,4,5,8,20,36)  multiple arguments u can pass


# Definition : KARGS => If you want to pass multiple or unlimited keyword arguments to a function so just simply pass **kargs into function's parameter. Kargs has a type of dictionary (key value pairs) . you have to add double asterick(**) in the beginning and you can change "kargs" name put it as per ur choice but ** are mandatory            
#  exapmle : def name(**kargs):
            #    print(args)
            # name(id="achj0" , phone="1343653135" , education="fsdkfksjf" , address="snfksjd") multiple keyword arguments u can pass



# example of args
def name(*args):
    print(args)
    print(args)
    # you can loop on every value to multiply them 
    multiply = 0
    for i in args :
        multiply = i*2
    print(multiply)
            
            
name(2,3,4,5,8,20,36) 

# iteration of given arguments 
# First Iteration (i = 2):
# multiply = 2 * 2 ➔ multiply = 4
# Second Iteration (i = 3):
# multiply = 3 * 2 ➔ multiply = 6
# Third Iteration (i = 4):
# multiply = 4 * 2 ➔ multiply = 8
# Fourth Iteration (i = 5):
# multiply = 5 * 2 ➔ multiply = 10
# Fifth Iteration (i = 8):
# multiply = 8 * 2 ➔ multiply = 16
# Sixth Iteration (i = 20):
# multiply = 20 * 2 ➔ multiply = 40
# Seventh Iteration (i = 36):
# multiply = 36 * 2 ➔ multiply = 72


def name(**kwargs):
    print(kwargs)
    
    # you can loop on every value to multiply them 
    # multiply = 0
    for  key,value in kwargs.items():
       print(key,value)
            
            
#  you can pass multiple keyword arguments 
name(name= "sidra" , age= "2" , location = "karachi") 