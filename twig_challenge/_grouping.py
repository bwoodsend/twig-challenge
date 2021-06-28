import math


def group_array_elements(container, group_count):
    """Divide a **container** into equally sized groups.

    Args:
        container:
            The input data to divide. Must support slicing and ``len()``.
        group_count:
            The number of groups to divide into.

    Returns:
        A list of **group_count** groups.

    Raises:
        ValueError:
            If **group_count** is zero or negative.

    Where the size of the original array cannot be divided equally by
    **group_count**, elements are deducted last group(s) to make up the
    difference.

    Examples::

        # Divide 6 elements into 2 groups of 3...
        >>> group_array_elements([1, 2, 3, 4, 5, 6], 2)
        [[1, 2, 3], [4, 5, 6]]
        # ... or into 3 groups of 2.
        >>> group_array_elements([1, 2, 3, 4, 5, 6], 3)
        [[1, 2], [3, 4], [5, 6]]
        # Divide 5 elements into 3 groups with the last group being shorter to
        # accomodate 5 not being divisible by 3.
        >>> group_array_elements([1, 2, 3, 4, 5], 3)
        [[1, 2], [3, 4], [5]]

    .. note::

        The output is always of type ``list()`` but the type of each group
        is the type given by slicing **container** directly.

    """
    # Don't allow non-positive ``group_count``. Otherwise we could end up with
    # infinite or negative group lengths.
    if group_count <= 0:
        raise ValueError(
            f"Parameter group_count={group_count} is non-positive. A container "
            f"can't be divided into a non-positive number of groups.")

    # Work out how long each group will be.
    group_length = len(container) / group_count
    # In the case when the input doesn't divide equally, this is length of all
    # groups except the last, which will be shorter.
    group_length = math.ceil(group_length)

    grouped = []
    # For each group:
    for i in range(group_count):
        # Find the starting and ending index.
        # Note that out of bounds slices are clipped automatically so that,
        # even when the input doesn't divide equally, there is no need to clip
        # ``end`` to less than ``len(container)``.
        start = i * group_length
        end = start + group_length

        # Finally, slice the container into a new group.
        grouped.append(container[start:end])

    return grouped
