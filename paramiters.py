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


def grading_system():
    def main():
        user_input()

    def user_input():
        while True:
            print("Select Any Option:\n 1 for > Add Data\n 2 for > Quit")
            option = input('Option: ')
            if option == "1":
                user_input1()
            elif option == "2":
                break
            else:
                print("Invalid Option! Please Try Again")
                continue

    def user_input1():
        myFile = open("openfile.txt", "w+")
        name = input("Name: ")
        adm_no = input("Student No: ")
        # Let's assume the student is taking the following Units MAT, ENG, ENV, ACS, MAS, HPE, BIL, PHL
        global mat, eng, env, acs, mis, hpe, bil, phl
        mat = int(input("MAT: "))
        eng = int(input("ENG: "))
        env = int(input("ENV: "))
        acs = int(input("ACS: "))
        mis = int(input("MIS: "))
        hpe = int(input("HPE: "))
        bil = int(input("BIL: "))
        phl = int(input("PHL: "))
        mat_grading_system()
        eng_grading_system()
        env_grading_system()
        acs_grading_system()
        mis_grading_system()
        hpe_grading_system()
        bil_grading_system()
        phl_grading_system()
        myFile.write(
            f"Name: {name}\nStudent No: {adm_no}\nMAT: {mat} : {mat_grade}\nENG: {eng} : {eng_grade}\nENV: {env} : {env_grade}\nACS: {acs} : {acs_grade}\nMIS: {mis} : {mis_grade}\nHPE: {hpe} : {hpe_grade}\nBIL: {bil} : {bil_grade}\nPHL: {phl} : {phl_grade}")

    def mat_grading_system():
        global mat_grade
        if 91 <= mat < 101:
            mat_grade = "A"
        elif 91 > mat >= 81:
            mat_grade = "A-"
        elif 81 > mat >= 76:
            mat_grade = "B+"
        elif 76 > mat >= 71:
            mat_grade = "B"
        elif 71 > mat >= 66:
            mat_grade = "B-"
        elif 66 > mat >= 61:
            mat_grade = "C+"
        elif 61 > mat >= 56:
            mat_grade = "C"
        elif 56 > mat >= 51:
            mat_grade = "C-"
        elif 51 > mat >= 46:
            mat_grade = "D+"
        elif 46 > mat >= 42:
            mat_grade = "D"
        elif 41 > mat >= 0:
            mat_grade = "F"
        else:
            mat_grade = "Invalid Marks"

    def eng_grading_system():
        global eng_grade
        if 91 <= eng < 101:
            eng_grade = "A"
        elif 91 > eng >= 81:
            eng_grade = "A-"
        elif 81 > eng >= 76:
            eng_grade = "B+"
        elif 76 > eng >= 71:
            eng_grade = "B"
        elif 71 > eng >= 66:
            eng_grade = "B-"
        elif 66 > eng >= 61:
            eng_grade = "C+"
        elif 61 > eng >= 56:
            eng_grade = "C"
        elif 56 > eng >= 51:
            eng_grade = "C-"
        elif 51 > eng >= 46:
            eng_grade = "D+"
        elif 46 > eng >= 42:
            eng_grade = "D"
        elif 41 > eng >= 0:
            eng_grade = "F"
        else:
            eng_grade = "Invalid Marks"

    def env_grading_system():
        global env_grade
        if 91 <= env < 101:
            env_grade = "A"
        elif 91 > env >= 81:
            env_grade = "A-"
        elif 81 > env >= 76:
            env_grade = "B+"
        elif 76 > env >= 71:
            env_grade = "B"
        elif 71 > env >= 66:
            env_grade = "B-"
        elif 66 > env >= 61:
            env_grade = "C+"
        elif 61 > env >= 56:
            env_grade = "C"
        elif 56 > env >= 51:
            env_grade = "C-"
        elif 51 > env >= 46:
            env_grade = "D+"
        elif 46 > env >= 42:
            env_grade = "D"
        elif 41 > env >= 0:
            env_grade = "F"
        else:
            env_grade = "Invalid Marks"

    def acs_grading_system():
        global acs_grade
        if 91 <= acs < 101:
            acs_grade = "A"
        elif 91 > acs >= 81:
            acs_grade = "A-"
        elif 81 > acs >= 76:
            acs_grade = "B+"
        elif 76 > acs >= 71:
            acs_grade = "B"
        elif 71 > acs >= 66:
            acs_grade = "B-"
        elif 66 > acs >= 61:
            acs_grade = "C+"
        elif 61 > acs >= 56:
            acs_grade = "C"
        elif 56 > acs >= 51:
            acs_grade = "C-"
        elif 51 > acs >= 46:
            acs_grade = "D+"
        elif 46 > acs >= 42:
            acs_grade = "D"
        elif 41 > acs >= 0:
            acs_grade = "F"
        else:
            acs_grade = "Invalid Marks"

    def mis_grading_system():
        global mis_grade
        if 91 <= mis < 101:
            mis_grade = "A"
        elif 91 > mis >= 81:
            mis_grade = "A-"
        elif 81 > mis >= 76:
            mis_grade = "B+"
        elif 76 > mis >= 71:
            mis_grade = "B"
        elif 71 > mis >= 66:
            mis_grade = "B-"
        elif 66 > mis >= 61:
            mis_grade = "C+"
        elif 61 > mis >= 56:
            mis_grade = "C"
        elif 56 > mis >= 51:
            mis_grade = "C-"
        elif 51 > mis >= 46:
            mis_grade = "D+"
        elif 46 > mis >= 42:
            mis_grade = "D"
        elif 41 > mis >= 0:
            mis_grade = "F"
        else:
            mis_grade = "Invalid Marks"

    def hpe_grading_system():
        global hpe_grade
        if 91 <= hpe < 101:
            hpe_grade = "A"
        elif 91 > hpe >= 81:
            hpe_grade = "A-"
        elif 81 > hpe >= 76:
            hpe_grade = "B+"
        elif 76 > hpe >= 71:
            hpe_grade = "B"
        elif 71 > hpe >= 66:
            hpe_grade = "B-"
        elif 66 > hpe >= 61:
            hpe_grade = "C+"
        elif 61 > hpe >= 56:
            hpe_grade = "C"
        elif 56 > hpe >= 51:
            hpe_grade = "C-"
        elif 51 > hpe >= 46:
            hpe_grade = "D+"
        elif 46 > hpe >= 42:
            hpe_grade = "D"
        elif 41 > hpe >= 0:
            hpe_grade = "F"
        else:
            hpe_grade = "Invalid Marks"

    def bil_grading_system():
        global bil_grade
        if 91 <= bil < 101:
            bil_grade = "A"
        elif 91 > bil >= 81:
            bil_grade = "A-"
        elif 81 > bil >= 76:
            bil_grade = "B+"
        elif 76 > bil >= 71:
            bil_grade = "B"
        elif 71 > bil >= 66:
            bil_grade = "B-"
        elif 66 > bil >= 61:
            bil_grade = "C+"
        elif 61 > bil >= 56:
            bil_grade = "C"
        elif 56 > bil >= 51:
            bil_grade = "C-"
        elif 51 > bil >= 46:
            bil_grade = "D+"
        elif 46 > bil >= 42:
            bil_grade = "D"
        elif 41 > bil >= 0:
            bil_grade = "F"
        else:
            bil_grade = "Invalid Marks"

    def phl_grading_system():
        global phl_grade
        if 91 <= phl < 101:
            phl_grade = "A"
        elif 91 > phl >= 81:
            phl_grade = "A-"
        elif 81 > phl >= 76:
            phl_grade = "B+"
        elif 76 > phl >= 71:
            phl_grade = "B"
        elif 71 > phl >= 66:
            phl_grade = "B-"
        elif 66 > phl >= 61:
            phl_grade = "C+"
        elif 61 > phl >= 56:
            phl_grade = "C"
        elif 56 > phl >= 51:
            phl_grade = "C-"
        elif 51 > phl >= 46:
            phl_grade = "D+"
        elif 46 > phl >= 42:
            phl_grade = "D"
        elif 41 > phl >= 0:
            phl_grade = "F"
        else:
            phl_grade = "Invalid Marks"

    # Call the whole function// Like the whole of the code that is contained in main function
    main()

