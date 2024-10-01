# Cube of integers:

# Get the size of the array
try:
    array_size = int(input("Enter the size of the array: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Get the elements of the array
while True:
    entered_elements = (input("Enter the elements separated by space: ")).split()
    if len(entered_elements) != array_size:
        print(f"Invalid input. Please enter an integer with {array_size} elements seperated with spaces")
        exit()
    elif len(entered_elements) == array_size:  
        break
    else:
        print("Ivalid input. Please enter an integer")
        exit()

# Convert the elements to distinct value of integers
array = []
for numbers in entered_elements:
    array.append(int(numbers))

# Calculate the cube of each element
for cube in range(array_size):
    array[cube] = array[cube] ** 3
    # Print the array
    print(array[cube])