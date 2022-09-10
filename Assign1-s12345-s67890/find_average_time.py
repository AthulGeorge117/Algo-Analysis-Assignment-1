import time
from dictionary_file_based import main

if __name__ == '__main__':

    number_of_runs = 10

    total_time = 0
    for n in range(number_of_runs):

        start_time = time.time()
        main()
        end_time = time.time()

        run_time = end_time - start_time
        print("runtime", run_time)

        total_time.append(run_time)
    
    average_time = total_time / number_of_runs
    print("average_time", average_time)
    
    
