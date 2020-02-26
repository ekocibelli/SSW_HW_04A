import unittest
from HW_04A_ekocibelli import get_user_data
from unittest import mock


class TestGithub(unittest.TestCase):
    @mock.patch('urllib.request.urlopen')
    def test_get_user_data(self, mock_return):
        mock_return.side_effect = [
            '[{"name" : "567"}, {"name" : " 567_HW_04A"}]',
            '[{"1" : "richk"}, {"2" : "richk"}]',
            '[{"1" : "richk"}, {"2" : "richk"}, {"3" : "richk"}]'
        ]
        self.assertEqual(get_user_data('richkempinski'),
                         {'Mocks': 10,
                          'Project1': 2,
                          'hellogitworld': 30,
                          'helloworld': 6,
                          'threads-of-life': 1})


"""
    def test_not_valid_user(self):
        self.assertEqual(get_user_data("ekocibel"), "User ekocibel does not exist.")

    def test_valid_user(self):
        self.assertEqual(get_user_data('richkempinski'),
                         {'Mocks': 10,
                          'Project1': 2,
                          'hellogitworld': 30,
                          'helloworld': 6,
                          'threads-of-life': 1})
"""

if __name__ == '__main__':
    print('Running HW_04A_TESTING.py testing suite...')
    unittest.main(exit=False, verbosity=2)

