from _csv import writer

import paramiters
# paramiters.find_the_max_value()
# paramiters.find_frequency_of_an_element_in_an_array()
# paramiters.find_the_most_or_least_repeated_number_in_an_array()
# aramiters.find_the_squres_of_prime_numbers()
# paramiters.get_the_sum_of_multiple_parameters()
# paramiters.fint_the_squres_of_even_numbers()

# paramiters.grading_system()


while True:
    ourFile = open('myname.txt', 'w+')
    name = input("Name: ")
    age = int(input("Age: "))
ourFile.write(f"Name: {name}\n")
ourFile.write(f"Age: {age}\n")
