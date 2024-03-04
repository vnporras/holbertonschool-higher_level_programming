#!/usr/bin/python3

import unittest

Base = __import__('base').Base 

class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.Base = Base()

    def test_id_generation(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_passed(self):
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_none(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

if __name__ == '__main__':
    unittest.main()
