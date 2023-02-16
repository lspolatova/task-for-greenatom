from unittest import TestCase
from task_5 import compare_versions


class Test(TestCase):
    def test_compare_versions(self):
        self.assertEqual(compare_versions('1', '2'), -1)
        self.assertEqual(compare_versions('2', '1'), 1)
        self.assertEqual(compare_versions('2', '2'), 0)
        self.assertEqual(compare_versions('1.1', '1.1'), 0)
        self.assertEqual(compare_versions('1.2', '1.1'), 1)
        self.assertEqual(compare_versions('1.1', '1.2'), -1)
        self.assertEqual(compare_versions('1.1', '1.1'), 0)
        self.assertEqual(compare_versions('1.10', '1.1'), 1)
        self.assertEqual(compare_versions('1.1', '1.10'), -1)
        self.assertEqual(compare_versions('1.1.10', '1.1'), 1)
        self.assertEqual(compare_versions('1.1', '1.1.10'), -1)
        self.assertEqual(compare_versions('1', '1.1'), -1)
        self.assertEqual(compare_versions('1.1', '1'), 1)
        self.assertEqual(compare_versions('1.1.1', '1.1.1.1'), -1)
        self.assertEqual(compare_versions('1.1a', '1.1b'), -1)
        self.assertEqual(compare_versions('1.1b', '1.1a'), 1)
        self.assertEqual(compare_versions('1.1a', '1.1a'), 0)
        self.assertEqual(compare_versions('test 0.1b', '0.2'), -1)


