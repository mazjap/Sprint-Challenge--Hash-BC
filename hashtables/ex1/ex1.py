#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if len(weights) < 2:
        return (None, None)

    for key in weights:
        value = limit - key
        hash_table_insert(ht, key, value)

    for index in range(len(weights)):
        key = weights[index]
        value = limit - key
        if hash_table_retrieve(ht, value):
            second_index = weights.index(hash_table_retrieve(ht, key))
            return (max(index, second_index), min(index, second_index))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(f"answer_2[0] ({answer_2[0]}) == 1: {answer_2[0] == 1}")
print(f"answer_2[1] ({answer_2[1]}) == 0: {answer_2[1] == 0}")


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(f"answer_4[0] ({answer_4[0]}) == 6: {answer_4[0] == 6}")
print(f"answer_4[1] ({answer_4[1]}) == 2: {answer_4[1] == 2}")