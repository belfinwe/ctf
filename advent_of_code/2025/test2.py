from day2 import main

def block_test():
    test_string = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    correct_answer = 1227775554

    invalid_codes = main(test_string)
    answer = 0
    for i in invalid_codes:
        answer += int(i)

    assert answer == correct_answer, f"There was an error: {answer=} != {correct_answer=}"


def list_unit_test():
    test_string = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    answer = [
            (11,22),
            (99,111),
            (999,1010,),
            (1188511885,),
            (222222,),
            ([],),
            (446446,),
            (38593859,),
            (565656,),
            (824824824,),
            (2121212121,),
            ([],)
    ]


    invalid_codes_list = list()
    counter = 0
    test_string_list = test_string.split(",")
    for i in test_string_list:
        invalid_codes = main(i)

        if counter >= len(answer) or counter == -1:
            print(f"changing counter to -1")
            counter = -1

        for j in range(len(invalid_codes)):
            assert int(invalid_codes[j]) == int(answer[counter][j]), f"Wrong answer: {invalid_codes[j]} == {answer[counter][j]}. {invalid_codes=}"
            if int(invalid_codes[j]) == int(answer[counter][j]):
                invalid_codes_list.append(invalid_codes[j])

        print(f"{invalid_codes} should match {answer[counter]}")
        counter += 1
    return invalid_codes_list


if __name__ == "__main__":
    final_answer = 4174379265
    the_sum = list_unit_test()
    the_answer = 0
    for i in the_sum:
        the_answer += int(i)
    assert the_answer == final_answer, f"Got the wrong anser: {the_answer} != {final_answer}"
    print(f"{the_answer=}")
