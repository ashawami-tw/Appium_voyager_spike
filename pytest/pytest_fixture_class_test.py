import pytest

# run this file using - pytest ./pytest/pytest_fixture_class_test.py -s -v

# if we want to run the same fixture for all the tests then we need to pass the fixture as argument to each test method
# e.g. test_1(common_setup), test_2(common_setup) , test_3(common_setup) , test_4(common_setup) , test_5(common_setup)
# but if we know all this test method needs common fixture
# we can pass the fixture on class level
# for this @pytest.mark.usefixtures("fixture_name) (inbuilt - provided by pytest) is used

# before every test common_setup will run
# e.g. @beforeMethod and @afterMethod in testng
# common_setuo is common for all tests so declared in conftest.py

@pytest.mark.usefixtures("common_setup")
class Test:
    def test_1(self):
        print("test 1 running")

    def test_2(self):
        print("test 2 running")

    def test_3(self):
        print("test 3 running")

    def test_4(self):
        print("test 4 running")

    def test_5(self):
        print("test 5 running")
