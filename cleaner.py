def filter_nondigits(data: list) -> list:
    """
    This function will take in a list of strings and filter out all the strings that include non digit characters such as the new-line character (\n).
    Then it will convert these digit characters into integers and append it into a new list. 
        Argument: data: list 
        Return: list of integers
    
    """

    non_digits_list = []
    for item in data:
        #if item in the data list is a digit, convert to integer, and then add those items to a list.  
        if item.strip().isdigit():
            non_digits_list.append(int(item))
    return non_digits_list
   