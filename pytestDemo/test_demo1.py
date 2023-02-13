# Any pyTest file should start with a naming standard = test_
# pyTest methods should start with = test
# Any code should be wrapped in method only

# Running scripts through command prompt -
# cd <navigate to directory part - here it is pytestDemo>
# Will execute the scripts through CMD      = py.test
# Will execute and print more logs          = py.test -v
# Will show logs as well as output if any   = py.test -v -s
# Running selected tests through CMD        = py.test test_demo2.py -v -s
# Running tests using regular expression    = py.test -k <regular_expression> -v -s / py.test -k Variable -v -s
# Running tests using mark                   = py.test -m smoke -v -s
# Skipping tests using mark                  = py.test -v -s (Use @pytest.mark.skip)
# Executing tests using mark but skipping it = py.test -v -s (Use @pytest.mark.xfail)

import pytest


@pytest.mark.smoke
# @pytest.mark.xfail
def test_FirstProgramWelcome():
    print("First Program")


def test_SecondProgramWelcome():
    print("Second Program")

