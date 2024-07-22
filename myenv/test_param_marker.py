import pytest

@pytest.mark.parametrize("a,b,final",[(2,3,5),(5,6,20),(10,15,25)])
def test_add(a,b,final):
    assert a+b == final