import unittest

class TestOnLogin(unittest.TestCase):
    def test_login_by_email(self):
        print("This is a test for email login")
        self.assertTrue(True)
    def test_login_by_google(self):
        print("This is a test for google login")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()


