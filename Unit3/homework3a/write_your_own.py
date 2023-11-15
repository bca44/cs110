true_response = ['Y', 'y', 'Yes', 'yes']


def get_name():
    # gets and returns name from user

    name = input("What is your first and last name? Ex. Mary Johnson ")
    return name


def get_number():
    # gets and returns number from user

    number = input("What is your phone number? ")

    # determines if number is primary or no, stores in Boolean primary_number
    if input("Is this your primary number? ") in true_response:
        primary_number = True
    else:
        primary_number = False

    return number, primary_number


def summary_and_confirm(name, number, primary_number):
    # determines if number is primary number or not

    if primary_number:
        print(f"Just to confirm, your name is {name} and your primary number is {number}.")
    else:
        print(f"Just to confirm, your name is {name} and your phone number is {number}.")

    # returns True if info correct. Else, False

    if input("Is that correct? ") in true_response:
        print("Excellent. Fetching your account information now. ")
        print("...")
        return True
    else:
        print("Ok. Let's try again. ")
        return False


def customer_info():
    while True:

        print("Welcome to Bulwark Exterminating!")
        print("We are happy to help you today. We will collect some information to verify your account.")

        name = get_name()

        number, primary_number = get_number()

        if summary_and_confirm(name, number, primary_number):
            # summary_and_confirm returns True if customer confirms info is correct
            break


if __name__ == "__main__":
    customer_info()
