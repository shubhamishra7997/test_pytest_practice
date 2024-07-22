import pytest

from question import solution

### GROUPINGs
#pytest --markers (list of markers that exist)
#custom marker
#pytest -marker sanity
#pytest -marker regresssion

#given markers
#skip
#xfail


def test_pass_mark():
    assert solution([1,2,3],3) == 2, "Test pass"

def test_fail_mark():
    assert solution([1,7,11],11) == 0, "Fail test"

#group tests into custom markers.
@pytest.mark.sanity
def test_pass_valid_mark():
    assert solution([1,2,3],3) == 2, "successful valid test set 2"


#group tests into custom markers.
@pytest.mark.regression
def test_pass_valid_mark():
    assert solution([1,2,3],3) == 2, "Test pass"

#group tests into custom markers.
@pytest.mark.sanity
def test_pass_invalid_mark():
    assert solution([1,7,11],11) == 0, "Test fail "

#skip this tests, due to bug or waiting for new release.
@pytest.mark.skip
def test_pass_invalid_skip_mark():
    assert solution([1,7,11],77) == 0, "Test skip "

#xfail can be used to write test cases in advance of development, so that there is no waiting
# once the code is developed by the user, xfail can then be removed.
@pytest.mark.xfail
def test_pass_invalid_xfail_mark():
    assert solution([1,7,11],77) == 0, "Test will not be marked as fail (expected fail) "



