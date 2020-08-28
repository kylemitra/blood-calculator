def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - Check HDL")
        print("2 - Check LDL")
        print("3 - Check Cholesterol")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
        elif choice == '3':
            cholesterol_driver()

def HDL_driver():
    HDLInput = inputFunc('HDL')
    calculatedHDL = HDLChecker(HDLInput)
    outputFunc('HDL', calculatedHDL)

def LDL_driver():
    LDLInput = inputFunc('LDL')
    calculatedLDL = LDLChecker(LDLInput)
    outputFunc('LDL', calculatedLDL)

def cholesterol_driver():
    cInput = inputFunc('Cholesterol')
    calculatedChol = cholesterolChecker(cInput)
    outputFunc('Cholesterol', calculatedChol)

def inputFunc(type):
    myInput = input('Enter your {}: '.format(type))
    return int(myInput)

def HDLChecker(input):
    if input >= 60:
        output = "Normal"
    elif input < 40:
        output = "Low"
    else:
        output = "Borderline Low"
    return output

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

def cholesterolChecker(input):
    if input < 200:
        output = "Normal"
    elif 200 <= input <= 239:
        output = "Borderline High"
    else:
        output = "Very High"
    return output

def outputFunc(type, value):
    print("Your {} level is {}".format(type, value))

interface()