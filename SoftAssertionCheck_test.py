import pytest
import pytest_check as check

def test_sample_one():
    print("Hai")

def test_sample1():
    a = 10
    b = 10
    check.equal(a, b, "a and b are not equal")

def test_sample2():
    a = "arun"
    b = "aruns"
    check.equal(a, b, "Strings are not equal")

    print("Execution continues even if check fails")

def test_sample3():
    a = 5
    b = 10
    check.is_true(a < b, "a is not less than b")
