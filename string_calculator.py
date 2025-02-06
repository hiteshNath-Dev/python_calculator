def add(numbers: str) -> int:
    
    """
    Adds numbers from a given string.

    Args:
        numbers (str): A string containing numbers seperated by delimiters.

    Returns:
        int: The sum of the numbers. Returns o if the string is empty.
    """
    
    if not numbers:
        return 0
    
    delimiter = ","
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)

    return sum(map(int, numbers.replace("\n", delimiter).split(delimiter)))
