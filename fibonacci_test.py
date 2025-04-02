import pytest

def test_fibonacci():
    from fibonacci import fibonacci

    # Test for the first 10 Fibonacci numbers
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    result = [fibonacci(i) for i in range(10)]
    assert result == expected

    # Test for negative input
    with pytest.raises(ValueError):
        fibonacci(-1)

    # Test for non-integer input
    with pytest.raises(TypeError):
        fibonacci(5.5)

    # # Test for large input
    assert fibonacci(30) == 832040
    assert fibonacci(50) == 12586269025