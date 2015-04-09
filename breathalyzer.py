#!/usr/bin/python

mainloop = 1

while mainloop == 1:

    # SET VARIABLES FROM USER INPUTS
    not_a_num = "That is not a number!\n"

    # w = weight (lbs)

    wflag = 1

    while wflag == 1:

        w = input('\nhowmuch do you weigh in pounds?: ')

        if (w).isdigit():
            print("\n")
            w = float(w)
            wflag = 0
        else:
            print(not_a_num)
            wflag = 1


    # d = drinks (qty)

    dflag = 1

    while dflag == 1:

        d = input('how many drinks have you had?: ')

        if (d).isdigit():
            print("\n")
            d = float(d)
            dflag = 0
        else:
            print(not_a_num)
            dflag = 1


    # t = time (hrs)

    tflag = 1

    while tflag == 1:

        t = input('how many hours have you been drinking?: ')

        if (t).isdigit():
            print("\n")
            t = float(t)
            tflag = 0
        else:
            print(not_a_num)


    ###
    # Metabolic rate = s    (f = mean 0.017, 0.014-0.021g/ml)    (m = mean 0.015, 0.013-0.017g/ml)
    ###
    # THIS IS WHERE WE NEED TO IMPLEMENT A LOOP THAT RELATES THE WEIGHT AND SEX OF A PERSON TO A VALUE OF S
    # A HIGHER WEIGHT WOULD CORRESPOND TO A LARGER VALUE OF S
    ###

    # sex = gender
    # s = metabolic rate
    # body = Body Water Constant *** Different for males(0.58) and females(0.49)

    flag = 1

    while flag == 1:

        sex = input('are you male or female?: ')

        if sex.lower() in ('male', 'm'):
            s = 0.015
            body = 0.58
            flag = 0
        elif sex.lower() in ('female', 'f'):
            s = 0.017
            body = 0.49
            flag = 0
        else:
            flag = 1


    # DECLARE ALL CONSTANTS

    h2 = float(0.806) # Body water in the blood (80.6% average)

    ss = float(1.2)   # Swedish standard constant


    # Equation for the estimated Blood Alcohol Content (BAC) is calculated

    EBAC = (((h2*d*ss)/(body*(w/(2.203))))-(s*t))

    if EBAC <= 0:
        EBAC = 0


    # Print the results of the equation to the screen

    print('\n\nYour BAC is:', EBAC, '%\n')


    # Ask the user if he wants to continue the loop

    p = input('\nType Quit to Exit or Press Enter to Continue\n\n')

    if p.lower() in ('quit', 'q'):
        mainloop = 0
    else:
        mainloop = 1




