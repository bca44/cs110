def found_word(response, words):
    """ Return True if one of the words is in the text. Return
    false otherwise.
    - text is a string
    - words is a list of strings
    """

    for word in words:
        if word in response:
            return True

    return False


def chat():
    """ Rules for the chatbot:
    - start with, "Hello! What did you do today?"
    - read input until "goodbye"
    - if input has 'good', 'great', 'fun', or 'amazing'
        - response is "Cool!"
    - if input has 'bad', 'rough', 'sad', or 'terrible'
        - response is "I'm so sorry, how can I help?"
    - otherwise
        - response is "Tell me more."
    """

    response = input("Hello! What did you do today? ")
    while response.lower() != "goodbye":

        if found_word(response, ["bad", "rough", "sad", "terrible"]):
            response = input("I'm so sorry, how can I help? ")

        elif found_word(response.lower(), ["good", "great", "fun", "amazing"]):
            response = input("Cool! ")

        else:
            response = input("Tell me more. ")


def main():
    chat()


if __name__ == '__main__':
    main()
