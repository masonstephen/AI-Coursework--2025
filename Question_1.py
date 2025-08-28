# The line below will ask the user for the number of days
days = int(input("Enter the number of days: "))

# Calculate the number of seconds in the given number of days inputed by the user
seconds = days * 24 * 60 * 60

# Print the result
print(f"The number of seconds in {days} days is {seconds} seconds.")