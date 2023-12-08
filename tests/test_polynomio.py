import subprocess
import os

def run_test(input_str):
    cmd = ["python3", os.environ['COMMAND_RUN']]
    process = subprocess.Popen(
        cmd, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    output, error = process.communicate(input=input_str)
    process.kill()
    return output.strip()


def test_case1():
    input_str = """\
(4, 6)
[((2, 2), 2)]
[((3, 4), 1), ((2, 3), 1)]
"""
    expected_output = "True"
    assert run_test(input_str) == expected_output


def test_case2():
    input_str = """\
(4, 6)
[((2, 2), 1), ((2, 3), 1)]
[((3, 4), 1), ((2, 3), 1)]
"""
    expected_output = "True"
    assert run_test(input_str) == expected_output


def test_case3():
    input_str = """\
(4, 6)
[((2, 3), 1), ((2, 3), 1)]
[((3, 4), 1), ((2, 3), 1)]
"""
    expected_output = "False"
    assert run_test(input_str) == expected_output


def test_case4():
    input_str = """\
(4, 6)
[((2, 2), 2)]
[((3, 3), 1), ((2, 3), 1)]
"""
    expected_output = "True"
    assert run_test(input_str) == expected_output


def test_case5():
    input_str = """\
(4, 6)
[((2, 2), 2)]
[((4, 3), 1), ((2, 3), 1)]
"""
    expected_output = "False"
    assert run_test(input_str) == expected_output