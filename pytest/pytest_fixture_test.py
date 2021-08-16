import pytest
# run this file using - pytest ./pytest/pytest_fixture_test.py -s -v

# fixtures are like @before and @after method in testng
# we can create a fixture and then tie up the test with that fixture
# which we will run that fixture first and then the actual test

# fixture setup is created
@pytest.fixture
def setup():
    print("\n*********** Run me first ***********")
    # for test down we can use same setup method and use yield
    # which will run after test is ran
    yield
    print("\n*********** I am running at end ***********")


# now we have tied following test with setup fixture
# so the setup fixture will run first and then the respective test will run
# we need to pass fixture as an argument to the test
# e.g. setup fixture is passed as an argument to the test_fix_me
# so first setup will run and then test_fix_me
# at end yield will run
# execution will be as setup -> test_fix_me -> yield
def test_fix_me(setup):
    print("I am running after setup is done")