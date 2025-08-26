def forty_two(str_1, str_2, str_3):
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if user_input == str_1 or user_input == str_2 or user_input == str_3:
        return "Yes"
    else:
        return "No"
forty_two("42", "forty-two", "forty two")


def greeting():
    user_input = input("Greeting:")
    a = user_input.split()
    if a[0] == "hello":
        return "$0"
    elif user_input[0] == "h":
        return "$20"
    else:
        return "$100"
greeting()