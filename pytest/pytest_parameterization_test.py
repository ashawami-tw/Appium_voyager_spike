import pytest


# run this file using - pytest ./pytest/pytest_parameterization_test.py -s -v

# to pass data set to the test we need to enclose them in tuple and assigning them to params
# then we need to pass request(mandatory keyword) in the method
# this request.param will return chrome first and invoke test test_parametrisation
# then it will return firefox and invoke test test_parametrisation
# then it will return IE and invoke test test_parametrisation

@pytest.fixture(params=["chrome", "firefox", "IE"])
def setup_browser(request):
    return request.param


def test_parametrisation(setup_browser):
    # this will print first chrome then firefox and then IE
    # so this test will run for three different data set
    print(setup_browser)


# if we want to send more info in dataset then enclose them in set
# test_sports will run with ("steve", "steve@gmail.com", "Australia") first
# then with ("Micheal", "micheal@gmail.com", "Australia")
# and then with ("Jimmy", "jimmy@gmail.com", "England")
@pytest.fixture(params=[("steve", "steve@gmail.com", "Australia"), ("Micheal", "micheal@gmail.com", "Australia"),
                        ("Jimmy", "jimmy@gmail.com", "England")])
def setup_sports(request):
    return request.param

def test_sports(setup_sports):
    print(setup_sports)
