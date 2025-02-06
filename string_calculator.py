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

    num_list = [int(n) for n in numbers.replace("\n", delimiter).split(delimiter)]
    negatives = [n for n in num_list if n < 0]

    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")
    
    return sum(num_list)