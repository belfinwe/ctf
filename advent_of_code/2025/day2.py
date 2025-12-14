"""
Gift shop, part 2!
"""

import csv

def get_csv_content():
    with open("puzzle_input_day2.csv", "r") as csv_file:
        puzzle = csv_file.read()

        return puzzle


def further_validation_check(code: str) -> bool:
    """
    True = valid, False = invalid
    """
    for i in range(1,len(code)+1):
        sequence_length = 0
        counter = 0
        if len(code) % i == 0 and i < len(code):

            sequence_length = i
            all_sequences = list()

            for j in range(0, int(len(code) / sequence_length), sequence_length):

                if len(all_sequences) == 0 or all_sequences[-1] == j:
                    all_sequences.append(j)
                else:
                    continue

            # code has a sequence
            return code


    """
    # print(f"Checking {code}...")
    if len(code) <= 1 and len(code) % 2 != 0:
        # print(f"{code} is valid")
        return True

    first = code[:int(len(code) / 2)]
    second = code[int(len(code) / 2):]
    if first == second:
        # print(f"Invalid: {first=}, {second=}")
        return False

    # print(f"{code} default to valid")
    return True
    """


def main(puzzle: str):
    """
    """
    pz: list = puzzle.split(",")
    invalid_codes = list()
    valid_codes = list()

    counter = 1
    for digi_sequence in pz:
        print(f"{counter}/{len(pz)}")

        start, end = digi_sequence.split("-")
        print(start, end)

        i = f"{start}"
        while int(i) <= int(end):
            # print(f"{counter}/{len(pz)}: {i}")

            if further_validation_check(i):
                valid_codes.append(i)
            else:
                invalid_codes.append(i)


            i = f"{int(i) + 1}"
        counter += 1

    # print(f"{valid_codes}")
    print(f"{len(invalid_codes)=}")
    return invalid_codes


if __name__ == "__main__":
    puzzle = get_csv_content()
    invalid_codes = main(puzzle)
    answer = 0
    for i in invalid_codes:
        answer += int(i)
    print(answer)

