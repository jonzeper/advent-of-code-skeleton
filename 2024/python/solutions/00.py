def part_one_prep(lines: list[str]) -> list[int]:
    # Optional prep step, won't be included in benchmarks
    return [int(i) for i in lines[0].split()]


def part_one(ints: list[int]) -> int:
    # Example solution, just summing the numbers from the input
    # Receives the result of prep step as input
    return sum(ints)


def part_two(lines: list[str]) -> int:
    # Without a prep step, solution function receives lines of text from the input
    return 1
