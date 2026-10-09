def fibonacci_numbers(limit: int) -> list[int]:
    """Return a list of Fibonacci numbers up to a given limit."""
    numbers = []
    current_number, next_number = 1, 2

    while current_number <= limit:
        numbers.append(current_number)
        current_number, next_number = next_number, current_number + next_number

    return numbers


def sum_even_fibonacci(limit: int) -> int:
    """Return the sum of even Fibonacci numbers up to a given limit."""
    return sum(number for number in fibonacci_numbers(limit) if number % 2 == 0)


if __name__ == "__main__":
    assert fibonacci_numbers(89) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(sum_even_fibonacci(4_000_000))
