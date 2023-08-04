__author__ = "Uğurkan Hoşgör"
__version__ = "1.0.0"
def execute(input):
    """Finds out the longest substring in it that doesn't contain any duplicate characters.

    Time complexity: O(n) where n is the length of the input string.

    Parameters:
    input (str): The input string to find the longest substring that doesn't contain any duplicate characters.

    Returns:
    tuple: A tuple which contains the longest substring without duplicates and its length.

    """
    #Result Variables
    maxStart = 0
    maxLength = 0
    #Temporary Variables
    start = 0
    length = 0
    #Loop Variables
    index = 0
    lastChar = ''
    while index < len(input):
        currentChar = input[index]
        if lastChar != currentChar: #Different Character
            length = length + 1
            if length > maxLength: #If it is longer
                maxLength = length
                maxStart = start
        else: #Same Character
            length = 1
            start = index
        index = index + 1
        lastChar = currentChar
    return input[maxStart:maxStart+maxLength], maxLength
    
if __name__ == "__main__":
    input = input("input: ").strip()
    str, length = execute(input)
    print(f"output: {str} length: {length}")