def find_the_max_value():
    def largest(arr, n):
        max = arr[0]
        for i in range(1, n):
            if arr[i] > max:
                max = arr[i]
        return max

    arr = [10, 324, 45, 90, 1]
    print(list(set(arr)))
    arr = arr[::-1]
    print(arr)
    # arr = input("give a list of random numbers")
    n = len(arr)
    Ans = largest(arr, n)
    print(f"The largest in the given array is {Ans}")


def find_frequency_of_an_element_in_an_array():
    array = [1, 2, 8, 3, 2, 2, 2, 5, 1]
    fr = [None] * len(array)
    visited = -1

    for i in range(0, len(array)):
        count = 1;
        for j in range(i + 1, len(array)):
            if (array[i] == array[j]):
                count = count + 1
                fr[j] = visited
        if (fr[j] != visited):
            fr[i] = count
    print("----------------------")
    print(" Element | Frequency ")
    print("----------------------")
    for i in range(0, len(fr)):
        if (fr[i] != visited):
            print(" " + str(array[i]) + " | " + str(fr[i]))
    print("----------------------")

def find_the_smallest_value_in_an_array():
    the_arr = [25, 43, 6, 4, 23, 5, 3]

    min = the_arr[0]
    for i in range(0, len(the_arr)):
        if (the_arr[i] > min):
            min = the_arr[i]
    print(f"The smallest value in this array is {min}")

def find_the_most_or_least_repeated_number_in_an_array():
    the_arr = [1, 2, 8, 3, 2, 2, 2, 5, 1, 5, 6, 6, 5, 3]
    most = max(set(the_arr), key=the_arr.count)
    least = min(set(the_arr), key=the_arr.count)
    print(f"The most repeated number in this array is {most}")
    print(f"The least repeated number in this array is {least}")

def find_the_squres_of_prime_numbers():
    def squres_of_prime():
        my_range = []
        your_range = int(input("What's the range that you want the squres of prime numbers: "))
        for i in range(your_range):
            if i % 2 == 1:
                my_range.append(i ** 2)
        print(my_range)
    squres_of_prime()

def get_the_sum_of_multiple_parameters():
    def sum(*a):
        result = 0
        for i in a:
            result = result + i
        return result

    print(sum(2, 4, 5, 6, 78, 56))

def fint_the_squres_of_even_numbers():
    def find_squres_of_even():
        my_range = []
        your_range = int(input("What's the range that you want the squres of prime numbers: "))
        for i in range(your_range):
            if i % 2 == 0:
                my_range.append(i ** 2)
        print(my_range)

    find_squres_of_even()

def system():
    name = input("Name: ")
    adm_no = input("Student No: ")
    # Let's assume the student is taking the following Units MAT, ENG, ENV, ACS, MAS, HPE, BIL, PHL
    mat = int(input("MAT: "))
    eng = int(input("ENG: "))
    env = int(input("ENV: "))
    acs = int(input("ACS: "))
    mas = int(input("MAS: "))
    hpe = int(input("HPE: "))
    bil = int(input("BIL: "))
    phl = int(input("PHL: "))
    def grading_system():
        # Assumption that we're using Dayster University Grading System
        if mat >= 91 :
            mat_grade = "A"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=81 & mat < 91:
            mat_grade = "A-"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >= 76 & mat < 81:
            mat_grade = "B+"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=71 & mat < 76:
            mat_grade = "B"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=66 & mat < 71:
            mat_grade = "B-"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=61 & mat < 66:
            mat_grade = "C+"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=56 & mat < 61:
            mat_grade = "C"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=51 & mat < 56:
            mat_grade = "C-"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=46 & mat < 51:
            mat_grade = "D+"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=42 & mat < 46:
            mat_grade = "D"
            print(f"MAT: {mat} ({mat_grade})")
        elif mat >=0 & mat < 41:
            mat_grade = "F"
            print(f"MAT: {mat} ({mat_grade})")
        else:
            mat_grade = "Invalid Marks"
            print(f"MAT: {mat} ({mat_grade})")


    grading_system()
system()