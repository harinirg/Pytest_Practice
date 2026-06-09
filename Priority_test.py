import pytest

@pytest.mark.order(4)
def test_sample_one():
    print("Hai")

@pytest.mark.order(2)
def test_sample1():
    a = 10
    b = 10
    assert a == b

@pytest.mark.order(3)
def test_sample2():
    a = 5
    b = 10
    assert a < b

@pytest.mark.order(1)
def test_sample3():
    a = "arun"
    b = "arun"
    assert a.__eq__(b)