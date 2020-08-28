def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - Run HDL Driver")
        print("2 - Run LDL Driver")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()

def HDL_driver():
    # Create get input function
    HDLInput = inputHDL()

    # Check if HDL is normal
    calculatedHDL = HDLChecker(HDLInput)

    # Output
    outputHDL(calculatedHDL)

def LDL_driver():
    # Create get input function
    LDLInput = inputLDL()

    # Check if HDL is normal
    calculatedLDL = LDLChecker(LDLInput)

    # Output
    outputLDL(calculatedLDL)

def inputHDL():
    myInput = input('Enter your HDL: ')
    return int(myInput)

def HDLChecker(input):
    if input >= 60:
        output = "Normal"
    elif input < 40:
        output = "Low"
    else:
        output = "Borderline Low"
    return output

def outputHDL(HDL):
    print("Your HDL level is {}".format(HDL))

def inputLDL():
    myInput = input('Enter your LDL: ')
    return int(myInput)

def LDLChecker(input):
    if input > 130:
        output = "Normal"
    elif 130 <= input <= 159:
        output = "Borderline High"
    elif 160 <= input <=189:
        output = "High"
    else:
        output = "Very High"
    return output

def outputLDL(LDL):
    print("Your LDL level is {}".format(LDL))

interface()