# Define a function to calculate the area of a square
def calculate_area(side_length):
    return side_length ** 2

# Define a function to calculate the perimeter of a square
def calculate_perimeter(side_length):
    return 4 * side_length

# Ask the user for the side length of the square
side_length = float(input("Enter the side length of the square: "))

# Calculate and print the area and perimeter
area = calculate_area(side_length)
perimeter = calculate_perimeter(side_length)
print(f"The area of the square with side length {side_length} is {area:.2f} square units.")
print(f"The perimeter of the square with side length {side_length} is {perimeter:.2f} units.")