def DivideByZero(x,y):
    ''' This Function is intended to return an Exception,if an integer has been tried to get divisible by Zero '''
    try:
        x/y
    except ZeroDivisionError as e:
        print("An interger/number can't be divisible by Zero")
        print("An execption has been occured as, ",e, " action has been attempted")



DivideByZero(5,0)