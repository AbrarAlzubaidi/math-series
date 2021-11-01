from math_series import __version__
from math_series.series import fibonacci 
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fib_best():
    expected=1
    actual=fibonacci(1)
    assert actual == expected

def test_fib():
    expected=5
    actual=fibonacci(5)
    assert actual == expected

def test_lucas_best():
    expected=1
    actual=lucas(1)
    assert actual == expected

def test_lucas():
    expected=11
    actual=lucas(5)
    assert actual == expected

def test_sum_series():
    expected=11
    actual=sum_series(5,2,1)
    assert actual == expected
    

