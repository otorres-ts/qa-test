import unittest
from pages.authenticate_page import AuthenticatePage
from commons import tags
from config.environment_set_up import EnvironmentSetup


class AuthenticateTest(EnvironmentSetup):

    def test_reliq1_verify_authenticate_process_works(self):
        # authenticate process
        post_request_authenticate = AuthenticatePage()
        post_request_authenticate.auth_header

        print(tags.SUCCESSFULLY_AUTHENTICATE)


if __name__ == '__main__':
    unittest.main()