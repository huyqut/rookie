# Unit testing with unittest

import unittest
from python_101.chap27_target import Giant


class TestGiant(unittest.TestCase):

    def setUp(self):
        """ Set up something before EACH test method """
        self.giant = Giant()

    def test_get(self):
        self.assertEqual("Tran Quang Huy", self.giant.name)
        self.assertEqual('abc123', self.giant.id)
        self.assertEqual(123, self.giant.height)

    def test_set(self):
        self.giant.name = 'Tauntaun'
        self.giant.id = '123abc'
        self.giant.height = 139
        self.assertEqual('Tauntaun', self.giant.name)
        self.assertEqual('123abc', self.giant.id)
        self.assertEqual(123, self.giant.height)

    def tearDown(self):
        """ Tear down something after EACH test method """
        pass
