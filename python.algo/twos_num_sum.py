def twoNumberSum(array, targetSum):
    new_array = []
    print(len(array))
    for i in range(len(array)-1):
        firstNumber = array[i]
        for j in range(i + 1, len(array)):
            secondNumber = array[j]
            if firstNumber + secondNumber == targetSum:
                new_array.append(firstNumber)
                new_array.append(secondNumber)
                return new_array
                #return [firstNumber, secondNumber]
    return []

array = [1, 23, 34, 4, 2, 5, 6, 7, 9 -3]
targetSum = 500
print(twoNumberSum(array, targetSum))