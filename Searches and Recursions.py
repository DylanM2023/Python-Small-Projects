



def menu():
    print("######################################################")
    print("                        MENU                          ")
    print("     1. A subroutine that performs recursion")
    print("     2. A subroutine that performs a linear search")
    print("     3. A subroutine that performs a binary sort")
    print("     4. A subroutine that performs a bubble sort")
    print("     5. A subroutine that performs an insertion sort")
    print("     6. A subroutine that performs a merge sort")
    print("     7. EXIT PROGRAM")
    print("######################################################")
    user_input = int(input("Which subroutine would you like to run?(1-7): "))
    return user_input

def exit():
    Exit = str(input("\n \n WOULD YOU LIKE TO CONTINUE? YES or NO: "))
    
    if (Exit.upper()) == "YES" or (Exit.upper()) == "EYS" or (Exit.upper()) == "ES" or (Exit.upper()) == "SYE":
        return ""
    else:
        return "1"

def recursion(n):
	if n == 0:
		return 1
	else:
		return n * recursion(n-1)


def linear(letters, n, item):
    for i in range(0, n):
        if (letters[i] == item):
            return i
    return -1

def binary(letters,item,lowerBound,upperBound):
    while lowerBound <= upperBound:
        midpoint = lowerBound+(upperBound-lowerBound)//2
        if letters[midpoint]==item:
            print(midpoint+1)
            return midpoint
        elif letters[midpoint]<item:
            lowerBound=midpoint+1
            print(midpoint+1)
        else:
            upperBound = midpoint-1
            print(midpoint+1)
    return -1

def bubbleSort(array):
    for i in range(len(array)):
        print(data)
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

def insertion(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key
        print(data)

def merge(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        merge(L)
        merge(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


Start = input("PRESS ENTER TO START")
while Start == "":
    user_input = int(menu())
    while user_input >= 1 or user_input <=6:
        if user_input == 1:
            base = 4
            answer = recursion(base)
            print("Factorial of",base,"is",answer)
            break
        
        if user_input == 2:
            letters = ["B", "V", "D", "E", "T", "P"]
            print(letters)
            item = input("Enter the item to be found: ")
            n = len(letters)
            result = linear(letters, n, item)
            if(result == -1):
                print("Element not found.")
            else:
                print("Element found at index: ", result)  
            break
        if user_input == 3:
            letters=["A","B","C","D","E","F","G","H","I","J"]
            print(letters)
            item=input("Enter the item to be found: ")
            result = binary(letters,item,0,len(letters)-1)
            if result != -1:
                print (item,"found at position",str(result+1))
            else:
                print (item,"not found")

        if user_input == 4:
            data = [6,5,4,3,10]
            bubbleSort(data)
            print('Sorted Array in Ascending Order:',data)
            break
        if user_input == 5:
            data = [3,6,5,11,2,7,1]
            print(data)
            insertion(data)
            print('Insertion Sorted Array in Ascending Order:',data)

        if user_input == 6:
            array = [6, 5, 12, 10, 9, 1]
            print(array)
            merge(array)
            print("Merge sorted array is: ")
            print(array)

        
        if user_input == 7:
            quit()
        menu()
        user_input = int(menu())
    Start=exit()
quit()
