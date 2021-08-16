from test.base import AppiumTest
from main.SignIn import SignIn


class TestSignIn(AppiumTest):
    def test_successful_sign_in(self , set_up):
        SignIn(self.driver).sign_in("steve")


