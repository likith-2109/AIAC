def scrip(data):
    result = []
    for i, item in enumerate(data):
        if isinstance(item, str) and item.isdigit():
            num = int(item)
            if num % 2 == 0:
                result.append(num * 2)    # Double even numbers found as digit-strings
            else:
                result.append(num + 1)    # Increment odd numbers found as digit-strings
        elif isinstance(item, int):
            if item < 0:
                result.append(abs(item))  # Convert negative integers to positive
            else:
                result.append(item)
        else:
            continue    # Skip items that are neither int nor digit-string
    return result
