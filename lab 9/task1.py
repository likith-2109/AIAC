def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two integers.

    Example:
        result = add_numbers(2, 3)
    """
    return a + b

def multiply_numbers(x: float, y: float) -> float:
    """Multiplies two floating-point numbers.

    Args:
        x (float): The first number to multiply.
        y (float): The second number to multiply.

    Returns:
        float: The product of the two numbers.

    Example:
        product = multiply_numbers(1.5, 2.0)
    """
    return x * y

def greet(name: str) -> str:
    """Generates a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.

    Example:
        message = greet("Alice")
    """
    return f"Hello, {name}!"

def is_even(number: int) -> bool:
    """Checks if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.

    Example:
        result = is_even(4)
    """
    return number % 2 == 0
