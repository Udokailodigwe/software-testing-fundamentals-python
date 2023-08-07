import unittest
from customer.test_case_login import TestOnLogin
from customer.test_case_signup import TestOnSignUp
from admin.test_case_assign_role import TestOnAssignRole
from admin.test_case_delete_customer import TestOnDeleteCustomer


#get all test from test module

test_case_1 = unittest.TestLoader().loadTestsFromTestCase(TestOnLogin)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(TestOnSignUp)
test_case_3 = unittest.TestLoader().loadTestsFromTestCase(TestOnAssignRole)
test_case_4 = unittest.TestLoader().loadTestsFromTestCase(TestOnDeleteCustomer)

sanity_test_suite = unittest.TestSuite([test_case_1,test_case_2])
functional_test_suite = unittest.TestSuite([test_case_3, test_case_4])
master_test_suite = unittest.TestSuite([sanity_test_suite, functional_test_suite])
unittest.TextTestRunner().run(master_test_suite)