def dicc_counter(variable):
    '''
    Encodes a sequence (like a string or list) using Run-Length Encoding.

    This algorithm iterates through the input sequence and counts consecutive occurrences of the 
    same element. When the element changes or the end of the sequence is reached, it appends a list 
    containing the element and its count to the result

    Args:
        variable (sequence): The input sequence to be encoded
    Returns:
        list: A list of lists, where each inner list contains an element from the input sequence and its 
        consecutive count.

    Example: 
    >>> run_length_encoding("aaaabbcca")
        [['a', 4], ['b', 2], ['c', 2], ['a', 1]] 
    '''

    counter = 1
    result = []

    for position in range(len(variable)):
        current = variable[position]
        next = variable[position + 1] if position + 1 < len(variable) else None

        if current != next:
            result.append([current, counter])
            counter = 1
        else:
            counter += 1
        
    return result


