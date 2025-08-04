def roman_to_int(s: str) -> int:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    n = len(s)

    for i in range(n - 1):
        current_value = values[s[i]]
        next_value = values[s[i+1]]

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    result += values[s[-1]]
    return result