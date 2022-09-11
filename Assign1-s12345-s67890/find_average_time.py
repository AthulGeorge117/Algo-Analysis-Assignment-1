from run_dictionary_data_sructure import run_dictionary_data_structure
import time
import sys

# python dictionary_file_based.py array sampleDataToy.txt testToy.in testToy.out

def find_average_time(data_structure, data_input, data_command, data_output):

    number_of_runs = 10

    total_time = [0, 0, 0, 0, 0]
    for n in range(number_of_runs):

        args = ["dictionary_file_based.py", data_structure, data_input, data_command, data_output]
        run_time = run_dictionary_data_structure(args)

        for x in range(len(total_time)):
            total_time[x] += run_time[x]
    
    average_time = [0, 0, 0, 0, 0]
    for x in range(len(total_time)):
        average_time[x] = round(total_time[x] / number_of_runs, 4) 

    return average_time  

if __name__ == '__main__':

    data_commands = ["add.in", "delete.in", "search.in", "auto_complete.in"]
    data_output = "testToy.out"

    data_structures = ["array", "linkedlist", "trie"]
    data_sizes = [500, 1000, 5000, 10000, 50000, 100000, 200000]

    # run times are in ms
    for data_structure in data_structures:
        for data_size in data_sizes:
            data_input = f"testData{data_size}words.txt"
            for data_command in data_commands:
                average_time = find_average_time(data_structure, data_input, data_command, data_output)
                # total_time = 0
                # for t in average_time:
                #     total_time += t
                # total_time = round(total_time / len(average_time), 4) 
                print(f"{data_structure} with {data_size} words for {data_command} has average_time: {average_time}")
            print()
        print("--------------------------------------------------------------------------------------------")