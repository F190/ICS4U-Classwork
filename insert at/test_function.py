from function import insert_at, insert_sorted


def test_insert_at():
    original = [1, 2, 3, 4]
    expecting = [1, 2, 5, 3, 4]
    result = insert_at(original, 5, 2)
    assert result == expecting

def test_insert_sorted():
    original = [1, 2, 3, 5]
    expecting = [1, 2, 3, 4, 5]
    result = insert_sorted(original, 4)
    assert result == expecting

    original = [1, 234, 345, 456, 567]
    expecting = [1, 234, 345, 346, 456, 567]
    result = insert_sorted(original, 346)
    assert result == expecting