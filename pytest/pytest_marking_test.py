import pytest

# run this file using - pytest ./pytest/pytest_marking_test.py -s -v

# we can run the specific tests by marking them as tags
# for that we need to use @pytest.mark.<tag_name>

# if we use smoke as a tag name and we want to run all tests with smoke tag name
# then use flag -m <tag_name>
# e.g. pytest -m "smoke" - will only run test_hello and test_world

@pytest.mark.smoke
def test_hello():
    print("hello")


@pytest.mark.smoke
def test_world():
    print("world")

# if we want to skip any test we can use tag name skip (inbuilt - provided by pytest)
# this will skip the following test when we run all test together
@pytest.mark.skip
def test_skip():
    print("skipping")

# if we can not skip the test as some other test is dependent on this test
# then we can run the test using tag name xfail (inbuilt - provided by pytest)
# this will simply run the test but will not report as pass or fail
@pytest.mark.xfail
def test_just_run():
    print("run me")