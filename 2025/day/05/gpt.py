import sys

def merge_ranges(ranges):
    """Merge overlapping [start, end] ranges."""
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # overlapping or directly adjacent
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def parse_input(lines):
    """Parse the input lines into fresh_ranges and available_ids."""
    lines = [line.strip() for line in lines]

    # Split on blank line
    blank_index = lines.index('')
    fresh_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    fresh_ranges = []
    for line in fresh_lines:
        a, b = map(int, line.split('-'))
        fresh_ranges.append((a, b))

    available_ids = [int(x) for x in id_lines if x]

    return fresh_ranges, available_ids


def count_fresh_ids(merged_ranges, ids):
    """Count how many ids fall into any of the merged ranges."""
    count = 0
    for x in ids:
        for start, end in merged_ranges:
            if x < start:
                break
            if start <= x <= end:
                count += 1
                break
    return count


def total_fresh_ids(merged_ranges):
    """Total number of distinct IDs covered by merged_ranges."""
    return sum(end - start + 1 for start, end in merged_ranges)


def main():
    fresh_ranges, available_ids = parse_input(open('2025/day/05/input.txt').readlines())
    merged = merge_ranges(fresh_ranges)

    # Part 1
    part1 = count_fresh_ids(merged, available_ids)
    print("Part 1:", part1)

    # Part 2
    part2 = total_fresh_ids(merged)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
