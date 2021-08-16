import pytest

# run this file using - pytest ./pytest/pytest_fixture_running_once_for_a_class_test.py -s -v

# if we want to run fixture once when class initiates and tear down at the end of the last test in class
# we can define scope of that fixture in fixture
# e.g. @beforeClass and @afterClass in testng
# we can pass the fixture on class level
# for this @pytest.mark.usefixtures("fixture_name) (inbuilt - provided by pytest) is used

# before every first test common_setup_class_scoped will run
# and it will end/tear down at end of last test
# so we can see
# common_setup_class_scoped is common for all tests so declared in conftest.py

@pytest.mark.usefixtures("common_setup_class_scoped")
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


# for following class we are not passing the fixture common_setup_class_scoped as on class level by using @pytest.mark.usefixtures("common_setup_class_scoped")
# we can pass fixture common_setup_class_scoped at test_3 as argument and it will run first and will end/teardown at end of the class

class TestStartAtAnyTest:
    def test_1(self):
        print("test 1 running")

    def test_2(self):
        print("test 2 running")

    def test_3(self , common_setup_class_scoped):
        print("test 3 running")

    def test_4(self):
        print("test 4 running")

    def test_5(self):
        print("test 5 running")
