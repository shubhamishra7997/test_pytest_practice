import pytest
from question import solution

###PARAMETERIZED FIXTURES
"""
Here the fixture is having an argument param, through which a and b are passed.
So we ran the test couple of times.
When we run, the output shall be:
test_pass_valid_param_fixture[a] a
PASSED
test_pass_valid_param_fixture[b] b
PASSED
test_pass_invalid_param_fixture[a] a
FAILED
test_pass_invalid_param_fixture[b] b
FAILED
"""

@pytest.fixture(params=["a","b"])
def demo_fixture_setup(request):
    print(request.param)


def test_pass_valid_param_fixture(demo_fixture_setup):
    assert solution([1,2,3],3) == 2, "successful valid test set 3"

def test_pass_invalid_param_fixture(demo_fixture_setup):
    assert solution([1,7,11],11) == 0, "Successful invalid test set 3"


