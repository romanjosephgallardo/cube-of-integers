'''
Steps:
1. Input the size of the array.
2. input the elements of the array
3. display the cube of each element

Sample output

Enter the size of the array : 3
Enter the elements separated by space: 3 10 20
27
1000
8000
'''

# pseudocode

# Get the size of the array
array_size = int(input("Enter the size of the array: "))

# Get the elements of the array
entered_elements = (input("Enter the elements separated by space: "))

array = []
for numbers in entered_elements.split():
    array.append(int(numbers))

# Calculate the cube of each element
for cube in range(array_size):
    array[cube] = array[cube] ** 3

# Display the cube of each element
for display_cube in range(array_size):
    print(array[display_cube])
