def sum_of_odd_squares(upper_limit: int) -> int:
    """Return the sum of squares of all odd numbers from 1 to upper_limit (inclusive)."""
    return sum(x * x for x in range(1, upper_limit + 1, 2))


if __name__ == "__main__":
    assert sum_of_odd_squares(5) == 35

    print(sum_of_odd_squares(176000))
