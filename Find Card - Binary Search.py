
#Binary Search Algo
def binary_locate_cards(cards, query):
    lo,hi = 0, len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]

        print("Low:",lo,"\t High:",hi,"\t Mid:",mid,"\tMid Number:",mid_number)

        if mid_number == query: return mid
        elif mid_number>query : hi = mid - 1
        elif mid_number<query : lo = mid + 1

    return -1
    pass

cards = [1,4,5,6,7,8,9,10,11]
query = 10

result = binary_locate_cards(cards,query)
print(result)


def test_binary_locate_cards(cards, query):
    # Test 1: Query is in the middle
    assert binary_locate_cards([1, 4, 5, 6, 7, 8, 9, 10, 11], 7) == 4

    # Test 2: Query is the first element
    assert binary_locate_cards([1, 4, 5, 6, 7, 8, 9, 10, 11], 1) == 0

    # Test 3: Query is the last element
    assert binary_locate_cards([1, 4, 5, 6, 7, 8, 9, 10, 11], 11) == 8
    # Test 4: Query is not in the list
    assert binary_locate_cards([1, 4, 5, 6, 7, 8, 9, 10, 11], 3) == -1

    # Test 5: Empty list
    assert binary_locate_cards([], 5) == -1

    # Test 6: List with one element (match)
    assert binary_locate_cards([5], 5) == 0

    # Test 7: List with one element (no match)
    assert binary_locate_cards([5], 7) == -1

    # Test 8: Query is in the middle of even-length list
    assert binary_locate_cards([4, 6, 8, 10, 12], 8) == 2

    print("All Cases passed")

    pass


test_binary_locate_cards(cards,query)