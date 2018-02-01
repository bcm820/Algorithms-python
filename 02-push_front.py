
# Swapping in Python (similar to Go)
# arr[0], arr[1] = arr[1], arr[0]

"""
Write a function that takes in a list and a value, and adds the value to the front of that list, outputting the changed list. This should be done in place. This means you should not create a new list, but change the existing one.
Limit your use of built-in functions to only the most basic, doing the harder stuff manually. Use only the built-in list.append(value) method to solve this problem.
"""

def push_front(list, value):
    list.append(value)
    for i in range(len(list)-1, 0, -1):
        list[i], list[i-1] = list[i-1], list[i]
    return list

print(push_front([4,22,3,46,5], 6))