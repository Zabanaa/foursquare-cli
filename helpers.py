def get_int_input(prompt, min_value=None, max_value=None, default=None):

    user_input = input(prompt + "\n")

    while user_input and int(user_input) not in range(min_value, max_value + 1):
        print("There was a problem")
        user_input = input(prompt + "\n")
    int_to_return = user_input if user_input else default

    return int_to_return

def check_alnum(prompt):

    user_input = input(prompt + '\n')

    while user_input and not all(c.isalnum() or c.isspace() or c == ',' for c in user_input):
        print("Please provide a list of correct alpha numeric strings separated by commas - Leave blank\
 to skip")
        user_input = input(prompt + "\n")

    return user_input

def get_valid_string(prompt):

    user_input = input(prompt + "\n")

    while not all(c.isalpha() or c.isspace() or c == "," for c in user_input) or not user_input:
        print("This is a required field that should only contain letters, spaces and commas. \n")
        user_input = input(prompt + "\n")

    return user_input