def new():
    df = pd.DataFrame(
        {'Names': ['David Tampul', 'Gad Owola', 'Ester Montana', 'Minus Colorodo', 'Washington DC', 'Faith Virginia'],
         'MAT': ['67', '65', '69', '90', '74', '97'],
         'ENG': ['67', '65', '69', '90', '74', '97'],
         'ENV': ['67', '65', '69', '90', '74', '97'],
         'ACS': ['67', '65', '69', '90', '74', '97'],
         'STA': ['67', '65', '69', '90', '74', '97'],
         'HPE': ['67', '65', '69', '90', '74', '97'],
         'Population': ['508529', '193551', '32315', '619968', '52555', '227032']})

    df.to_excel('table.xlsx', 'sheet_name:Grading System')

def new_funt():
    myFile = open("table.xlsx", "w+")
    while True:
        name = input("What is your name: ")
        if name.upper() == "QUIT":
            break
        age = input("How old are you: ")
        gender = input("What is your gender: ")
        myFile.write(f"Name: {name}\n")
        myFile.write(f"Age: {age}\n")
        myFile.write(f"Gender: {gender}\n")
        print("Data Succesfully Saved")

def import_ccv():
    def main():
        def data_for_table():
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
                if mat >= 91:
                    mat_grade = "A"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 81:
                    mat_grade = "A-"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 76 & mat < 81:
                    mat_grade = "B+"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 71 & mat < 76:
                    mat_grade = "B"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 66 & mat < 71:
                    mat_grade = "B-"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 61 & mat < 66:
                    mat_grade = "C+"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 56 & mat < 61:
                    mat_grade = "C"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 51 & mat < 56:
                    mat_grade = "C-"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 46 & mat < 51:
                    mat_grade = "D+"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 42 & mat < 46:
                    mat_grade = "D"
                    print(f"MAT: {mat} ({mat_grade})")
                elif mat >= 0 & mat < 41:
                    mat_grade = "F"
                    print(f"MAT: {mat} ({mat_grade})")
                else:
                    mat_grade = "Invalid Marks"
                    print(f"MAT: {mat} ({mat_grade})")

        filename = "Grading System.csv"
        header = (
        "Name", "Student No", "MAT", "MAT Grade", "ENG", "ENG Grade", "ACS", "ACS Grade", "HPE", "HPE Grade", "ENV",
        "ENV Grade", "STA", "STA Grade", "GOE", "GOE Grade")
        data = data_for_table()
        writer(header, data, filename, "write")
        updater(filename)

    def writer(header, data, filename, option):
        with open(filename, "w", newline="") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")

    def updater(filename):
        with open(filename, newline="") as file:
            readData = [row for row in csv.DictReader(file)]
            # print(readData)
            readData[0]['Rating'] = '9.4'
            # print(readData)

        readHeader = readData[0].keys()
        writer(readHeader, readData, filename, "update")

    if __name__ == "__main__":
        main()
