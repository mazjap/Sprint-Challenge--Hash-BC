#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if len(weights) > 1:
#       [12,   6, 7, 14, 19, 3, 0, 25, 40]
#       [      1, 0,         4, 7        ]
        for index in range(len(weights)):
            key = weights[index] # 0
            value = limit - key # 7 - 0 = 7
            if key <= limit: # True
                hash_table_insert(ht, key, value) # ht[hash(0)] = 7
            if hash_table_retrieve(ht, value) is not None: # False? Whats the difference between putting 'is not None' and not having it?
                second_index = weights.index(hash_table_retrieve(ht, key))
                print(second_index)
                if index is not second_index:
                    return (max(index, second_index), min(index, second_index))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")