import pytest
from twig_challenge import group_array_elements


def test_groupArrayElements():
    """Test twig_challenge.group_array_elements()."""

    # Test some homogenous cases.
    assert group_array_elements([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert group_array_elements([1, 2, 3, 4, 5, 6], 3) \
           == [[1, 2], [3, 4], [5, 6]]

    # And some inhomogeneous cases.
    assert group_array_elements([1, 2, 3, 4, 5], 2) == [[1, 2, 3], [4, 5]]
    assert group_array_elements([1, 2, 3, 4, 5], 3) == [[1, 2], [3, 4], [5]]

    # Try with some alternative types.
    assert group_array_elements(range(10), 3) \
           == [range(4), range(4, 8), range(8, 10)]

    # Verify that the safely net for invalid **group_count** count works and
    # the string formatting is correct.
    with pytest.raises(ValueError, match="Parameter group_count=-4 is"):
        group_array_elements([1, 2, 3], -4)

    # Test some quirkier inputs:
    # No data. Should create empty groups.
    assert group_array_elements([], 3) == [[], [], []]
    # More groups than data. The second last as well as the last group will be
    # empty.
    assert group_array_elements([1, 2], 4) == [[1], [2], [], []]
