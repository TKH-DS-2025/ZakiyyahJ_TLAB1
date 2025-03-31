"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    
    heart_rate_data_file = open(filename)
    data = heart_rate_data_file.readlines() # Returns a list of lines from the file and stores it into data
    #print("Original Data:" ,data)
    heart_rate_data_file.close()


    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    cleaned_data = filter_nondigits(data)
    #print("Cleaned Data: ", cleaned_data)
    

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    
    fig,ax = plt.subplots()
    ax.plot(cleaned_data)
    ax.set_title("Heart Rate Samples Over Time")
    ax.set_title("Heart Rate Samples Over Time")
    ax.set_xlabel("Minutes")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Heart Rate")
    fig.savefig("images/phase")
    fig.show()
    

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(cleaned_data)
    max_hr = maximum(cleaned_data)
    std_dev_hr = standard_deviation(cleaned_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print("Phase 0:",run("data/phase0.txt"))
    print("Phase 1:",run("data/phase1.txt"))
    print("Phase 2:",run("data/phase2.txt"))
    print("Phase 3:",run("data/phase3.txt"))


