"""DOCSTRING for Lab 02"""
#Wendell Yeung
#A01063806
#22 January 2019

def format_name(firstName, lastName):
    # fullname = str(firstName) + " " + str(lastName)
    # titledname = fullname.title()
    # finalname = titledname.strip()
    firstName = firstName.strip().capitalize()
    lastName = lastName.strip().capitalize()
    return (firstName + " " + lastName)

def main():
    first = input("Enter your first name")
    last = input("Enter your last name")
    result = format_name(first, last)
    print(result)

parameter = input("Enter the parameter you want to double up. ")

def doubler(parameter):
    doubledparameter = str(parameter) + str(parameter)
    print(doubledparameter)

doubler(parameter)

def this_year():
    print(int(45 * 45) + (24 * 24) - (26 * 26) + 93)

this_year()

def base_conversion():
    base = int(input("Enter your destination base (2-9):"))
    maximumnumber = (base * base * base * base) - 1
    print("Your maximum 4-digit number in this base is", maximumnumber)
    numbertoconvert = int(input("Enter a number equal to or lower than the maximum:"))
    stage1 = numbertoconvert % base
    stage1a = int(numbertoconvert / base)
    stage2 = stage1a % base
    stage2a = int(stage1a / base)
    stage3 = stage2a % base
    stage3a = int(stage2a / base)
    stage4 = stage3a % base
    convertedstring = str(stage4) + str(stage3) + str(stage2) + str(stage1)
    convertednumber = int(convertedstring)
    print("Your entered number converted to your entered base is", convertednumber)

base_conversion()

if __name__ == "__main__":
    main()
    base_conversion()