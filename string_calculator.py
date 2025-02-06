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
        parts = numbers.split("\n", 1)
        delimiter = parts[0][2:]
        numbers = parts[1]

    numbers = numbers.replace("\n", delimiter)
    return sum(map(int, numbers.split(delimiter)))