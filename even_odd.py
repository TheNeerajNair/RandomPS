def even_or_odd(num):
    print('**** ODD-EVEN CHECK INITIATED ****')
    if num % 2 == 0:
        print('INPUT RECIEVED  ->  {}'.format(num))
        return 0
    elif num % 2 == 1:
        print('INPUT RECIEVED  ->  {}'.format(num))
        return 1
    elif (num == 0 ) or ( num < 0 ):
        print('Invalid Number, Rerun Again!')
        Processor(a)

def Processor(a):
    print('    Welcome to my Program that checks if a user\'s input is Odd or Even!     ')
    num = input(str(' USER INPUT REQUIRED: Please ENTER an INPUT -->  '))

    print('**** INPUT VALIDITY Check System STARTS ****')
    if num.isdigit() == True:
        print('Input Validity Check Passed - Processing Further')
        decision_code = even_or_odd(int(num))
        if decision_code == 0:
            print( ('RESULT = ' ) + a + ( ' has selected an EVEN number!' ))
            
        else:
            print( ('RESULT = ' ) + a + ( ' has selected an ODD number!' ))
            
    else:
        print('INVALID INPUT DETECTED!!! , Aborting current instance and Restarting Program')
        Processor(a)

a = input(str("Please Enter Your Name!  -->    "))
Processor(a)
