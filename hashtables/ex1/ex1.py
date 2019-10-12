#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(len(weights)):
        weight = weights[i]
        hash_table_insert(ht, weight, i)
    
    for weight in weights:
        print(hash_table_retrieve(ht, weight))
    print("****")

    for weight in weights:
        diff = limit - weight
        value = hash_table_retrieve(ht, diff)
        if value is not None:
            index = hash_table_retrieve(ht, weight)
            if index > value:
                return [index, value]
            else:
                return [value, index]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# weights_2 = [4, 6, 3, 2]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_2)