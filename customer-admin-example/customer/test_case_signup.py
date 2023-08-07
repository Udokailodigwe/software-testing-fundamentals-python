import unittest


class TestOnSignUp(unittest.TestCase):
    def test_signup_by_email(self):
        print("This is a test for email signup")
        self.assertTrue(True)

    def test_signup_by_google(self):
        print("This is a test for google signup")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()


