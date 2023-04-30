import pytest
from moduls.example_for_pytest.func_devision import devision



@pytest.mark.parametrize("a, b, res", 
                         [(10, 2, 5), 
                          (20, -2,-10),
                          (5, 2, 2.5)])
def test_devision_good(a, b, res):
    assert devision(a, b) == res

def test_devision_zero():
    with pytest.raises (ZeroDivisionError):
        devision(10, 0)

@pytest.mark.parametrize("exeption, div, devider",
                          [(ZeroDivisionError, 10, 0), 
                           (TypeError, 10, '2')]) 
def test_devision_with_error(exeption, div, devider):
    with pytest.raises (exeption):
        devision(div, devider)
