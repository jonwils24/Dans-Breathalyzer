#!/usr/bin/python


mainloop = 1

while mainloop == 1:


    
    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    #''' SET VARIABLES FROM USER INPUTS                                                                           '''
    # '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    

#"""----------------------------  w = weight (lbs) --------------------------------------------------"""

    
    wflag = 1

    while wflag == 1:

            w = input('\nhow much do you weigh in pounds?: ')

            if (w).isdigit():
                print("\n")
                w = float(w)
                wflag = 0
      

            else: 
                print("That is not a number!\n")
                wflag = 1


#"""---------------------------  d = drinks (qty)  --------------------------------------------------"""


    dflag = 1

    while dflag == 1:

            d = input('how many drinks have you had?: ')

            if (d).isdigit():
                print("\n")
                d = float(d)
                dflag = 0
      

            else: 
                print("That is not a number!\n")
                dflag = 1

                

#"""---------------------------  t = time (hrs)  ---------------------------------------------------"""
  

    tflag = 1

    while tflag == 1:

            t = input('how many hours have you been drinking?: ')

            if (t).isdigit():
                print("\n")
                t = float(t)
                tflag = 0
      

            else: 
                print("That is not a number!\n")
                tflag = 1






    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    #''' Metabolic rate = s             (f = mean 0.017,  0.014-0.021g/210L)    (m = mean 0.015, 0.013-0.017g/ml)'''
    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''


########     THIS IS WHERE WE NEED TO IMPLEMENT A LOOP THAT RELATES THE WEIGHT AND SEX OF A PERSON TO A VALUE OF S   #######
########     A HIGHER WEIGHT WOULD CORRESPOND TO A LARGER VALUE OF S   #########


#"""-------------------------------  sex = gender  ---------------------------------------------------"""
#"""--------------------------------  s = metabolic rate  --------------------------------------------"""

    flag = 1

    while flag == 1:

            sex = input('are you male or female?: ') 

            if sex == 'male':
                s = 0.015
                flag = 0

            elif sex == 'MALE': 
                s = 0.015
                flag = 0
       
            elif sex == 'Male': 
                s = 0.015
                flag = 0
       
            elif sex == 'm': 
                s = 0.015
                flag = 0
                
            elif sex == 'M': 
                s = 0.015
                flag = 0
       
            elif sex == 'female': 
                s = 0.017
                flag = 0

            elif sex == 'FEMALE': 
                s = 0.017
                flag = 0
       
            elif sex == 'Female': 
                s = 0.017
                flag = 0
        
            elif sex == 'f': 
                s = 0.017
                flag = 0
         
            elif sex == 'F': 
                s = 0.017
                flag = 0       

    else:
        flag = 1
        





    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    #''' DECLARE ALL CONSTANTS                                                                                    '''
    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    

    h2 = float(0.806)                #Body water in the blood  (80.6% average)
    
    ss = float(1.2)                  #Swedish standard constant








    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    #'''Body Water Constant  ****(DIFFERENT FOR MALES(0.58) AND FEMALES(0.49))***  '''
    #'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''



    bflag = 1

    while bflag == 1:

            if sex == 'male':
                body = float(0.58)
                bflag = 0

            elif sex == 'MALE': 
                body = float(0.58)
                bflag = 0
       
            elif sex == 'Male': 
                body = float(0.58)
                bflag = 0
       
            elif sex == 'm': 
                body = float(0.58)
                bflag = 0
                
            elif sex == 'M': 
                body = float(0.58)
                bflag = 0
       
            elif sex == 'female': 
                body = float(0.49)
                bflag = 0

            elif sex == 'FEMALE': 
                body = float(0.49)
                bflag = 0
       
            elif sex == 'Female': 
                body = float(0.49)
                bflag = 0
        
            elif sex == 'f': 
                body = float(0.49)
                bflag = 0
         
            elif sex == 'F': 
                body = float(0.49)
                bflag = 0 
      

    else:
        bflag = 1


              





#   '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
#   ''' THIS IS WHERE THE EQUATION FOR YOUR ESTIMATED BLOOD ALCOHOL CONTENT (BAC) IS CALCULATED                  '''
#   '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    
    EBAC = (((h2*d*ss)/(body*(w/(2.203))))-(s*t))


    if EBAC <= 0:
            EBAC = 0







#   '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
#    ''' PRINT THE RESULTS OF THE EQUATION TO THE SCREEN                                                          '''
#    '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
    

    print('\n\nYour BAC is:', EBAC, '%\n')







#    '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''
#    ''' ASK THE USER IF HE WANTS TO CONTINUE THE LOOP                                                            '''
#    '''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''



    p = input('\nType Quit to Exit or Press Enter to Continue\n\n')
    
    if p == 'Quit':
        mainloop = 0

    elif p == 'quit':
        mainloop = 0

    elif p == 'q':
        mainloop = 0
        
    elif p == 'Q':
        mainloop = 0

    else:
        mainloop = 1