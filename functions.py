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

if __name__ == "__main__":
    main()

parameter = input("Enter the parameter you want to double up. ")

def doubler(parameter):
    doubledparameter = str(parameter) + str(parameter)
    print(doubledparameter)

doubler(parameter)

def this_year():
    print(int(45 * 45) + (24 * 24) - (26 * 26) + 93)

this_year()

def base_conversion():
    base = input("Enter your destination base (0-9) ")
    maximumnumber = (base - 1) + ((base * 2) - 1) + ((base * 3) - 1) + ((base * 4) - 1)
    print("Your maximum 4-digit number in this base is", maximumnumber)