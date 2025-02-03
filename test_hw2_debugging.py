import pytest  # Keep pytest import because the homework requires using pytest
from hw2_debugging import merge_sort

@pytest.mark.parametrize("input_arr, expected", [
    ([1, 2, 3], [1, 2, 3]),  # Already sorted list
    ([3, 1, 2], [1, 2, 3]),  # Unsorted list
    ([], []),                # Empty list
])
def test_merge_sort(input_arr, expected):
    """Test merge_sort with different inputs."""
    assert merge_sort(input_arr) == expected
