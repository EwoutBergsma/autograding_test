# DO NOT MODIFY THE CODE IN THIS FILE
import pytest
from testbook import testbook
import random
import os

# This is to prevent: RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq. Registering an additional selector thread for add_reader support via tornado.
if os.name == 'nt':  # Check if running on a Windows machine
    import asyncio
    from asyncio import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# Enables to load parts of a notebook
@pytest.fixture(scope='module')
def tb():
    with testbook('assignments.ipynb', execute=True) as tb:
        yield tb

################### Assignment 1a ###################

# Tests assignment 1a, by performing a series of unittests using static test_inputs and corresponding expected values.
@pytest.mark.parametrize("test_input,expected", [([1, 2], 3), ([3.5, 7.13], 10.63), ([-13.23, 6], -7.23)])
def test_assignment_1a_static(tb, test_input, expected):
    student_add = tb.ref("add")
    assert student_add(test_input[0], test_input[1]) == pytest.approx(expected, 0.01)

# Tests assignment 1a, by performing a series of unittests using random test_inputs and corresponding expected values.
@pytest.mark.parametrize("test_input", [([random.uniform(-10, 10), random.uniform(-10, 10)]), ([random.uniform(-10, 10), random.uniform(-10, 10)]), ([random.uniform(-10, 10), random.uniform(-10, 10)])])
def test_assignment_1a_random(tb, test_input):
    student_add = tb.ref("add")
    assert student_add(test_input[0], test_input[1]) == pytest.approx(test_input[0] + test_input[1], 0.01)

################### Assignment 1b ###################

# Tests assignment 1a, by performing a series of unittests using static test_inputs and corresponding expected values.
@pytest.mark.parametrize("test_input", [([1, 2]), ([3.5, 7.13]), ([-13.23, 6])])
def test_assignment_1b_static(tb, test_input):
    student_multiply = tb.ref("multiply")
    assert student_multiply(test_input[0], test_input[1]) == pytest.approx(test_input[0] * test_input[1], 0.01)

# Tests assignment 1a, by performing a series of unittests using random test_inputs and corresponding expected values.
@pytest.mark.parametrize("test_input", [([random.uniform(-10, 10), random.uniform(-10, 10)]), ([random.uniform(-10, 10), random.uniform(-10, 10)]), ([random.uniform(-10, 10), random.uniform(-10, 10)])])
def test_assignment_1b_random(tb, test_input):
    student_multiply = tb.ref("multiply")
    assert student_multiply(test_input[0], test_input[1]) == pytest.approx(test_input[0] * test_input[1], 0.01)

################### Assignment 2 ###################

def test_assignment_2(tb):
    student_print = tb.ref("awesome_string")
    assert student_print() == "automatic assignments are fun!"
