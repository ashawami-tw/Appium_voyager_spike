import pytest
# run this file using - pytest ./pytest/pytest_passing_data_through_fixture_test.py -s -v

# fixtures are like @before and @after method in testng
# we can create a fixture and then tie up the test with that fixture
# which we will run that fixture first and then the actual test

# fixture setup is created
@pytest.fixture
def return_data():
    print("\n*********** fixture: returning data ***********")
    return [1,2,3,4]

def test_returned_data(return_data):
    print(return_data)
    print("I am running after return data is done")


# on class level if we want read the data returned by fixture we need to use @pytest.mark.usefixtures("return_data") on class level
# and need to pass fixture name as an argument to test method to access returned data
@pytest.mark.usefixtures("return_data")
class Test:
    def test_returned_data_on_class_level_1(self, return_data):
        print(return_data)
        print("I am running after return data is done")

    def test_returned_data_on_class_level_2(self, return_data):
        print(return_data)
        print("I am running after return data is done")

    def test_returned_data_on_class_level_3(self):
        print("Test 3")