
try:
    numList = list(map(int, input("Введите последовательность чисел через пробел ").split()))
except ValueError:
    print("Введен неверный тип данных")
    numList = list(map(int, input("Введите последовательность чисел через пробел ").split()))
try:
    num = int(input("Введите любое число "))
except ValueError:
    print("Введен неверный тип данных")
    num = int(input("Введите любое число "))

def sortFun(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

sorted_list = sortFun(numList)
print(sorted_list, num)

def binary_search(array, element, left, right):
    if left > right:  
        return False
    middle = (right + left) // 2
    if element <= max(array) and element >= min(array):
        if array[middle] < element <= array[middle+1]:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        elif element > array[middle]:
            return binary_search(array, element, middle + 1, right)
        else:
            return "Введенное число не подходит под условия поиска"
    else:
        print("Введенное число за границами диапазона")

print(binary_search(numList, num, numList[0], numList[-1]))



