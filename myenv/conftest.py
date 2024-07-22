
import pytest

##fixture
#pre condition/setup/arrange:
# yield to do act and assert
# post condition/teardown/cleanup
@pytest.fixture()
def setup():
    print("Array is ready")
    print("Numbers are sorted")
    print("Ready to execute test")
    yield #where the act and assert happens
    print("Element position found")
    print("Exit")

"""
#Run on all tests in the folder
@pytest.fixture(autouse = True)
def setup():
    print("Array is ready")
    print("Numbers are sorted")
    print("Ready to execute test")
    yield #where the act and assert happens
    print("Element position found")
    print("Exit")
"""

