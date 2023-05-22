import unittest
from app.models import Data

class DataModelTestCase(unittest.TestCase):

    def test_create_data(self):
        data = Data(id=1, name='Test Data', value=10)
        self.assertEqual(data.id, 1)
        self.assertEqual(data.name, 'Test Data')
        self.assertEqual(data.value, 10)

    def test_data_representation(self):
        data = Data(id=1, name='Test Data', value=10)
        self.assertEqual(str(data), 'Test Data')

if __name__ == '__main__':
    unittest.main()
