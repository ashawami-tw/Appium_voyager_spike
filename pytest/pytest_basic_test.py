# the test file name should either start with test_ or end with _test so that it gets identified as pytest test file
# e.g. naming can be pytest_basic_test.py or test_pytest
# in tyche they have ended the test file with _test

# each test is defined under a test method
# the name of the test method should start with test_ to get identified by pytest
# in tyche they have started the test method name with test_

# to run all tests use command - pytest
# to get details of tests ran use flag -v
# if any print statement is there in test simply running pytest command will not show the output
# so to see this print output use flag -s
# to run the all test with specific keyword use flag -k <keyword>
# e.g. if want to run all tests which contains calc in their test name we can use command as - pytest -k "calc"
# the above example will run only test_addition_calc and test_subtraction_calc tests as they has the calc keyword and will skip test_me
# to run only specific test file use command - pytest <file_name>

# run this file using - pytest ./pytest/pytest_basic_test.py -s -v

def test_addition_calc():
    assert 1 + 1 == 2


def test_subtraction_calc():
    assert 1 - 1 == 2, "The subtraction is wrong"


def test_hello():
    print("\nhello")




