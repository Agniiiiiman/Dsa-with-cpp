""""
How it works:

Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.
""""" 

# List of numbers to sort
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Bubble Sort logic
for i in range(len(my_array) - 1):
    for j in range(len(my_array) - i - 1):
        # Swap if the current number is bigger than the next number
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

# Print the sorted list
print("Sorted array:", my_array)



# Bubble Sort using function 

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example array
my_array = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", my_array)

bubble_sort(my_array)

print("Sorted array:",my_array)

