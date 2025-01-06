import os
os.system('clear')


""" SIMPLE ALGORITHMS """
prev2 = 0
prev1 = 1
# print(prev2)
# print(prev1)
for i in range(18):
    new_Fibonacci = prev1 + prev2
    # print(new_Fibonacci)
    prev2 = prev1
    prev1 = new_Fibonacci

count = 2
def Fibonacci(prev2, prev1):
    global count
    if count <= 19:
        new_Fibonacci = prev1 + prev2
        print(new_Fibonacci)
        prev2 = prev1
        prev1 = new_Fibonacci
        count += 1
        return Fibonacci(prev2, prev1)
# Fibonacci(0, 1)

def F(n):
    if n <= 1:
        return n
    return F(n - 1) + F(n - 2)
# print(F(19))



""" ARRAYS """
array = [7, 12, 9, 4, 11]                   # Eng kichik qiymatni topish algoritmi O(n) vaqt murakkabligi bilan ishlaydi.

minVal = array[0]
for i in array:
    if i < minVal:
        minVal = i
# print(minVal)



"""" BUBBLE SORT """
my_array = [64, 34, 25, 12, 22, 11, 90, 5]  # Tartiblash O(n ** 2) vaqt murakkabligi bilan ishlaydi.

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
# print("Sorted array:", my_array)


my_array = [7, 3, 9, 12, 11]

n = len(my_array)
for i in range(n-1):                        # Bu holat agar array tartiblangan bo'lsa  O(n ** 2) ish bajarilishini oldini olish uchun ***swapped*** pointeri yozilgan!
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        break
# print("Sorted array:", my_array)



"""" SELECTION SORT """
my_array = [64, 34, 25, 5, 22, 11, 90, 12]  

n = len(my_array)                           # Bu algoritmda elementlarni siljitish muammosi bor!
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)
# print("Sorted array:", my_array)


my_array = [64, 34, 25, 5, 22, 11, 90, 12]  # Tartiblash O(n ** 2) vaqt murakkabligi bilan ishlaydi.

n = len(my_array)                           # Bu algoritmda elementlarni siljitish muammosi hal qilingan!
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
# print("Sorted array:", my_array)



""" INSERTION SORT """
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)                           # Bu algoritmda elementlarni siljitish muammosi bor!
for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)
# print("Sorted array: ", my_array)


my_array = [64, 34, 25, 5, 22, 11, 90, 12]  # Tartiblash O(n ** 2) vaqt murakkabligi bilan ishlaydi.

n = len(my_array)                           # Bu algoritmda elementlarni siljitish muammosi hal qilingan!
for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value
print("Sorted array: ", my_array)