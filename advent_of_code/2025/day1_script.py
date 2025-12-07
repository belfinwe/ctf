import json

def main(seq: str, current_number: int):
    # print(f"Got {seq}, current number is {current_number}")
    increment = 1
    if seq[0].upper() == "L":
        increment = -1

    turns = int(seq[1:])

    number = current_number
    number_of_times_at_zero = 0
    for i in range(0, turns):
        number += increment

        if number < 0:
            number = 99
        elif number > 99:
            number  = 0

        if number == 0:
            number_of_times_at_zero += 1

    return number, number_of_times_at_zero


if __name__ == "__main__":
    # # Testing
    # number = 5
    # number = main("L10", number)
    # print(f"Input L10, new number: {number}")
    # print("----------------------")
    # number = main("R5", number)
    # print(f"Input R5, new number: {number}")
    password_counter = 0
    number = 50  # Could not see any other starting position in the text

    with open("seq.json", "r") as seq_file:
        seqs = json.load(seq_file)
        for seq in seqs:
            number, tmp_password_counter = main(seq, number)
            password_counter = password_counter + tmp_password_counter


    print(f"The passowrd is: {password_counter}")

