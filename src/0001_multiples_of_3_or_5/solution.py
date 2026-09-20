def sum_multiples_of_3_or_5(upper_limit: int) -> int:
    """Return the sum of non-negative multiples of 3 and 5 below upper_limit."""
    return sum(x for x in range(upper_limit) if x % 3 == 0 or x % 5 == 0)


if __name__ == "__main__":
    assert sum_multiples_of_3_or_5(10) == 23

    print(sum_multiples_of_3_or_5(1000))
