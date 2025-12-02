def is_valid_id_p1(id: int) -> bool:
    str_id = str(id)
    middle_index = len(str_id) // 2
    first_half = str_id[:middle_index]
    second_half = str_id[middle_index:]

    return first_half == second_half

def find_invalid_ids_p1(id_range: tuple[int, int]) -> list[int]:
    invalid_ids = []
    for i in range(id_range[0], id_range[1] + 1):
        if len(str(i)) % 2 == 0:
            # We have an even number of digits, so we can check if the number is valid
            if is_valid_id_p1(i):
                invalid_ids.append(i)
    return invalid_ids

def find_invalid_ids_p2(id_range: tuple[int, int]) -> list[int]:
    invalid_ids = []
    for i in range(id_range[0], id_range[1] + 1):
        if is_valid_id_p2(str(i)):
            invalid_ids.append(i)
    return invalid_ids

def is_valid_id_p2(id: str, seq_len = 1) -> bool:
    # this can be any number of repeated digits
    # if sequence length is greater than half, return false
    if seq_len > len(id) // 2:
        return False

    i = seq_len
    match_seq = id[0:seq_len]
    while (i < len(id)):
        print(f'Checking match of {id[i:i+seq_len]} == {match_seq}')
        if id[i:i+seq_len] == match_seq:
            i += seq_len
        else:
            return is_valid_id_p2(id, seq_len=seq_len+1)

    return True    

def parse_range(range_str):
    return tuple[int, int](map(int, range_str.split("-")))

def part1(data):
    id_ranges = [parse_range(range_str) for range_str in data.split(",")]
    invalid_ids = [find_invalid_ids_p1(id_range) for id_range in id_ranges]
    flattened_invalid_ids = [item for sublist in invalid_ids for item in sublist]
    print(flattened_invalid_ids)
    print(sum(flattened_invalid_ids))

def part2(data):
    id_ranges = [parse_range(range_str) for range_str in data.split(",")]
    invalid_ids = [find_invalid_ids_p2(id_range) for id_range in id_ranges]
    flattened_invalid_ids = [item for sublist in invalid_ids for item in sublist]
    print(flattened_invalid_ids)
    print(sum(flattened_invalid_ids))

TEST_DATA = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    part2(data)
    #part2(TEST_DATA)
   