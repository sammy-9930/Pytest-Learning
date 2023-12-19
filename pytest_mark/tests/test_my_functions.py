"""uses my_functions.py source file"""

@pytest.mark.slow
def test_very_slow():
    """This is a slow test which adds 5 seconds delay."""
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    """Test is skipped during execution denoted by 's'"""
    assert my_functions.add(1, 2) == 3


@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero_broken():
    """Add this marker when we know the test will fail"""
    my_functions.divide(3, 0)
