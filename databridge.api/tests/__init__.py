import unittest

# Import your test modules here
from .test_routes import TestRoutes
from .test_models import DataModelTestCase

# Create the test suite
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRoutes))
    return test_suite

# Run the tests
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
