import evaluation_prep


def test_add():
    assert evaluation_prep.add(1, 1) == 2
    assert evaluation_prep.add(-1, -2) == -3


def test_list_sum():
    original = [1, 2, 3, 4, 5]
    expect = 15
    assert evaluation_prep.list_sum(original) == expect
    assert evaluation_prep.list_sum([]) == 0


def test_count_occurances():
    assert evaluation_prep.count_occurances([]) == {}
    assert evaluation_prep.count_occurances(["Mer", "MMer", "Mer"]) == {"Mer": 2, "MMer": 1}
    
    words = ["Mer", "is", "Mer"]
    expect = {"Mer": 2, "is": 1}
    result = evaluation_prep.count_occurances(words)
    assert result == expect