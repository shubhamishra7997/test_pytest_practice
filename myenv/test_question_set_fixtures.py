import pytest
from question import solution

###FIXTURES
"""
Arrange, Act, Assert, Cleanup.
Fixture takes care of Arrange (setup) and Cleanup (teardown).
"""

##fixture
#pre condition/setup/arrange:
# yield to do act and assert
# post condition/teardown/cleanup
#moved to conftest.py for universal access
@pytest.fixture
def setup():
    print("Array is ready")
    print("Numbers are sorted")
    print("Ready to execute test")
    yield #where the act and assert happens
    print("Element position found")
    print("Exit")

def test_pass_valid_fixture(setup):
    assert solution([1,2,3],3) == 2, "successful valid test set 3"

def test_pass_invalid_fixture(setup):
    assert solution([1,7,11],11) == 0, "Successful invalid test set 3"


