import pytest

#command line prompts.
#pytest --help
#pytest -v (verbose), -s (statements), -k(keywords)

from question import solution

def test_pass_valid():
    assert solution([1,2,3],3) == 2, "Test pass"

def test_fail():
    assert solution([1,7,11],11) == 0, "Test fail "



