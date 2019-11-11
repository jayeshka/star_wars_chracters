'''
@author: Jayesh Kariya
'''
from mock import Mock
from ApiHelper import ApiHelper
import unittest

class TestAPIHelper(unittest.TestCase):
    def test_star_wars_characters(self):
        apiHelp = ApiHelper()
        expected = ['Test Name', 'Test Height', 'Test Gender']
        apiHelp.star_wars_characters = Mock(return_value=expected)
        self.assertListEqual(apiHelp.star_wars_characters(1), expected)

if __name__ == '__main__':
    unittest.main()