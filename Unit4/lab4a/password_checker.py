def character_count(a_string):
    # checks character count of string, returns True if >= 8

    count = 0
    for character in a_string:
        count += 1

    if count >= 8:
        return True

    return False


def check_lowercase(a_string):
    # returns True if at least one lowercase character

    for character in a_string:
        if character.islower():
            return True

    return False


def check_uppercase(a_string):
    # returns True if at least one uppercase character

    for character in a_string:
        if character.isupper():
            return True

    return False


def check_number(a_string):
    # returns True if at least one number

    for character in a_string:
        if character.isdigit():
            return True

    return False


def check_password(password):
    # returns 'error' statement for condition not met
    # if all met, returns 'password accepted'

    if not character_count(password):
        return "Password must have at least 8 characters."

    elif not check_lowercase(password):
        return "Password must contain at least 1 lowercase letter"

    elif not check_uppercase(password):
        return "Password must contain at least 1 uppercase letter"

    elif not check_number(password):
        return "Password must contain at least 1 number."

    else:
        return "Password accepted."


def main():
    print(check_password('password'))
    print(check_password('a87fRPesT'))
    print(check_password('a8P'))
    print(check_password('abFHaprucndPE8'))
    print(check_password('arPReSH!!$@'))
    print(check_password('Password1'))




if __name__ == '__main__':
    main()
