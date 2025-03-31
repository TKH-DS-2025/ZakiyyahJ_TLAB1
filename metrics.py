def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    average = 0
    length = len(data)
    for item in data:
        average += item
    if length != 0:
        average = average/length
        return round(average,2)
    else:
        return data

def maximum(data: list) -> float:
    """
    calculate the maximum value of the list
    
    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of this list
    """
    if not data:
        return data
    maximum = data[0]
    for item in data:
        if item > maximum:
            maximum = item
    return float(maximum)


def variance(data: list) -> float:
    """
    This function calculates population variance

    Argument:
        data (list[int]): list of integers representing heart rate samples
    Returns: 
        float: a floating point value representing the variance in the heart rate samples
    """
    if not data:
        return data
    variance = []
    #Calculate the mean of the data.
    mean = average(data)
    #Find each data point's difference from the mean value and Square each of these values.
    for item in data:
        v_difference = pow((item - mean),2)
        variance.append(v_difference)
    #Add up all of the squared values and Divide this sum of squares by  N (for the total population)
    variance = (sum(variance))/ len(data)
    return float(variance)
    


def standard_deviation(data: list) -> float:
    """
    This function calculates population standard deviation
    Argument:
        data (list[int]): list of integers representing heart rate samples
    Returns: 
        float: a floating point value representing the satndard deviation in the heart rate samples
    """
    #standard deviation is the square root of variance
    if not data:
        return data
    else:
        st_dev = pow(variance(data),.5)   
        return(round((st_dev),2))