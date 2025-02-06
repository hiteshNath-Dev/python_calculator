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
    
    return sum(int(n) for n in numbers.replace("\n", ",").split(","))