# A password generator. Takes input from users (some word). Uses these words to generate a password.
# By using these words, retrieves previously generated password if any.
# Two types password generated each time -
#     1. Medium (number and alphabet)
#     2. Very strong (special character, number and alphabet)
# Saves these info into a file and retrieve those from that file

# Standard Library modules
import random as rd


def insert_num_in_pass(pass_string, num_of_nums):
    """Inset random numbers at random indices

        INPUT:
            pass_string --> string. To insert numbers in (password string)
            num_of_nums --> int. Number of how many numbers to be inserted in pass_string

        OUTPUT: string. The string with numbers inserted into it
    """
    password = pass_string
    # Insert num_of_nums numbers
    for i in range(num_of_nums):
        # Select a random int for the index. Must exist in the string, so use len()
        index = rd.choice(list(range(len(password))))
        # Insert a random one-digit number at a random index
        password = password[:index] + \
            str(rd.choice(list(range(10)))) + password[index:]
    return password


def insert_symbols_in_pass(pass_string, num_of_symbols):
    """Insert random symbols at random indices

        INPUT:
            pass_string --> string. To insert symbols in (password string)
            num_of_symbols --> int. Number of how many symbols to be inserted in pass_string

        OUTPUT: string. The string with symbols inserted into it
    """
    password = pass_string
    symbols = []

    # Read data from the symbol's txt file
    with open("symbols.txt") as f:
        # In each line there is symbol
        for line in f:
            symbol = line.strip()
            # Add the symbol to the symbols list
            symbols.append(symbol)

    # Insert num_of_nums symbols
    for i in range(num_of_symbols):
        # Select a random int for the index. Must exist in the string, so use len()
        index = rd.choice(list(range(len(password))))
        # Insert a random symbol from the symbols list at a random index
        password = password[:index] + \
            str(rd.choice(symbols)) + password[index:]
    return password


def gen_and_save_pass(words):
    """Read data from the file 'password_and_words.txt'.
        If the words the user has given are already saved in the file:
            return the passwords that corresponds with the words in the file.

        Else:
            generate two password (one with letters and numbers and another with letters, numbers and symbols),
            save them in the file 'password_and_words.txt' and return them.

        INPUT: list - words to be used to generate the passwords
        OUTPUT: tuple - if found, previous passwords generated for the words given, else newly generated passwords
    """
    # Read the 'password_and_words.txt' file
    with open("password_and_words.txt") as f:
        for line in f:
            # Words given previously
            user_words = line.split(": ")[0]
            # String to list of words
            word_list = user_words.split(" ")
            # If the list matches
            if word_list == words:
                # Read the passwords generated previously
                passwords = line.split(": ")[1].strip().split(" , ")
                return (passwords[0], passwords[1])

    # Shuffle the words given getting rid of any blank spaces in them
    shuffled_words = ''.join(rd.sample(words, len(words))).replace(" ", "")
    # Generate a medium password
    medium_password = insert_num_in_pass(shuffled_words, 4)
    # Generate a strong password
    strong_password = insert_symbols_in_pass(medium_password, 2)
    # Save the password in the file 'password_and_words.txt'
    save_pass(words, medium_password, strong_password)
    return (medium_password, strong_password)


def ask_user_words():
    """Ask users to input the number of words they want to input consequently.
        According to the number, take word input from the user.
        Append all the numbers the user inputs to a list on by one.

        INPUT: None
        OUTPUT: List - containing the words user inputted
    """
    # Ask the user for a number until they input one
    while True:
        try:
            word_num = int(input("How many words do you want for your pass? "))
            break
        except ValueError:
            # If user inputs any value other than a number
            print("Oops! Please tell me a number")

    # Initial array which will contain all the words the user inputs
    words = []
    for i in range(word_num):
        word = input("Enter your {} {} word: ".format("no", i + 1))
        words.append(word)
    return words


def save_pass(words, medium_password, strong_password):
    """Save passwords along with the words used to generate the passwords to the password_and_words.txt

        INPUT:
            words --> list. Words the user has inputted and have been used to generated the passwords
            medium_password --> string. A password generated randomly from the words the user has inputted and with
                                        random numbers at random indices
            strong_password -->

        OUTPUT: string. The string with symbols inserted into it
    """
    words_string = ""
    for word in words:
        # Add words to the words_string getting rid of blank spaces in the word
        words_string = words_string + word + " "
    with open("password_and_words.txt", "a") as f:
        # Write the words_string in the file getting rid of the last blank_space, add a colon and
        # after that add the two passwords seperated by " , " and then end the line
        f.write(words_string.strip() + ": " +
                medium_password + " , " + strong_password + "\n")


def main():
    """The main function of the program. Run automatically if the main file is run.
        Don't run if is imported in other files.
    """
    # Will ask the user for words to make two passwords
    words = ask_user_words()

    # Two passwords generated using the user's words
    #     1. Medium pass (numbers and letters)
    #     2. Very strong pass (special characters, numbers and letters)
    medium_password, strong_password = gen_and_save_pass(words)
    print("Your medium password is", medium_password)
    print("Your strong password is", strong_password)


if __name__ == "__main__":
    main()
