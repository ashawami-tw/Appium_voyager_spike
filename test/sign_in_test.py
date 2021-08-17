from test.base import AppiumBaseTest
from main.page_actions.sign_in_actions import SignInActions


class TestSignIn(AppiumBaseTest):
    def test_successful_sign_in(self, set_up):
        SignInActions(self.driver).sign_in("alexa")



