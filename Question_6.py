# An empty list to store the user's input values is being initialized
values = []

# Loop 5 times to get 5 values from the user
for i in range(5):
    value = float(input(f"Enter value {i+1}: "))
    values.append(value)

# Calculate the average of the values
average = sum(values) / len(values)

print(f"The average of the values is {average:.2f}")