def main():
    print("I am main")


# Call my value
# main()

# Call by reference
# a = main
# a()

from convert_to_upper_case import CTUC as yay

@yay
def say_hii():
    return "helllo"

print(say_hii())