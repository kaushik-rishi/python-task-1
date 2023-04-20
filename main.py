list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


"""
Complete this function, by merging the information from list_1 and list_2
to create a new list, which has all the information about each student from
both lists in one single dict.

- Both lists are unsorted
- Both lists can have missing values (for ex list_2 has missing id=2)
"""
def merge_lists_on2(list_1, list_2) -> list: # O(n^2) -> unoptimised
    merged_dict = {}

    for element in list_1:
        id = element.get("id")
        merged_dict[id] = {k: v for k, v in element.items() if k != "id"}

    for element in list_2:
        id = element.get("id")
        if id in merged_dict:
            merged_dict[id].update({k: v for k, v in element.items() if k != "id"})
        else:
            merged_dict[id] = {k: v for k, v in element.items() if k != "id"}

    merged_list = [{"id": k, **v} for k, v in merged_dict.items()]

    return merged_list

def merge_lists(list_1, list_2) -> list:
    """
    Using a hashmap type approach to map the dictionary of a user to it's ID
    """
    merged_dicts_hash = {}

    for lst in (list_1, list_2):
        for student in lst:
            sid = student["id"]
            if sid in merged_dicts_hash:
                merged_dicts_hash[sid].update(student)
            else:
                merged_dicts_hash[sid] = student.copy()

    merged_list = list(merged_dicts_hash.values())
    return merged_list


list_3 = merge_lists(list_1, list_2)
