import matplotlib.pyplot as plt
import numpy as np
import re


def sort_file(file_name):
    
    counter = 0
    test_number = []
    coverage_percentage = []


    try:
        opened_file = open(file_name, "r")
    except:
        print ("File not found")
        return

    for command in opened_file:
        
        if(re.search("-------", command)):
            counter+=1
            test_number.append(counter)

        if re.search("Covered percentage", command):

            number = int(re.search(r'\d+', command).group())

            if counter == 0 or (number >= coverage_percentage[len(coverage_percentage)-1]):
                coverage_percentage.append(number)
            else:
                coverage_percentage.append(coverage_percentage[len(coverage_percentage)-1])
    
    plt.plot(test_number, coverage_percentage, color='b')
    plt.xlabel('Test Number')
    plt.ylabel('Coverage %')
    plt.title('Coverage Graph')
    axes = plt.gca()
    axes.set_xlim([0,130])
    axes.set_ylim([0,100])
    plt.show()

    # j = 0
    # while j < len(coverage_percentage):
    #     print ("Test number", test_number[j], "\t", coverage_percentage[j])
    #     j+=1

sort_file("Stats.txt")
