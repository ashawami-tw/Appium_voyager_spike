import pytest

# this tis the file where pytest will look for the common fixtures
# if we have common fixture for all the tests then declaring them in each file will unfollow DRY principle
# so we can create that fixture in this file and then tie the tests with this fixture
# pytest will first try to find that fixture in that specific test file
# if does not find then will try to find in conftest.py file
# the name of the file should be mandatory conftest.py

@pytest.fixture
def common_setup():
    print("\n*********** I am common setup and will run at start of the test ***********")
    yield
    print("\n*********** I am running at end of the test ***********")


# if we want to run fixture once when class initiates and tear down at the end of the last test in class
# we can define scope of that fixture in fixture as class
# so this common_setup_class_scoped will run at the start of class and will yield at end of the class
# e.g. @beforeClass and @afterClass in testng
@pytest.fixture(scope="class")
def common_setup_class_scoped():
    print("\n*********** I am running at start of class ***********")
    yield
    print("\n*********** I am running at the end of the class ***********")