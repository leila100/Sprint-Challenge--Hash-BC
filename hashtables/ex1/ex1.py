#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(len(weights)):
        weight = weights[i]
        val = hash_table_retrieve(ht, weight)
        if val is None:
            hash_table_insert(ht, weight, i)
        else:
            # handle duplicates in weight
            hash_table_insert(ht, weight+100, i)

    for weight in weights:
        diff = limit - weight
        # handle duplicates in weight
        if diff == weight:
            new_weight = weight + 100
            value = hash_table_retrieve(ht, new_weight)
        else:
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