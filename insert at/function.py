def insert_at(
    insert_list: list,
    insert_value: int,
    insert_index: int
) -> list:
    new_list = [0] * (len(insert_list) + 1)

    #below insert_value
    i = 0
    while i < insert_index:
        new_list[i] = insert_list[i]
        i += 1

    #at insert_value
    new_list[i] = insert_value
    i += 1


    #over insert_value
    while i < len(new_list):
        new_list[i] = insert_list[i-1]
        i += 1

    return new_list







def insert_sorted(original, value):
    i = 1
    smaller = 0
    larger = 0
    while i < len(original):
        smaller = original[i-1]
        larger = original[i+1]
        if value > smaller and value < larger:
            return insert_at(original, value, i+1)
        i += 1