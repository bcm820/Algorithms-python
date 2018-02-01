
def bubble_sort(list):
    sorted = True
    for i in range(0, len(list) - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            sorted = False
    if sorted:
        return list
    else:
        return bubble_sort(list)

def selection_sort(list):
    for i in range(0, len(list)):
        minI = i
        for j in range(i, len(list)):
            if list[j] < list[minI]:
                minI = j
        list[i], list[minI] = list[minI], list[i]
    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        current = list[i]
        j = i
        while list[j-1] > current and j > 0:
            list[j] = list[j-1]
            j = j-1
        list[j] = current
    return list