def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - Run HDL Driver")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    # Create get input function
    HDLInput = input()

    # Check if HDL is normal
    calculatedHDL = HDLChecker(HDLInput)

    # Output
    outputDisplay(calculatedHDL)


def input():
    myInput = input('Enter your HDL: ')
    return myInput

def HDLChecker(input):
    if input >= 60:
        output = "Normal"
    elif input < 40:
        output = "Low"
    else:
        output = "Borderline Low"
    return output

def outputDisplay(HDL):
    print("Your HDL level is {}".format(HDL))

interface()