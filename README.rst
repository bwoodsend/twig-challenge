=====================
Twig Coding Challenge
=====================

A basic repo containing my solution to Twig's coding challenge.


Installation
------------

To install this package and all its (currently non existent) dependencies
directly from Github use::

    pip install https://github.com/bwoodsend/twig-challenge/archive/refs/heads/master.zip

To uninstall, use::

    pip uninstall twig-challenge


Usage
-----

The sole member of this package is the ``group_array_elements()`` function to
split a list or array into a specified number of groups of (if possible) equal
lengths.
Its basic usage:

.. code-block:: python

    >>> import twig_challenge

    # Divide 6 elements into 2 groups of 3...
    >>> twig_challenge.group_array_elements([1, 2, 3, 4, 5, 6], 2)
    [[1, 2, 3], [4, 5, 6]]

    # ... or into 3 groups of 2.
    >>> twig_challenge.group_array_elements([1, 2, 3, 4, 5, 6], 3)
    [[1, 2], [3, 4], [5, 6]]

If it is impossible to divide equally, the last group(s) are shortened.

.. code-block:: python

      # Divide 5 elements into 3 groups with the last group being shorter to
      # accommodate 5 not being divisible by 3.
      >>> twig_challenge.group_array_elements([1, 2, 3, 4, 5], 3)
      [[1, 2], [3, 4], [5]]

      # Divide 3 elements into 6 groups.
      >>> twig_challenge.group_array_elements([1, 2, 3], 6)
      [[1], [2], [3], [], [], []]


Hacking
-------

The remainder of this page is a guide for future developers.


Setup
*****

Install an editable clone of this repo by first cloning this repo::

    git clone https://github.com/bwoodsend/twig-challenge.git
    cd twig-challenge

Then installing in editable mode::

    pip install -e .

In editable (or `symlinked`) mode, changes you make to this repo will propagate
automatically - no need to reinstall.


Testing
*******

Install the test requirements using the following
(assuming the root of this repository is your current working directory)::

    pip install -e .[test]

Then run the test suite using::

    pytest

