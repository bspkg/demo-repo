import unittest
from summon_robot import droid_name

class TestSummonRobot(unittest.TestCase):
    def test_droid_name_gold(self):
        result = droid_name('Gold')
        self.assertEqual(result, 'C3P0')

    def test_droid_name_blue(self):
        result = droid_name('Blue')
        self.assertEqual(result, 'R2D2')

    def test_droid_name_unknown(self):
        result = droid_name('Purple')
        self.assertEqual(result, 'Unknown')

if __name__ == '__main__':
    unittest.main()