# Cube of integers:

# Get the size of the array
array_size = int(input("Enter the size of the array: "))

# Get the elements of the array
entered_elements = (input("Enter the elements separated by space: ")).split()

array = []
for numbers in entered_elements:
    array.append(int(numbers))

# Calculate the cube of each element
for cube in range(array_size):
    array[cube] = array[cube] ** 3
    # Print the array
    print(array[cube])