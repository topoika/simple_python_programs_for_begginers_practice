import paramiters

# paramiters.find_the_max_value()
# paramiters.find_frequency_of_an_element_in_an_array()
# paramiters.find_the_most_or_least_repeated_number_in_an_array()
# aramiters.find_the_squres_of_prime_numbers()
# paramiters.get_the_sum_of_multiple_parameters()
# paramiters.fint_the_squres_of_even_numbers()

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