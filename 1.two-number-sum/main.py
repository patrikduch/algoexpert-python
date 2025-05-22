

def twoNumberSum(array, targetSum):

    i = 0
    j = 1

    while i < len(array):

        j = i + 1
        

        while j < len(array):

            if (array[i] + array[j] == targetSum):

                return [array[i], array[j]]

            j += 1
        i += 1
    
    return []


array = [1,2,3]


test = twoNumberSum(array, 3)

print(test)