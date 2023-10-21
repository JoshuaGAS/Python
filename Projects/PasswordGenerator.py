import argparse
import random

class Cli:
    option = int(input("What kind of password do you want?\n1 for just alphanumeric\n2 with special characters\n3 for Uppercase letters\n4 for All Features\n-> "))
    print("You choose: ", option)
    pattern = input("how many characters the password need to have? ")

def main(): 
    try:
        new_pass = do_new_password(Cli.pattern)
        print(f"New Password Generated:\n{new_pass}")
    except ValueError as error:
        print(f"Error: {error}")

# def parse_args():
#     parser = argparse.ArgumentParser(description="Generate a new password")
#     parser.add_argument("pattern", help="Number of characters in the password (as a string)")
#     return parser.parse_args()

def do_new_password(pattern):
    user_input = int(pattern)
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "~`!@#$%^&*-_+=:|<,>.?/"
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    new_pass = ""
    count = 0

    if  Cli.option == 1:
        print("Just alphanumeric")
    elif Cli.option == 2:
        print("Special Characters")
        characters+=special
    elif Cli.option == 3:
        print("Uppercase Letters")
        characters+=uppercase
    elif Cli.option == 4:
        print("all features")
        characters+=special+uppercase
    else: print("invalid option")


    while count < user_input:
        random_char = random.choice(characters)
        new_pass += random_char
        count += 1
    return new_pass

if __name__ == "__main__":
    main()
