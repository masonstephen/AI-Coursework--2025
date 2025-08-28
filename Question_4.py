# Define a function to check if a character is uppercase or lowercase
def check_case(char):
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    else:
        return "Neither"

# Ask the user for a character
char = input("Enter a character: ")

# Check the case of the character and print the result
result = check_case(char)
print(f"The character '{char}' is {result}.")