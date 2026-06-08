import pytest
@pytest.mark.printstatement
def test_sample_one():
    print("Hai")
@pytest.mark.xfail(reason="xfail")
def test_sample1():
    a=10
    b=9
    assert a==b
@pytest.mark.lessernum
def test_sample2():
    a=5
    b=10
    assert a<b
#@pytest.mark.skip(reason="No need")
@pytest.mark.nameequal
def test_sample3():
    a="arun"
    b="arun"
    assert a.__eq__(b)