#Problem Statement: We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.


cards = [1,2,4,5,6,7,12,13]
query = 7
output = 5

#linear search algo:
def linear_locate_card(cards, query):
    position = 0
    for position in range(len(cards)):
        if cards[position] == query:
            return position
        else: position = position+1
    return -1

#result = linear_locate_card(cards,query)
#print(result)


def test_linear_locate_cards():

    #Case 1: Query is in the middle of the deck
    assert linear_locate_card([1,4,5,7,8,9,10],7) == 3

    #Case 2: Query is the first element
    assert linear_locate_card([1,3,4,5,8,9],1) == 0

    #Case 3: Query is the last element
    assert linear_locate_card([1,3,4,5],5) == 3

    #Case 4: Query is not in the list
    assert linear_locate_card([1,3,4,5,7],8) == -1

    #Case 5: No list
    assert  linear_locate_card([],7) == -1

    print("All Test Cases passed")


test_linear_locate_cards()

